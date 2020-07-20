library(readr)
datos<-read_csv('/home/eduardo/PycharmProjects/DataMiningCovid/Data/data.csv')
correlacion<-cor(datos)
write.csv(correlacion, file="/home/eduardo/PycharmProjects/DataMiningCovid/scripts_R/Preprocessing/correlacion.csv")
View(correlacion)



