getwd()
setwd("C:/Users/erlizhou/Desktop")
library(data.table)
data <- read.csv("ds_test_final.txt", sep = "\t", header = TRUE)
names(data)
summary(data$hicov)
hist(data$hicov)

library(MASS)
library(ISLR)
fit1 <- lm(data$hicov~., data)
summary(fit1)

# dividing the data
training_data <- data[which(data$hicov == 1 | data$hicov == 2),]
test_data <- data[which(is.na(data$hicov) == TRUE),]
summary(training_data$hicov)
summary(test_data$hicov)
nrow(training_data)
272762/5

# convert into categorical variable
is.factor(training_data$hicov)
training_data$hicov <- as.factor(training_data$hicov)
is.factor(training_data$hicov)


mylogit <- glm(I(hicov == 2)~.,data = training_data, family = "binomial")
summary(mylogit)



