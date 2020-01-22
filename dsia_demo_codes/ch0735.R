df %>% 
  group_by(year, continent) %>% 
  summarise(ttl_pop = sum(as.numeric(pop))) %>% # integer 會溢位，轉換為 numeric
  tail(10)