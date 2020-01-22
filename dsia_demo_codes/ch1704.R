# Library packages
# install.packages(c("gapminder", "plotly"))
library(gapminder)
library(plotly)

# Bubble chart
bubble_radius <- sqrt(gapminder$pop / pi)
range_gdpPercap <- log10(range(gapminder$gdpPercap) + c(-200, 20000))
range_lifeExp <- range(gapminder$lifeExp) + c(-30, 30)

gapminder %>% 
  plot_ly(x = ~gdpPercap, y = ~lifeExp,
        size = ~pop, type = "scatter", mode = "markers",
        color = ~continent, text = ~country, frame = ~year, hoverinfo = "text",
        sizes = c(min(bubble_radius), max(bubble_radius))) %>%
  layout(xaxis = list(type = "log",
                      range = range_gdpPercap),
         yaxis = list(range = range_lifeExp))