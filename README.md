# FALC

Cette repo a été créée dans le but de rassembler les solutions algorithmiques de notre projet "Projet d'Ingénieur en Equipe : Traduction automatique de contenu textuel en FALC" à l'ENSTA. Cette repository servira également de lieu de stockage pour les documents utiles, permettant ainsi d'assurer une gestion de version rigoureuse.
## Quelques résultats

<img src="https://github.com/fira7s/FALC/blob/main/blob/4.PNG" alt="Test 1" width="420">
<img src="https://github.com/fira7s/FALC/blob/main/blob/5.PNG" alt="Test 2" width="420">


## Démarche

Le but de ce projet est de concevoir une application capable de traduire du français complexe en FALC (Facile à Lire et à Comprendre) en utilisant l'intelligence artificielle.

**Les modèles NLP** (Natural Language Processing) de l'intelligence artificielle, tels que le T5 que nous avons entraîné (plus précisément, fine-tuné), nécessitent évidemment des données sur lesquelles ils doivent s'entraîner. Cependant, il n'y a pas suffisamment de textes FALC disponibles sur l'internet avec les textes complexes correspondants. Par conséquent, il n'existe pas de dataset prêt pour entraîner le modèle.

L'approche accessible pour nous en tant qu'étudiant est la **data augmentation**. Nous essayons d'extraire des phrases simples de Wikipédia et de les complexifier pour ainsi créer notre propre dataset artificiel accessible ici `Generation/gpt3/dataset.xlsx`. 

Vous pouvez voir les détails de cette partie ci-dessous.


## Génération de données
### Scarping
Le **dossier** `web_scraping` contient un script `web_scrap.py` ainsi qu'un autre code `cleanup.ipynb.`. Ces codes nous permettent tout d'abord d'extraire des phrases simples depuis Wikipédia. Ensuite, nous les filtrons afin d'obtenir, au final, des phrases qui peuvent être considérées comme FALC selon nos modestes critères.

Voici quelques phrases extraites avec cette démarche :
```
Il résiste bien au vent.
Il passe en dernier.
La cathédrale a cinq portes.
```

### Complexification

Le **dossier** `generation` contient du code qui sert à complexifier les phrases simples extraites de FALC en phrases plus complexes.

Voici quelques exemples de phrases issues de ce processus :
```
Bien que le vent souffle avec force, il est remarquablement résistant.

Bien qu'il soit souvent en avance, il a décidé de passer en dernier cette fois-ci pour laisser aux autres participants le temps de s'organiser avant lui.

La cathédrale dispose de cinq entrées distinctes permettant aux fidèles de pénétrer dans l'édifice religieux majestueux et de s'imprégner de sa grandeur architecturale.
```
## Tâches à accomplir

1. ~~Extraire des phrases simples de Wikipédia.~~
2. ~~Complexifier les phrases simples et enregistrer les paires phrase-complexe/phrase-simple dans un fichier Excel.~~
3. ~~Fine-tuner un modèle pré-entraîné sur notre dataset.~~
4. ~~Créer une interface graphique conviviale et ergonomique pour l'utilisateur.~~
5. Inclure un autre dataset de textes variés tels que des romans, afin d'enrichir notre corpus en FALC de meilleure qualité.
6. Réviser l'architecture du modèle pour qu'il soit mieux adapté à l'apprentissage et la génération de textes FALC.

