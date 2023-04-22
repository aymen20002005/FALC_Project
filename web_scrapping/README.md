# <span style="font-size: 24px;">Extraction de phrases simples à partir de Wikipédia : processus et résultats
Dans cette section, l'objectif est d'extraire des phrases simples de Wikipédia qui peuvent être considérées comme FALC (Français Facile À Lire et à Comprendre). 

Ces phrases seront utilisées dans une prochaine étape pour générer artificiellement un dataset afin d'entraîner un modèle d'intelligence artificielle. Le résultat final de cette étape est enregistré dans le fichier `simple_french.xlsx`.

# <span style="font-size: 22px;">Extraction de phrases simples à partir de Wikipédia
Le script `web_scarp.txt` extrait des phrases simples en français à partir d'articles Wikipédia aléatoires. Le processus suit les étapes suivantes :

## <span style="font-size: 18px;">1. Récupération d'articles aléatoires de Wikipédia
On récupère un certain nombre d'articles Wikipédia en utilisant l'API REST de Wikipédia. (à définir dans le script)

## <span style="font-size: 18px;">2. Calcul des fréquences de mots
On analyse chaque article pour déterminer la fréquence de chaque mot.

## <span style="font-size: 18px;">3. Identification des mots simples
En utilisant la loi de Zipf et un seuil de fréquence, les mots simples sont identifiés. (Le seuil dans le code est défini à 15 mots, ce qui signifie que si un mot se répète 15 fois dans un article, il est considéré comme étant simple)

## <span style="font-size: 18px;">4. Extraction de phrases simples
Le programme extrait ensuite des phrases simples à partir des articles en se basant sur les mots simples identifiés.

## <span style="font-size: 18px;">5. Encodage des phrases simples
Chaque phrase simple est encodée à l'aide du modèle pré-entraîné BERT (ici, "dbmdz/bert-base-french-europeana-cased").

## <span style="font-size: 18px;">6. Regroupement des phrases encodées
Les phrases encodées sont regroupées en utilisant l'algorithme K-Means (30 groupes).

## <span style="font-size: 18px;">7. Sauvegarde des phrases regroupées
Les phrases les plus simples sont ensuite sauvegardées dans un fichier texte.

## <span style="font-size: 18px;">8. Filtrage des phrases
Enfin, le programme filtre les phrases en ne conservant que celles ayant un nombre de mots compris entre une valeur minimale et une valeur maximale (ici, entre 3 et 8 mots).

# <span style="font-size: 22px;">Test
1. En exécutant le script sur plusieurs instances EC2 et en effectuant plusieurs tests, tous les résultats obtenus ont été fusionnés dans un unique fichier "merged-output.txt". Ce fichier contient des phrases simples provenant de Wikipédia, mais une étape de nettoyage supplémentaire est requise car certaines phrases présentent des erreurs grammaticales.

2. Le nombre d'articles défini dans `scarp.py` est de 15 000, ce qui génère environ 2 600 phrases et nécessite une durée d'exécution de 6 heures. Bien qu'il soit possible de lancer plusieurs threads en même temps, il convient de rester vigilant car certains peuvent être interrompus avant la fin en fonction des ressources de l'instance. 

3. `merged-output.txt` est le résultat de la fusion de plusieurs fichiers txt et contient 18 000 phrases. Ce nombre diminuera à 4 300 après la phase de nettoyage.

# <span style="font-size: 22px;">Nettoyage

Le code dans `cleanup.ipynb` traduit et conserve que les bonne phrases **<span style="font-size: 15px;">qu'on peut consideré comme FALC (Français Facile À Lire et à Comprendre) mais nous sommes pas totalement sur du vrai FALC** . Le processus suit les étapes suivantes :

## <span style="font-size: 18px;">1. Chargement et traduction des phrases en anglais
On charge les phrases en français à partir d'un fichier texte, puis les traduit en anglais à l'aide de la bibliothèque `mtranslate`. Les phrases traduites sont enregistrées dans un fichier texte intermédiaire.

## <span style="font-size: 18px;">2. Vérification de la grammaire
Le programme vérifie ensuite la grammaire des phrases en anglais à l'aide de la bibliothèque `spacy`. Il filtre les phrases qui ne respectent pas certaines règles grammaticales, telles que la présence d'un sujet et d'un verbe, l'utilisation de la voix active et du présent, etc. Les phrases valides sont enregistrées dans un autre fichier texte.

## <span style="font-size: 18px;">3. Traduction des phrases simplifiées en français
Les phrases en anglais sont à nouveau traduites en français, en utilisant `mtranslate`. Les phrases traduites sont enregistrées dans un fichier texte final.

## <span style="font-size: 18px;">4. Exportation des phrases simplifiées au format xlsx
Enfin, le programme lit les phrases simplifiées en français à partir du fichier texte final et les enregistre dans un fichier xlsx pour une meilleure visualisation, avec chaque phrase dans une ligne séparée.
