vec <- matrix(c(11, 12, 13, 14, 15))
mat <- matrix(11:20, nrow = 2, byrow = TRUE)
to_fill <- 11:34
tensor <- array(NA, c(3, 4, 2))
for (i in 1:2) {
  for (j in 1:3) {
    for (k in 1:4) {
      tensor[j, k, i] <- to_fill[1]
      to_fill <- to_fill[-1]
    }
  }
}
vec[5, 1]       # 15 位於 (5, 1)
mat[1, 5]       # 15 位於 (1, 5)
tensor[2, 1, 1] # 15 位於 (2, 1, 1)