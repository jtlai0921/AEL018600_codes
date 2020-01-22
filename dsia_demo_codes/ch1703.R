# app.R
# Library packages
# install.packages(c("gapminder", "plotly", "shiny"))
library(gapminder)
library(plotly)
library(shiny)

# Globar variables
bubble_radius <- sqrt(gapminder$pop / pi)

# Define UI for application
ui <- fluidPage(
   # Application title
   titlePanel("R Gapminder Replica"),
   # Plotly rendering
   mainPanel(
        plotlyOutput("gapminder")
   )
)

# Define server logic
server <- function(input, output) {
   output$gapminder <- renderPlotly({
     gapminder %>% 
       plot_ly(x = ~gdpPercap, y = ~lifeExp,
               size = ~pop, type = "scatter", mode = "markers",
               color = ~continent, text = ~country, hoverinfo = "text",
               sizes = c(min(bubble_radius), max(bubble_radius))) %>%
       layout(xaxis = list(type = "log"))
   })
}

# Run the application 
shinyApp(ui = ui, server = server)