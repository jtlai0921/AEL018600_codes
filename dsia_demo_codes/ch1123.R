library(ggplot2)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
df$Court <- ifelse(df$Pos %in% c("SG", "PG"), "Back Court", "Front Court")
labs <- c("Center", "Power Forward", "Point Guard", "Small Forward", "Shooting Guard")
df %>% 
  ggplot(aes(x = Pos, fill = Court)) +
  geom_bar(alpha = 0.7) +
  ggtitle("Front court players are the majorities.") +
  labs(subtitle = "Chicago Bulls is relatively weak in the paint.",
       caption = "Source: basketball-reference.com") +
  xlab("Positions") +
  ylab("Number of Players") +
  scale_x_discrete(labels = labs) +
  scale_y_continuous(breaks = 1:4) +
  theme_minimal() +
  theme(legend.position=c(1,1), legend.justification = c(1, 1)) + # 調整圖例的擺放位置
  theme(legend.background=element_blank()) + # 調整圖例背景顏色
  theme(legend.key=element_blank()) # 調整圖例邊框顏色