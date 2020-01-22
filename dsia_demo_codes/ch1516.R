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
split_data <- get_train_validation(labeled)
train <- split_data$train
validation <- split_data$validation
logistic_clf <- glm(Survived ~ Age + Fare, data = train, family = "binomial")
thetas <- as.matrix(logistic_clf$coefficients)
X_validation <- as.matrix(validation[, c("Age", "Fare")])
ones <- as.matrix(rep(1, times = nrow(X_validation)))
X_validation <- cbind(ones, X_validation)
y_hat <- X_validation %*% thetas
g_y_hat <- sigmoid(y_hat)
y_pred <- step(g_y_hat)
y_true <- validation$Survived
print("Thetas from glm():")
print(thetas)
print("Before Sigmoid transform:")
print(y_hat[1:5])
print("After Sigmoid transform:")
print(g_y_hat[1:5])
print("After Step transform:")
print(y_pred[1:5])
print("True condition:")
print(y_true[1:5])