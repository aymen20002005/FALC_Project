# <span style="font-size: 24px;"> Génération de phrases complexes à partir de phrases simples.
Cette section est dédiée à la génération de phrases complexes à partir des phrases simples extraites de Wikipédia. Nous explorerons deux approches différentes.

# <span style="font-size: 22px;"> GPT-2

La première solution consiste à utiliser GPT-2 en anglais pour générer les résultats, puis les traduire à nouveau en français. Cependant, les résultats obtenus avec cette méthode n'ont pas été très satisfaisants, c'est pourquoi je ne vais pas trop la détailler. Le code correspondant est disponible dans le dossier "gpt2", et le fichier de sortie final se trouve dans "output4_translated.xlsx".

# <span style="font-size: 22px;"> GPT-3

La deuxième approche, plus adaptée, consiste à utiliser l'API de OpenAI pour générer des phrases complexes en utilisant GPT-3.5. Avec un compte gratuit, le nombre de requêtes est limité à 3 par minute, et la complexification de 4 300 phrases a pris plus de 24 heures. Pour obtenir des résultats plus rapidement, il est possible d'utiliser un compte payant. Le fichier final contenant les phrases générées, qui sera utilisé pour entraîner notre modèle, se trouve dans le dossier "gpt3", sous le nom de "dataset.xlsx".