
# <span style="font-size: 24px;"> Entraînement d'un modèle T5 pour simplifier des phrases en français

Nous allons ensuite entraîner un modèle sur notre dataset artificiel. Après plusieurs expérimentations, j'ai choisi de fine-tuner le modèle T5-small, disponible sur Hugging Face.

L'architecture du T5 basé sur l'architecture de transformerest constituée d'un encodeur et d'un décodeur. L'encodeur transforme la représentation de la séquence d'entrée en un espace de haute dimensionnalité et le décodeur génère la séquence de sortie à partir de cette représentation. Le T5 utilise également un mécanisme d'attention qui permet au modèle de se concentrer sur les parties pertinentes de la séquence d'entrée pour générer la séquence de sortie.

Ce modèle est pré-entraîné sur une grande quantité de données à partir de diverses tâches de NLP, telles que la traduction de langue, la classification de texte, etc. Le modèle est entraîné à générer des paires de texte à partir d'une grande variété de tâches, ce qui permet d'obtenir une représentation de langage naturel généralisable pour de nombreuses tâches de NLP.


Le T5-small, en particulier, est un modèle de petite taille avec une capacité de traitement limitée, mais qui reste néanmoins utile pour de nombreuses tâches de NLP comme la nôtre.

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
