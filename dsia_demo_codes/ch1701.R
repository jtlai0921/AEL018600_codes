# Library packages
# install.packages(c("gapminder", "plotly"))
library(gapminder)
library(plotly)

# About gapminder data
gapminder_dim <- dim(gapminder)
gapminder_years <- unique(gapminder$year)
gapminder_n_countries <- length(unique(gapminder$country))
sprintf("這個摘錄版本僅有 %d 個觀測值、%d 個變數，涵括 %d 至 %d 年中每五年、%d 個國家的快照。",
        gapminder_dim[1], gapminder_dim[2], min(gapminder_years), max(gapminder_years), gapminder_n_countries)