library(scatterplot3d)

prim = read.csv("./tests/prim.csv", header = TRUE, sep = ";")
kruskal = read.csv("./tests/kruskal.csv", header = TRUE, sep = ";")
kruskalSorted = read.csv("./tests/kruskalSorted.csv", header = TRUE, sep = ";")

plot3d <- function(data){
  return(scatterplot3d(
    x = data$n, y = data$m, z = log(data$time),
    xlab = "Vértices", ylab = "Arestas", zlab = "Tempo (log)",
    main=paste("Tempo por tamanho do problema (", data$algorithm[1], ")"), type = "h",
    pch = 16,# color="steelblue",
    #highlight.3d = TRUE,
    #xlim = c(0,250),
    ylim = c(0,3000)
    #zlim = c(0,3000)
  ))
}

plotNodes <- function(data){
  plot(
    data$n, data$time,
    xlab = "vértices", ylab = "tempo (ms)",
    main=paste("Tempo por número de vértices (", data$algorithm[1], ")")
  )
  fit <- lm(log(data$time) ~ log(data$n*data$m))
  abline(fit)
}

plotEdges <- function(data){
  plot(
      data$m, data$time,
      xlab = "arestas", ylab = "tempo (ms)",
      main=paste("Tempo por número de arestas (", data$algorithm[1], ")")
  )
  fit <- lm(log(data$time) ~ log(data$n*data$m))
  abline(fit)
}

regression <- function(data){
  return(
    lm(log(data$time)~log(data$n))
  )
}

data <- prim

plt <- plot3d(prim)
plotNodes(prim)
plotEdges(prim)
regression(prim)

regression = lm(log(data$time)~log(data$m))
abline(regression)
plt$points3d(x=c(0,200,-1,-1), y=c(1,1,-1,-1,1),z=rep(5,5), type="l", col="blue", lwd=2)

fit <- lm(data$time ~ data$n + data$m)
summary(fit)
anova(fit)
layout(matrix(c(1,2,3,4),2,2))
plot(fit)
abline(fit)


plot3d(kruskal)
plotNodes(kruskal)
plotEdges(kruskal)

plot3d(kruskalSorted)
plotNodes(kruskalSorted)
plotEdges(kruskalSorted)

####
exp(log(data$time)~log(data$n)+log(data$m))

data <- prim
hexp = lm(log(data$time)~data$n)
lines(data$n, exp(hexp$coefficients[1]) * exp(hexp$coefficients[2] * data$n))

abline(regression(prim))

####

time <- data$time
size <- data$n * data$m
  
hexp <- lm(log(time)~size) #3 # exp(5.68e-15)*exp(1.099*data$n)
hpol <- lm(log(time)~log(size)) #exp(-2.842e-15)*data$n^2

plot (size, time)
lines (size, exp(hpol$coefficients[1]) * size ^ hpol$coefficients[2])
lines (size, exp(hexp$coefficients[1]) * exp( hexp $ coefficients[2] * size))

summary(hexp)
summary(rpol)

####
mod2 <- loess(data$time~data$n+data$m)
grd <- data.frame(data$n, data$m)
grd$pred <- predict(mod2, newdata=grd)
grd <- grd[order(grd$data.n, grd$data.m),]
x1 <- unique(grd$data.n)
x2 <- unique(grd$data.m)   # shouldn't have used y
surface3d(x1, x2, z=matrix(grd$pred,length(x1),length(x2)) )




