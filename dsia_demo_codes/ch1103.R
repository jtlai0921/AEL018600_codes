library(ggplot2)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
plt <- df %>% 
  ggplot(aes(x = Pos)) +
  geom_bar(fill = "red", alpha = 0.5)

plt + theme_bw()
plt + theme_linedraw()
plt + theme_light()
plt + theme_dark()
plt + theme_minimal()
plt + theme_classic()
plt + theme_void()