library(caret)

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
train_index <- createDataPartition(labeled_df$Id, p = 0.7, 
                                  list = FALSE, 
                                  times = 1)
train <- labeled_df[train_index, ]
validation <- labeled_df[-train_index, ]
dim(train)
dim(validation)