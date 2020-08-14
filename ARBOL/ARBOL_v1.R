library(RWeka)

dataTrain <- read.csv("training_covid.csv")
dataTest <- read.csv("test_covid.csv")

resultJ48 <- J48(as.factor(class)~., dataTrain) 

dataTest.pred <- predict(resultJ48, newdata = dataTest)
table(dataTest$class, dataTest.pred)
plot(resultJ48)

dataTest.pred