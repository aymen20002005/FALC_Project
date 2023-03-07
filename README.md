# FALC

Cette repository a été créée dans le but de rassembler les solutions algorithmiques de notre projet "Projet d'Ingénieur en Equipe : Traduction automatique de contenu textuel en FALC" à l'ENSTA. Cette repository servira également de lieu de stockage pour les documents utiles, permettant ainsi d'assurer une gestion de version rigoureuse.

## Génération de données

Le **dossier** `web_scrapping` contient un script `scrapping.ipynb` qui peut être testé en l'uploadant sur votre Drive. Le script génère trois fichiers intermédiaires, mais le résultat final est stocké dans `output4.txt`, où vous trouverez des phrases simples en français.

Notez que le script peut prendre environ 2 heures pour traiter 7000 articles de Wikipédia. Vous pouvez le tester sur moins d'articles si vous le souhaitez.

Le **dossier** `generation` contient également un script qui sert à complexifier les phrases du fichier `output3.txt`. Vous pouvez voir les résultats finaux en dans le fichier `output4_translated.xlsx`.


## Tâches à accomplir

Voici une liste de tâches à accomplir pour améliorer notre projet :

~~1. Complexifier les phrases simples et enregistrer les paires phrase-complexe/phrase-simple dans un fichier Excel.~~
2. Entraîner un modèle pré-entraîné BERT ou GPT-2 sur notre dataset.
3. Inclure une autre dataset (romans, etc.).
4. Optimiser et fine-tuner le modèle.
