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

sigmoid <- function(z) {
  return(1/(1 + exp(-z)))
}

step <- function(g_y_hat, threshold = 0.5) {
  return(ifelse(g_y_hat >= threshold, yes = 1, no = 0))
}

labeled <- read.csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled <- labeled[!(is.na(labeled$Age)), ]
#survived <- labeled[labeled$Survived == 1, ]
#dead <- labeled[labeled$Survived == 0, ]
split_data <- get_train_validation(labeled)
train <- split_data$train
logistic_clf <- glm(Survived ~ Fare + Age, data = train, family = "binomial")
thetas <- as.matrix(logistic_clf$coefficients)
# Decision boundary plot
fare_min <- min(labeled$Fare)
fare_max <- max(labeled$Fare)
age_min <- min(labeled$Age)
age_max <- max(labeled$Age)
res <- 200
fare_vec <- seq(fare_min - 5, fare_max + 5, length.out = res)
age_vec <- seq(age_min - 5, age_max + 5, length.out = res)
gd <- expand.grid(fare_vec, age_vec)
X_grid <- as.matrix(gd)
ones <- rep(1, times = nrow(X_grid))
X_grid <- cbind(ones, X_grid)
y_grid <- X_grid %*% thetas
g_y_grid <- sigmoid(y_grid)
y_grid_pred <- step(g_y_grid)
Z <- matrix(y_grid_pred, nrow = res)
contour(fare_vec, age_vec, Z, labels = "", xlab = "", ylab = "", axes=FALSE)
points(labeled$Fare, labeled$Age, col = ifelse(labeled$Survived == 1, rgb(86, 180, 233, maxColorValue = 255), rgb(213, 94, 0, maxColorValue = 255)), pch = ifelse(labeled$Survived == 1, 16, 4), lwd = 2)
points(gd, pch = "." , cex = 1.2, col = alpha(ifelse(Z == 1, "cornflowerblue", "coral"), 0.4))
box()