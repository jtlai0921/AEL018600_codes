library(ggplot2)
library(reshape2)

df <- read.csv("https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996_per_game.csv")
cor_matrix <- cor(df[, 5:ncol(df)])
melt_cor_matrix <- melt(cor_matrix)
ggplot(data = melt_cor_matrix, aes(x = Var1, y = Var2, fill = value)) + 
  geom_tile() +
  xlab("") +
  ylab("") +
  scale_fill_gradient2(low = "blue", mid = "white", high = "red",
                       midpoint = 0, limits = c(-1, 1), name = "Corr")