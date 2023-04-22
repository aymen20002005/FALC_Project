import requests
from bs4 import BeautifulSoup
from collections import Counter
import numpy as np
import enchant
import requests
import json
import concurrent.futures
import math
import nltk
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
import datetime

dictionary = enchant.Dict("fr")
word_freqs = Counter()
current_size = 0

# Set maximum size max is 10/12 gb (collab limitation)
max_size = 50 * 1024 * 1024 * 1024

# Define the number of articles you want to retrieve (>5000 for decent results)
n_articles = 1000

urls = [] 
def fetch_random_article():
    response = requests.get("https://fr.wikipedia.org/api/rest_v1/page/random/summary")
    data = json.loads(response.text)
    url = data["content_urls"]["desktop"]["page"]
    return url

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_url = {executor.submit(fetch_random_article): i for i in range(n_articles)}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future.result()
        urls.append(url)

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    text = ''.join([i for i in text if not i.isdigit()])
    words = text.split()
    for word in words:
        if dictionary.check(word):
            word_freqs[word] += 1
    current_size += len(text)
    if current_size >= max_size:
        break

# Zipf's law
if len(word_freqs) > 1:
    ranks = range(1, len(word_freqs) + 1)
    freqs = [count for _, count in word_freqs.items()]
    log_ranks = np.log(ranks)
    log_freqs = np.log(freqs)
    a, b = np.polyfit(log_ranks, log_freqs, 1)
else:
    a, b = None, None

# Identify simple words
simple_words = set()
word_freqs_list = word_freqs.most_common()
threshold_frequency = 15 # Set a threshold frequency to define what constitutes a simple word
for word, freq in word_freqs_list:
    if freq > threshold_frequency:
        simple_words.add(word)


# now that we have defined the simple words we can extract sentences based on this simple words 


tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-french-europeana-cased")
model = AutoModel.from_pretrained("dbmdz/bert-base-french-europeana-cased")
nltk.download('punkt')
def extract_phrases(text):
    phrases = nltk.sent_tokenize(text)
    simple_phrases = []
    for phrase in phrases:
        words = phrase.split()
        simple = True
        for word in words:
            if word not in simple_words:
                simple = False
                break
        if simple:
            simple_phrases.append(phrase)
    return simple_phrases

def encode_phrase(phrase):
    input_ids = tokenizer.encode(phrase, return_tensors='pt')
    with torch.no_grad():
        encoded_phrase = model(input_ids).last_hidden_state[0][0].numpy()
    return encoded_phrase

simple_phrases = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    text = ''.join([i for i in text])
    simple_phrases += extract_phrases(text)

encoded_phrases = []
for phrase in simple_phrases:
    encoded_phrase = encode_phrase(phrase)
    encoded_phrases.append(encoded_phrase)


encoded_phrases = np.array(encoded_phrases)

kmeans = KMeans(n_clusters=30)
kmeans.fit(encoded_phrases)

cluster_labels = kmeans.labels_


# we save the output into a txt file
now = datetime.datetime.now()
output_file_name = f'output-{now.strftime("%Y-%m-%d-%H-%M-%S")}.txt'

with open(f'/home/ubuntu/scarp/{output_file_name}', 'w') as f:
    for cluster_label in set(cluster_labels):
        cluster = np.where(cluster_labels == cluster_label)[0]
        for i in cluster:
            f.write(f'{simple_phrases[i]}\n')
# we cleanup a bit the output, we preserve only the sentences that have less than 8 words

min_words = 3
max_words = 8

with open(f'/home/ubuntu/scarp/{output_file_name}', "r") as file:
    lines = file.readlines()

lines = list(set(line.strip() for line in lines if len(line.strip().split()) >= min_words and len(line.strip().split()) <= max_words))

with open(f'/home/ubuntu/scarp/{output_file_name}', "w") as file:
    file.writelines("\n".join(lines))
