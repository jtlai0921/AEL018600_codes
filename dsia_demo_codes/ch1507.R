library(ggplot2)
library(gridExtra)

log_function_1 <- function(x) {
  return(-log(x))
}

log_function_0 <- function(x) {
  return(-log(1 - x))
}

x_vec <- seq(0, 1, length.out = 50)
gg1 <- ggplot(data.frame(x = x_vec), aes(x = x)) +
  stat_function(fun = log_function_1, geom = "line")
gg2 <- ggplot(data.frame(x = x_vec), aes(x = x)) +
  stat_function(fun = log_function_0, geom = "line")
grid.arrange(gg1, gg2, nrow = 1, ncol = 2)