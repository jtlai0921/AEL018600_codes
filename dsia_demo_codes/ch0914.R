asset_tony_stark <- 12400000000
sprintf("The net worth of Stark Industries is $%s USD.", format(asset_tony_stark, scientific = FALSE))
sprintf("The net worth of Stark Industries is $%s USD.", format(asset_tony_stark, scientific = FALSE, big.mark = ","))
sprintf("The net worth of Stark Industries is $%s USD.", format(asset_tony_stark, scientific = FALSE, big.mark = ",", nsmall = 2))