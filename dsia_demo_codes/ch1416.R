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
train <- split_result$train
train$source <- "train"
validation <- split_result$validation
validation$source <- "validation"
reg_d1 <- lm(SalePrice ~ YearBuilt, data = train)
reg_d2 <- lm(SalePrice ~ YearBuilt + I(YearBuilt**2), data = train)
y_hat <- predict(reg_d1, newdata = validation)
mse_d1 <- mean((y_hat - validation$SalePrice)**2)
y_hat <- predict(reg_d2, newdata = validation)
mse_d2 <- mean((y_hat - validation$SalePrice)**2)
sprintf("MSE with degree=1: %.0f", mse_d1)
sprintf("MSE with degree=2: %.0f", mse_d2)
x_arr <- seq(from = min(labeled_df$YearBuilt), to = max(labeled_df$YearBuilt), length.out = 50)
new_data <- data.frame(YearBuilt = x_arr)
y_arr_d1 <- predict(reg_d1, newdata = new_data)
y_arr_d2 <- predict(reg_d2, newdata = new_data)
new_data$SalePrice_d1 <- y_arr_d1
new_data$SalePrice_d2 <- y_arr_d2
df_to_plot <- rbind(train, validation)
df_to_plot %>% 
  ggplot(aes(x = YearBuilt, y = SalePrice, color = source)) +
  geom_point(size=0.5) +
  geom_line(data = new_data, aes(x = YearBuilt, y = SalePrice_d1), color = "#ff00ff", size = 1.4) +
  geom_line(data = new_data, aes(x = YearBuilt, y = SalePrice_d2), color = "#006600", size = 1.4)