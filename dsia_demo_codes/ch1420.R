get_train_validation <- function(labeled_df, validation_size=0.3) {
  m <- nrow(labeled_df)
  row_indice <- 1:m
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
    reg <- lm(SalePrice ~ poly(YearBuilt, degree = degree), data = train)
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

get_bd_history <- function(labeled_df, num_iters = 100) {
  bd_history <- vector(length = num_iters)
  for (num_iters in 1:num_iters) {
    split_result <- get_train_validation(labeled_df)
    train <- split_result$train
    train$source <- "train"
    validation <- split_result$validation
    validation$source <- "validation"
    results <- get_best_degree(train, validation)
    best_degree <- results$best_degree
    bd_history[num_iters] <- best_degree
  }
  return(sort(table(bd_history), decreasing = TRUE))
}

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
get_bd_history(labeled_df)