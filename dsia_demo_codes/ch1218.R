library(leaflet)
library(geojsonio)
library(tigris)

pm25_url <- "https://storage.googleapis.com/ds_data_import/2017_avg_pm25.csv"
pm_25 <- read.csv(pm25_url, stringsAsFactors = FALSE)
# 取代臺為台
pm_25$county <- gsub(pattern = "臺", replacement = "台", pm_25$county)
# 取代桃園市為桃園縣
pm_25$county <- gsub(pattern = "桃園市", replacement = "桃園縣", pm_25$county)
sp_data <- geojson_read("~/twgeojson/json/twCounty2010.geo.json", what = "sp")
my_pal <- colorNumeric(palette = "RdYlGn", domain = pm_25$avg_pm25, n = 5, reverse = TRUE)
merged <- geo_join(sp_data, pm_25, "COUNTYNAME", "county")

merged %>% 
  leaflet() %>% 
  addTiles() %>%
  setView(lat = 24, lng = 121, zoom = 7) %>%
  addPolygons(stroke = FALSE, smoothFactor = 0.2, fillOpacity = 0.6,
              fillColor = ~my_pal(avg_pm25)) %>%
  addLegend(position = "bottomright", pal = my_pal, values = ~avg_pm25,
            title = "PM2.5",
            opacity = 0.7)