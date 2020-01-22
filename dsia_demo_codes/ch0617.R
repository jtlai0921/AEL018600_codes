arr <- c(11, 12, 13, 14, 15)
for (idx in 1:length(arr)) {
  print(sprintf("位於索引值 %i 的數字是 %i", idx, arr[idx]))
}