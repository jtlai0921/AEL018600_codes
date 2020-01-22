library(caret)
library(tidyr)
library(ggplot2)

get_best_degree <- function(labeled_df, d = 10, k = 5) {
  degrees <- seq(1, d)
  mse_train_avg_vec <- vector(length = d)
  mse_validation_avg_vec <- vector(length = d)
  for (degree in degrees) {
    validation_indice <- createFolds(labeled_df$SalePrice, k = k)
    validation_indice_len <- length(validation_indice)
    mse_train_vec <- vector(length = validation_indice_len)
    mse_validation_vec <- vector(length = validation_indice_len)
    for (i in 1:validation_indice_len) {
      train <- labeled_df[-validation_indice[[i]], ]
      validation <- labeled_df[validation_indice[[i]], ]
      reg <- lm(SalePrice ~ poly(YearBuilt, degree = degree), data = train)
      y_hat <- predict(reg, newdata = train)
      mse_train <- mean((y_hat - train$SalePrice)**2)
      y_hat <- predict(reg, newdata = validation)
      mse_validation <- mean((y_hat - validation$SalePrice)**2)
      mse_train_vec[i] <- mse_train
      mse_validation_vec[i] <- mse_validation
    }
    mse_train_avg_vec[degree] <- mean(mse_train_vec)
    mse_validation_avg_vec[degree] <- mean(mse_validation_vec)
  }
  best_degree <- which.min(mse_validation_avg_vec)
  return(list(
    mse_train_avg_vec = mse_train_avg_vec,
    mse_validation_avg_vec = mse_validation_avg_vec,
    best_degree = best_degree
  ))
}

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
X_labeled <- labeled_df$YearBuilt
y_labeled <- labeled_df$SalePrice
results <- get_best_degree(labeled_df)
mse_train_vec <- results$mse_train_avg_vec
mse_validation_vec <- results$mse_validation_avg_vec
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