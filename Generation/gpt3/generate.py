import openai
import pandas as pd
import time

openai.api_key = "api key"

df = pd.read_excel("/home/ubuntu/res/simple_french.xlsx", sheet_name="Sheet1",names=["A"])
def generate_complex_sentence(sentence):
    input_text = f"Dans le but d'entrainer un model Bert pour la traduction du francais complexe en frnacais FALC Transformez cette phrase simple en une phrase plus complexe gramaticalment(la phrase complexe doit avoir au moins 10 mots): '{sentence}'"
    try :
      response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[{"role": "user", "content": input_text }]
)
      message = response['choices'][0]['message']['content']
      return message
    except Exception as e:
        print(f"Error generating complex sentence for '{sentence}': {e}")
        print("Waiting for 2 minute before retrying...")
        time.sleep(120)
        return generate_complex_sentence(sentence)
complex_sentences = []
i=0
for sentence in df['A']:
    complex_sentence = generate_complex_sentence(sentence)
    complex_sentences.append(complex_sentence)
    print(i,flush=True)
    time.sleep(21)

df['B'] = complex_sentences

df.to_excel("/home/ubuntu/res/dataset.xlsx", index=False)
