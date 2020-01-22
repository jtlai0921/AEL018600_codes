import pandas as pd
import random

def get_train_validation(labeled_df, validation_size=0.3, random_state=123):
  """
  Getting train/validation data from labeled dataframe
  """
  m = labeled_df.shape[0]
  row_indice = list(labeled_df.index)
  random.Random(random_state).shuffle(row_indice)
  shuffled = labeled_df.loc[row_indice, :]
  validation_threshold = int(validation_size * m)
  validation = shuffled.iloc[0:validation_threshold, :]
  train = shuffled.iloc[validation_threshold:, :]
  return train, validation
  
labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
train_df, validation_df = get_train_validation(labeled_df)
print(train_df.shape)
print(validation_df.shape)