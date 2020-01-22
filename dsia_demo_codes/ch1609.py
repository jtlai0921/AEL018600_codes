import pandas as pd

titanic = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
digit_recognizer = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Digit-Recognizer/train.csv")
unique_digits = digit_recognizer["label"].unique()
unique_digits.sort()
print("Binaray classification:")
print(titanic["Survived"].unique())
print("Multi-class classification:")
print(unique_digits)