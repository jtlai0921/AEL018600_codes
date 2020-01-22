library(plotly)

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

compute_cost <- function(X, y, thetas) {
  m <- nrow(X)
  h <- X %*% thetas
  J <- sum((h - y)**2) / (2*m)
  return(J)
}

standardize <- function(X, y) {
  X_sd <- sd(X)
  mean_sd <- mean(X)
  y_sd <- sd(y)
  mean_y <- mean(y)
  X_scaled <- (X - mean_sd)/X_sd
  y_scaled <- (y - mean_y)/y_sd
  return(list(
    X_scaled = X_scaled,
    y_scaled = y_scaled
  ))
}

get_thetas_lm <- function(X, y, alpha=0.001, num_iters=10000) {
  thetas <- as.matrix(c(0, 0))
  m <- length(X)
  X <- as.matrix(X)
  y <- as.matrix(y)
  ones <- as.matrix(rep(1, times = m))
  X <- cbind(ones, X)
  J_history <- vector(length = num_iters)
  for (num_iter in 1:num_iters) {
    h <- X %*% thetas
    loss <- h - y
    gradient <- t(X) %*% loss
    thetas <- thetas - (alpha * gradient)/m
    J_history[num_iter] <- compute_cost(X, y, thetas = thetas)
  }
  return(list(
    thetas = thetas,
    J_history = J_history
  ))
}

get_rescaled_thetas <- function(thetas, X_train, y_train) {
  theta_0 <- thetas[1, 1]
  theta_1 <- thetas[2, 1]
  X_train_mean <- mean(X_train)
  y_train_mean <- mean(y_train)
  X_train_sd <- sd(X_train)
  y_train_sd <- sd(y_train)
  theta_1_rescaled <- theta_1 / X_train_sd * y_train_sd
  theta_0_rescaled <- y_train_mean + y_train_sd * theta_0 - y_train_sd/X_train_sd * theta_1 * X_train_mean
  return(list(
    theta_0_rescaled = theta_0_rescaled,
    theta_1_rescaled = theta_1_rescaled
  ))
}

surface_plot <- function(theta0_range, theta1_range, X, y) {
  theta0_start <- theta0_range[1]
  theta0_end <- theta0_range[2]
  theta1_start <- theta1_range[1]
  theta1_end <- theta1_range[2]
  length_out <- 50
  theta0_arr <- seq(theta0_start, theta0_end, length.out = length_out)
  theta1_arr <- seq(theta1_start, theta1_end, length.out = length_out)
  Z <- matrix(nrow = length_out, ncol = length_out)
  for (i in 1:length_out) {
    for (j in 1:length_out) {
      theta_0 <- theta0_arr[i]
      theta_1 <- theta1_arr[j]
      thetas_mat <- as.matrix(c(theta_0, theta_1))
      Z[i, j] <- compute_cost(X, y, thetas = thetas_mat)
    }
  }
  list_for_surface <- list(
    x = theta0_arr,
    y = theta1_arr,
    z = Z
  )
  plot_ly(x = list_for_surface$x, y = list_for_surface$y, z = list_for_surface$z, colorscale = "Jet") %>%
    add_surface() %>% 
    layout(
      title = "Cost function during gradient descent",
      scene = list(
        xaxis = list(title = "theta_0"),
        yaxis = list(title = "theta_1"),
        zaxis = list(title = "J")
      )
    )
}

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
split_result <- get_train_validation(labeled_df)
X_train <- split_result$train$GrLivArea
y_train <- split_result$train$SalePrice
# Normalization
standard_scaler <- standardize(X_train, y_train)
X_train_scaled <- standard_scaler$X_scaled
y_train_scaled <- standard_scaler$y_scaled
thetas_lm <- get_thetas_lm(X_train_scaled, y_train_scaled)
thetas <- thetas_lm$thetas
J_history <- thetas_lm$J_history
# Rescaling
thetas_rescaled <- get_rescaled_thetas(thetas, X_train, y_train)
theta_0 <- thetas_rescaled$theta_0_rescaled
theta_1 <- thetas_rescaled$theta_1_rescaled
sprintf("Theta 0: %.4f", theta_0)
sprintf("Theta 1: %.4f", theta_1)
m <- length(X_train)
X_train_reshaped <- as.matrix(X_train)
y_train_reshaped <- as.matrix(y_train)
ones <- as.matrix(rep(1, times = m))
X_train_reshaped <- cbind(ones, X_train_reshaped)
surface_plot(c(10000, 30000), c(0, 200), X_train_reshaped, y_train_reshaped)