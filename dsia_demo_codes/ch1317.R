library(ggplot2)

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
train_df <- split_result$train
train_df$Split <- "Train"
validation_df <- split_result$validation
validation_df$Split <- "Validation"
df_for_scatter <- rbind(train_df, validation_df)
regressor <- lm(SalePrice ~ GrLivArea, data = train_df)
theta_0 <- regressor$coefficients[1]
theta_1 <- regressor$coefficients[2]
X_min <- min(labeled_df$GrLivArea)
X_max <- max(labeled_df$GrLivArea)
X_arr <- seq(from = X_min, to = X_max, length.out = 50)
y_hats <- theta_0 + theta_1 * X_arr
df_for_line <- data.frame(X_arr, y_hats)

ggplot(df_for_scatter, aes(x = GrLivArea, y = SalePrice, color = Split)) +
  geom_point(size = 0.7) +
  geom_line(data = df_for_line, aes(x = X_arr, y = y_hats), color = "#009E73", size = 1.2) +
  xlab("Ground Living Area") +
  ylab("Sale Price")