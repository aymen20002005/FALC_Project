
# <span style="font-size: 24px;"> Entraînement d'un modèle T5 pour simplifier des phrases en français

Nous allons ensuite entraîner un modèle sur notre dataset artificiel. Après plusieurs expérimentations, j'ai choisi de fine-tuner le modèle T5-Base, disponible sur Hugging Face.

## <span style="font-size: 18px;"> 1. Préparation des données
on lit le fichier `dataset.xlsx` contenant des phrases complexes et simples, et les sépare en deux fichiers texte. Les phrases complexes sont également nettoyées pour supprimer les guillemets doubles.

## <span style="font-size: 18px;"> 2. Chargement du modèle T5 et du tokenizer
Le modèle T5 et le tokenizer sont chargés à partir de la bibliothèque `transformers`.

## <span style="font-size: 18px;"> 3. Lecture des phrases simples et complexes
Les phrases simples et complexes sont lues à partir des fichiers texte, puis un jeu de données est créé à partir de ces phrases.(Il est important de vérifier après l'exécution du code que les deux fichiers ont le même nombre de lignes.)

## <span style="font-size: 18px;"> 4. Séparation des données
Le jeu de données est divisé en ensembles d'entraînement et de validation.

## <span style="font-size: 18px;"> 5. Prétraitement des données
Les données sont prétraitées et tokenisées avant l'entraînement.

## <span style="font-size: 18px;"> 6. Entraînement  et sauvegarde du modèle entraîné
Le modèle est ensuite entraîné et sauvegardés pour une utilisation ultérieure.

## <span style="font-size: 18px;"> 7. Test de simplification de phrases
Le modèle est chargé à partir du fichier sauvegardé, et une phrase est simplifiée pour le tester.

# <span style="font-size: 22px;"> Quelques optimisations possibles

1. L'apprentissage de notre modèle a été réalisé sur Google Colab afin de réduire les coûts, toutefois il est envisageable de l'exécuter sur une instance plus puissante et d'utiliser, par exemple, t5-base ou t5-large.

2. Notre ensemble de données de 4300 phrases n'est pas très étendu, un overfitting apparaît dès les premiers 20 epochs, il est possible de générer davantage de phrases pour entraîner plus le modèle et améliorer le résultat final.
