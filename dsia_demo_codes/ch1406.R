compute_cost <- function(X, y, thetas) {
  m <- nrow(X)
  y_hat <- X %*% thetas
  J <- (1/(2*m))*sum((y_hat - y)**2)
  return(J)
}

get_thetas_gd <- function(X, y, alpha=0.01, num_iters=1500) {
  m <- nrow(X)
  thetas <- as.matrix(c(0, 0))
  J_history <- vector(length = num_iters)
  for (num_iter in 1:num_iters) {
    y_hat <- X %*% thetas
    loss <- y_hat - y
    gradient <- (t(X) %*% loss)/m
    thetas <- thetas - alpha * gradient
    J_history[num_iter] <- compute_cost(X, y, thetas)
  }
  result <- list(
    thetas = thetas,
    J_history = J_history
  )
  return(result)
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

standard_scaler <- function(x) {
  sd_x <- sd(x)
  mean_x <- mean(x)
  standard_x <- (x - mean_x)/sd_x
  return(standard_x)
}

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
split_result <- get_train_validation(labeled_df)
train <- split_result$train
lm_fit <- lm(SalePrice ~ GrLivArea, data = train)
print("Thetas from lm():")
print(lm_fit$coefficients)
X_train <- train$GrLivArea
y_train <- train$SalePrice
# Standardization
X_train_ss <- as.matrix(standard_scaler(X_train))
ones <- as.matrix(rep(1, times = nrow(X_train_ss)))
X_train_ss <- cbind(ones, X_train_ss)
y_train_ss <- as.matrix(standard_scaler(y_train))
lm_fit <- get_thetas_gd(X_train_ss, y_train_ss, alpha=0.001, num_iters=5000)
print("Thetas from manual gradient descent:")
print(lm_fit$thetas)
# Rescaling
theta_0_pron <- lm_fit$thetas[1, 1]
theta_1_pron <- lm_fit$thetas[2, 1]
mu_y <- mean(y_train)
sigma_y <- sd(y_train)
mu_X <- mean(X_train)
sigma_X <- sd(X_train)
theta_0 <- mu_y + sigma_y*theta_0_pron - sigma_y*mu_X*theta_1_pron/sigma_X
theta_1 <- sigma_y*theta_1_pron/sigma_X
print("Rescaled thetas from manual gradient descent:")
print(theta_0)
print(theta_1)