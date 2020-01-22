# Library packages
# install.packages(c("gapminder", "plotly"))
library(gapminder)
library(plotly)

# Bubble chart
bubble_radius <- sqrt(gapminder$pop / pi)
gapminder %>% 
  plot_ly(x = ~gdpPercap, y = ~lifeExp,
        size = ~pop, type = "scatter", mode = "markers",
        color = ~continent, text = ~country, hoverinfo = "text",
        sizes = c(min(bubble_radius), max(bubble_radius))) %>%
  layout(xaxis = list(type = "log"))