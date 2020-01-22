# app.R
# Library packages
# install.packages(c("gapminder", "plotly", "shiny"))
library(gapminder)
library(plotly)
library(shiny)
library(dplyr)

# Globar variables
bubble_radius <- sqrt(gapminder$pop / pi)
unique_continents <- unique(gapminder$continent)
range_gdpPercap <- log10(range(gapminder$gdpPercap) + c(-200, 20000))
range_lifeExp <- range(gapminder$lifeExp) + c(-30, 30)

# Define UI for application
ui <- fluidPage(
   # Application title
   titlePanel("R Gapminder Replica"),
   # Sidebar panel
   sidebarLayout(
     # CheckboxGroup input
     sidebarPanel(
       checkboxGroupInput(
         "continents",
         "Continents:",
         choices = unique_continents,
         selected = unique_continents
       )
     ),
     # Plotly rendering
     mainPanel(
       plotlyOutput("gapminder_bubble")
     )
   )
   
)

# Define server logic
server <- function(input, output) {
  # reactive filtering
  reactive_gapminder <- reactive(
    gapminder %>%
      filter(continent %in% input$continents)
  )
  output$gapminder_bubble <- renderPlotly({
    validate(
      need(input$continents, 'Check at least one continent!')
    )
    reactive_gapminder() %>% 
       plot_ly(x = ~gdpPercap, y = ~lifeExp,
               size = ~pop, type = "scatter", mode = "markers",
               color = ~continent, text = ~country, frame = ~year, hoverinfo = "text",
               sizes = c(min(bubble_radius), max(bubble_radius))) %>%
       layout(xaxis = list(type = "log",
                           range = range_gdpPercap),
              yaxis = list(range = range_lifeExp))
   })
}

# Run the application 
shinyApp(ui = ui, server = server)