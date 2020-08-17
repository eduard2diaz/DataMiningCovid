datos <- read.csv("solo_defunciones.csv")

data <- as.data.frame(scale(datos))

#data$Country = protein$Country
#rownames(data) = data$Country

hc <- hclust(dist(data, method = "euclidean"), method = "ward")
hc

plot(hc, hang = -0.01, cex = 0.6)

hc$call

clust <- cutree(hc, k = 6)

clust

rect.hclust(hc, k = 6, border = 2:10)



resultante <- datos
resultante$cluster = clust
write.csv(resultante, file = "cluster.csv", row.names = FALSE)
