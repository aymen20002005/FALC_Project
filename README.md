# FALC

Cette repository a été créée dans le but de rassembler les solutions algorithmiques de notre projet "Projet d'Ingénieur en Equipe : Traduction automatique de contenu textuel en FALC" à l'ENSTA. Cette repository servira également de lieu de stockage pour les documents utiles, permettant ainsi d'assurer une gestion de version rigoureuse.

## Génération de données

Le dossier `web_scrapping` contient un script `scrapping.ipynb` qui peut être testé en l'uploadant dans votre Drive. Le script génère trois fichiers intermédiaires, mais le résultat final est stocké dans `output4.txt` où vous trouverez des phrases en français simples.

Notez que le script peut prendre environ 2 heures pour traiter 7000 articles de Wikipedia.

## Tâches à accomplir

Voici une liste de tâches à accomplir pour améliorer notre projet :

1. Complexifier les phrases simples et enregistrer les paires phrase-complexe/phrase-simple dans un fichier Excel.
2. Entraîner un modèle pré-entraîné BERT ou GPT-2 sur notre dataset.
3. Inclure une autre dataset (romans, etc.).
4. Optimiser et fine-tuner le modèle.
