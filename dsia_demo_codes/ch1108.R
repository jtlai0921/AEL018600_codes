library(ggplot2)

csv_url <- "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df <- read.csv(csv_url)
# 無法顯示中文
df %>% 
  ggplot(aes(x = Pos)) +
  geom_bar(fill = "red", alpha = 0.5) +
  ggtitle("前場球員為芝加哥公牛隊的大宗") +
  labs(subtitle = "反映當時為了抗衡其他具有主宰力中前鋒的隊伍之現象",
       caption = "資料來源: basketball-reference.com") +
  xlab("鋒衛位置") +
  ylab("球員人數") +
  scale_x_discrete(labels = c("中鋒", "大前鋒", "小前鋒", "控球後衛", "得分後衛"))