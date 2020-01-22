library(jsonlite)
library(plotly)
library(magrittr)

get_ohlc <- function(twse_ticker) {
  today <- as.character(Sys.Date())
  today <- gsub(pattern = "-", replacement = "", today)
  twse_url <- sprintf("http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo=%s",today, twse_ticker)
  stock <- fromJSON(twse_url)
  data <- stock$data
  trading_dates <- data[, 1]
  trading_dates <- strsplit(trading_dates, split = "/")
  trading_dates_yr <- c()
  trading_dates_month <- c()
  trading_dates_day <- c()
  for (i in 1:length(trading_dates)) {
    trading_dates_yr <- c(trading_dates_yr, as.numeric(trading_dates[[i]][1]) + 1911)
    trading_dates_month <- c(trading_dates_month, trading_dates[[i]][2])
    trading_dates_day <- c(trading_dates_day, trading_dates[[i]][3])
  }
  trading_dates <- paste(trading_dates_yr, trading_dates_month, trading_dates_day,
                         sep = "-")
  trading_dates <- as.Date(trading_dates)
  opens <- as.numeric(data[, 4])
  highs <- as.numeric(data[, 5])
  lows <- as.numeric(data[, 6])
  closes <- as.numeric(data[, 7])
  ohlc <- data.frame(trading_date = trading_dates,
                     open = opens,
                     high = highs,
                     low = lows,
                     close = closes,
                     stringsAsFactors = FALSE)
  return(ohlc)
}

tsmc <- get_ohlc("2330")
p <- tsmc %>%
  plot_ly(x = ~trading_date,
          type="candlestick",
          open = ~open,
          close = ~close,
          high = ~high,
          low = ~low) %>%
  layout(xaxis = list(rangeslider = list(visible = FALSE)))
p