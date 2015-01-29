library(ggplot2)
library(dplyr)
library(reshape2)

for (i in 1:10) {
    filename <- paste("data/scores", i-1, ".csv", sep="")
    s <- read.csv(filename, stringsAsFactors=FALSE)
    s.2 <- s %>% 
        select(-X) %>% 
            mutate(time = as.POSIXct(substr(time, 1, 19),
                format="%Y-%m-%d %H:%M:%S"))
    s.df <- melt(s.2, id='time')
    ggplot(s.df, aes(x=time, y=value)) + 
        geom_line(aes(colour=variable, linetype=variable))
    ggsave(file=paste("post", i, ".png", sep=""),
        width=10, height=6)
}
