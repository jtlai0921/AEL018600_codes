labeled_url <- "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df <- read.csv(labeled_url)
is_numeric_col <- unlist(lapply(labeled_df, FUN = is.numeric))
corr_mat <- cor(labeled_df[, is_numeric_col], use = "complete.obs")
sorted_corr_mat <- sort(corr_mat[, "SalePrice"], decreasing = TRUE)
sorted_corr_mat[sorted_corr_mat >= 0.6]