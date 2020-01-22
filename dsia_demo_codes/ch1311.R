get_thetas_lm <- function(X, y) {
  m <- length(X)
  X <- as.matrix(X)
  y <- as.matrix(y)
  ones <- as.matrix(rep(1, times=m))
  X <- cbind(ones, X)
  LHS <- t(X) %*% X
  RHS <- t(X) %*% y
  return(solve(LHS, RHS))
}

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
X_train <- split_result$train$GrLivArea
y_train <- split_result$train$SalePrice
thetas_lm <- get_thetas_lm(X_train, y_train)
theta_0 <- thetas_lm[1, 1]
theta_1 <- thetas_lm[2, 1]
sprintf("Theta 0: %.4f", theta_0)
sprintf("Theta 1: %.4f", theta_1)