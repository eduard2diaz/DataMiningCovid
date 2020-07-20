library(readr)
datos<-read_csv('/home/eduardo/PycharmProjects/DataMiningCovid/Data/data.csv')
covarianza<-cov(datos)
write.csv(covarianza, file="/home/eduardo/PycharmProjects/DataMiningCovid/scripts_R/Preprocessing/covariance.csv")
View(covarianza)
summarize<-eigen(covarianza)
autovalores<- summarize[[1]]   #Arreglo de autovalores
autovectores<- summarize[[2]]   #Arreglo de autovectores
print("Autovalores")
write.csv(autovalores, file="/home/eduardo/PycharmProjects/DataMiningCovid/scripts_R/Preprocessing/autovalores.csv")
View(autovalores)
print("Autovectores")
write.csv(autovectores, file="/home/eduardo/PycharmProjects/DataMiningCovid/scripts_R/Preprocessing/autovectores.csv")
View(autovectores)
