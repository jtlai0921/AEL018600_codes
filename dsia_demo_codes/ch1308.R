library(ggplot2)

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
ggplot(labeled_df, aes(x = GrLivArea, y = SalePrice)) +
  geom_point()