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

digits <- read.csv("https://storage.googleapis.com/kaggle_datasets/Digit-Recognizer/train.csv")
unique_digits <- unique(digits$label)
unique_digits <- sort(unique_digits)
split_data <- get_train_validation(digits)
train <- split_data$train
validation <- split_data$validation
# One vs. all
all_probs <- matrix(0, nrow(validation), length(unique_digits))
for (unique_digit in unique_digits) {
  train$label_encoded <- ifelse(train$label == unique_digit, 1, 0)
  logistic_clf <- glm(label_encoded ~ .-label, data = train, family = "binomial")
  y_prob <- matrix(predict(logistic_clf, newdata = validation, type = "response"))
  all_probs[, unique_digit + 1] <- y_prob
}
head(max.col(all_probs), n = 10)