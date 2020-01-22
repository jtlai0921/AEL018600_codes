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

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
split_result <- get_train_validation(labeled_df)
train <- split_result$train
validation <- split_result$validation
lm_fit_simple <- lm(SalePrice ~ GrLivArea, data = train)
lm_fit_multiple <- lm(SalePrice ~ GrLivArea + GarageArea, data = train)
y_hat_simple <- predict(lm_fit_simple, newdata = validation)
y_hat_multiple <- predict(lm_fit_multiple, newdata = validation)
mse_simple <- mean((y_hat_simple - validation$SalePrice)**2)
mse_multiple <- mean((y_hat_multiple - validation$SalePrice)**2)
sprintf("MSE of simple linear regression: %.0f", mse_simple)
sprintf("MSE of multiple linear regression: %.0f", mse_multiple)