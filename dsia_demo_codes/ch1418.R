library(tidyr)
library(ggplot2)

get_train_validation <- function(labeled_df, validation_size=0.3, random_state=123) {
  m <- nrow(labeled_df)
  row_indice <- 1:m
  set.seed(random_state)
  shuffled_row_indice <- sample(row_indice)
  labeled_df <- labeled_df[shuffled_row_indice, ]
  validation_threshold <- as.integer(validation_size * m)
  validation <- labeled_df[1:validation_threshold, ]
  train <- labeled_df[(validation_threshold+1):m, ]
  return(list(
    validation = validation,
    train = train
  ))
}

get_best_degree <- function(train, validation, d = 10) {
  degrees <- seq(1, d)
  mse_train_vec <- vector(length = d)
  mse_validation_vec <- vector(length = d)
  for (degree in degrees) {
    reg <- lm(SalePrice ~ poly(YearBuilt, degree = degree, raw = TRUE), data = train)
    y_hat <- predict(reg, newdata = train)
    mse_train <- mean((y_hat - train$SalePrice)**2)
    y_hat <- predict(reg, newdata = validation)
    mse_validation <- mean((y_hat - validation$SalePrice)**2)
    mse_train_vec[degree] = mse_train
    mse_validation_vec[degree] = mse_validation
  }
  best_degree <- which.min(mse_validation_vec)
  return(list(
    mse_train_vec = mse_train_vec,
    mse_validation_vec = mse_validation_vec,
    best_degree = best_degree
  ))
}

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
split_result <- get_train_validation(labeled_df)
train <- split_result$train
train$source <- "train"
validation <- split_result$validation
validation$source <- "validation"
results <- get_best_degree(train, validation)
mse_train_vec <- results$mse_train_vec
mse_validation_vec <- results$mse_validation_vec
best_degree <- results$best_degree
sprintf("Best degree: %s", best_degree)
d <- 10
degrees <- seq(1, d)
df_to_plot <- data.frame(
  degree = degrees,
  mse_train = mse_train_vec,
  mse_validation = mse_validation_vec
)
df_to_plot_long <- gather(df_to_plot, key = "source", value = "mse", mse_train, mse_validation)

ggplot(df_to_plot_long, aes(x = degree, y = mse, color = source)) +
  geom_line() +
  geom_point() +
  geom_vline(aes(xintercept = best_degree), color="#007f00") +
  scale_x_continuous(breaks = degrees) +
  xlab("Degree") +
  ylab("MSE")