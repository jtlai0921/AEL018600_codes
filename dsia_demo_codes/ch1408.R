get_mse <- function(X_vec, y_vec, thetas) {
  m <- length(X_vec)
  theta_0 <- thetas[1, 1]
  theta_1 <- thetas[2, 1]
  y_hat <- theta_0 + theta_1*X_vec
  err <- y_hat - y_vec
  se <- sum(err**2)
  return(se/m)
}

get_mse_vectorized <- function(X, y, thetas) {
  m <- nrow(X)
  y_hat <- X %*% thetas
  err <- y_hat - y
  se <- t(err) %*% err
  return(se[1, 1]/m)
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
train <- split_result$train
validation <- split_result$validation
X_validation <- as.matrix(validation$GrLivArea)
ones <- as.matrix(rep(1, times = nrow(X_validation)))
X_validation <- cbind(ones, X_validation)
y_validation <- as.matrix(validation$SalePrice)
lm_fit <- lm(SalePrice ~ GrLivArea, data = train)
theta_0 <- lm_fit$coefficients[1]
theta_1 <- lm_fit$coefficients[2]
thetas <- as.matrix(c(theta_0, theta_1))
mse <- get_mse(validation$GrLivArea, validation$SalePrice, thetas)
mse_vectorized <- get_mse_vectorized(X_validation, y_validation, thetas)
sprintf("MSE: %.0f", mse)
sprintf("MSE(vectorized): %.0f", mse_vectorized)