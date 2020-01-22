library(ggplot2)

labeled <- read.csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled <- labeled[!is.na(labeled$Age), ]
labeled$Survived <- as.character(labeled$Survived)
ggplot(labeled, aes(x = Fare, y = Age, color = Survived)) +
  geom_point() +
  xlab("Fare") +
  ylab("Age") +
  scale_color_hue(labels = c("Dead", "Survived")) +
  theme(legend.title = element_blank())