shaq <- "Shaquille O'Neal"
strsplit(shaq, split = "\\s+")                  # 以空格分隔
grepl(shaq, pattern = "\\s+")                   # 判斷是否有空格
gsub(shaq, pattern = "\\s+", replacement = ";") # 將空格取代為分號