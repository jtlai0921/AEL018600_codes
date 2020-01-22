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
tensor
dim(tensor)