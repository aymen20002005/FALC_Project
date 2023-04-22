# Extraction de phrases simples à partir de Wikipédia

Ce script `web_scarp.txt` extrait des phrases simples en français à partir d'articles Wikipédia aléatoires. Le processus suit les étapes suivantes :

## 1. Récupération d'articles aléatoires de Wikipédia
Il récupère un certain nombre d'articles Wikipédia en utilisant l'API REST de Wikipédia.

## 2. Calcul des fréquences de mots
Le programme analyse chaque article pour déterminer la fréquence de chaque mot.

## 3. Identification des mots simples
En utilisant la loi de Zipf et un seuil de fréquence, les mots simples sont identifiés. (Le seuil dans le code est défini à 15 mots, ce qui signifie que si un mot se répète 15 fois dans un article, il est considéré comme étant simple)

## 4. Extraction de phrases simples
Le programme extrait ensuite des phrases simples à partir des articles en se basant sur les mots simples identifiés.

## 5. Encodage des phrases simples
Chaque phrase simple est encodée à l'aide du modèle pré-entraîné BERT (ici, "dbmdz/bert-base-french-europeana-cased").

## 6. Regroupement des phrases encodées
Les phrases encodées sont regroupées en utilisant l'algorithme K-Means (30 groupes).

## 7. Sauvegarde des phrases regroupées
Les phrases les plus simples sont ensuite sauvegardées dans un fichier texte.

## 8. Filtrage des phrases
Enfin, le programme filtre les phrases en ne conservant que celles ayant un nombre de mots compris entre une valeur minimale et une valeur maximale (ici, entre 3 et 8 mots).

# Test
En exécutant le script sur plusieurs instances EC2 et en effectuant plusieurs tests, tous les résultats obtenus ont été fusionnés dans un unique fichier "merged-output.txt". Ce fichier contient des phrases simples provenant de Wikipédia, mais une étape de nettoyage supplémentaire est requise car certaines phrases présentent des erreurs grammaticales.

# Nettoyage

le code dans `cleanup.ipynb` traduit et conserve que les bonne phrases qu'on peut consideré comme FALC (Français Facile À Lire et à Comprendre). Le processus suit les étapes suivantes :

## 1. Chargement et traduction des phrases en anglais
Il charge les phrases en français à partir d'un fichier texte, puis les traduit en anglais à l'aide de la bibliothèque `mtranslate`. Les phrases traduites sont enregistrées dans un fichier texte intermédiaire.

## 2. Vérification de la grammaire
Le programme vérifie ensuite la grammaire des phrases en anglais à l'aide de la bibliothèque `spacy`. Il filtre les phrases qui ne respectent pas certaines règles grammaticales, telles que la présence d'un sujet et d'un verbe, l'utilisation de la voix active et du présent, etc. Les phrases valides sont enregistrées dans un autre fichier texte.

## 3. Traduction des phrases simplifiées en français
Les phrases en anglais sont à nouveau traduites en français, en utilisant `mtranslate`. Les phrases traduites sont enregistrées dans un fichier texte final.

## 4. Exportation des phrases simplifiées au format xlsx
Enfin, le programme lit les phrases simplifiées en français à partir du fichier texte final et les enregistre dans un fichier xlsx pour une meilleure visualisation, avec chaque phrase dans une ligne séparée.
