library(ggplot2)
library(gridExtra)
library(MASS)

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

labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
split_result <- get_train_validation(labeled_df)
train <- split_result$train
X_vec <- seq(min(train$GarageArea), max(train$GarageArea), length.out = 50)

lambdas <- c(0, 1e2, 1e4, 1e6)
function_plots <- list()
coef_plots <- list()
d <- 10
for (i in 1:length(lambdas)) {
  ridge <- lm.ridge(SalePrice ~ poly(GarageArea, degree = d), lambda = lambdas[i], data = train)
  new_data <- poly(as.matrix(X_vec), degree = d)
  #ones <- as.matrix(rep(1, times = nrow(new_data)))
  y_vec <- cbind(1, new_data) %*% coef(ridge)
  function_df <- data.frame(GarageArea = X_vec, SalePrice = y_vec)
  gg <- ggplot(labeled_df, aes(x = GarageArea, y = SalePrice)) +
    geom_point(size = 0.5) +
    geom_line(data = function_df, aes(x = GarageArea, y = SalePrice), color = "#ff00ff") +
    xlab("") +
    ylab("") +
    theme(axis.ticks.x = element_blank(),
          axis.ticks.y = element_blank())
  function_plots[[i]] <- gg
  coefs <- abs(ridge$coef)
  thetas <- 1:d
  coef_df <- data.frame(thetas = thetas, coefs = coefs)
  gg <- ggplot(coef_df, aes(x = thetas, y = coefs)) +
    geom_line() +
    geom_point() +
    scale_y_continuous(trans = "log") +
    xlab("") +
    ylab("") +
    scale_x_continuous(breaks = 1:10) +
    geom_hline(yintercept = 5000, color = "red", lty = 2) +
    theme(axis.ticks.x = element_blank(),
          axis.ticks.y = element_blank())
  coef_plots[[i]] <- gg
}
grid.arrange(function_plots[[1]], coef_plots[[1]],
             function_plots[[2]], coef_plots[[2]],
             function_plots[[3]], coef_plots[[3]],
             function_plots[[4]], coef_plots[[4]],
             ncol = 2)