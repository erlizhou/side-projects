setwd("c:/users/erlizhou/Desktop/Career/olympic")
data = read.csv("OlympicAthletes_0.csv", header = TRUE)
head(data)
names(data)
dim(data)
summary(data)
attach(data)
hist(Year, breaks = 20, ylim = c(0,2000), ylab = "Medal winners")
with(data, barplot(rev(sort(table(Sport))[1:5]), ylim = c(0,40), xlab="Sport",ylab="Medal winners",main="5 sports with the least medal winners"))
with(data, barplot((sort(table(Sport), decreasing = TRUE)[1:5]),ylim = c(0,700), xlab="Sport",ylab="Medal winners",main="5 sports with the most medal winners"))
hist(Age, breaks = 18, ylim = c(0,1500),ylab = "Medal winners")
with(data, barplot(rev(sort(table(Country))[1:10]), xlab="Country",ylab="Medal winners",main="10 countries with the least medal winners"))
with(data, barplot(rev(sort(table(Country),decreasing = TRUE)[1:10]), ylim=c(0,1200),xlab="Country",ylab="Medal winners",main="10 countries with the most medal winners"))
newdata <- na.omit(data)
require(ggplot2)
age_by_country <- aggregate(newdata[,2], list(newdata$Country), mean)
age_30 <- age_by_country[age_by_country[,2] >= 30,]
ggplot(age_30, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Countries with highest average age of medal winners")+xlab("Country")+ylab("Age")+ylim(0,40)
age_22 <- age_by_country[age_by_country[,2] <= 22,]
ggplot(age_22, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Countries with lowest average age of medal winners")+xlab("Country")+ylab("Age")+ylim(0,25)
age_by_sport <- aggregate(newdata[,2], list(newdata$Sport), mean)
age_29 <- age_by_sport[age_by_sport[,2] >= 29,]
ggplot(age_29, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Sports with highest average age of medal winners")+xlab("Sport")+ylab("Age")+ylim(0,40)
age_23 <- age_by_sport[age_by_sport[,2] <= 23,]
ggplot(age_23, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Sports with lowest average age of medal winners")+xlab("Sport")+ylab("Age")+ylim(0,25)
age_by_year <- aggregate(newdata[,2], list(newdata$Year), mean)
ggplot(age_by_year, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Average age of medal winners by year")+xlab("Year")+ylab("Age")+ylim(0,30)
medals_by_country <- aggregate(data[,10], list(data$Country), mean)
medal_high <- medals_by_country[medals_by_country[,2] >= 1.3,]
ggplot(medal_high, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Countries with highest average medals per medal winner")+xlab("Country")+ylab("Medals")+ylim(0,4)
goldratio_by_country <- aggregate(data[,7]/data[,10], list(data$Country), mean)
goldratio_high <- goldratio_by_country[goldratio_by_country[,2] == 1,]
ggplot(goldratio_high, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Countries with all medals in gold")+xlab("Country")+ylab("Percent of gold medals")
silverratio_by_country <- aggregate(data[,8]/data[,10], list(data$Country), mean)
silverratio_high <- silverratio_by_country[silverratio_by_country[,2] == 1,]
ggplot(silverratio_high, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Countries with all medals in silver")+xlab("Country")+ylab("Percent of silver medals")
bronzeratio_by_country <- aggregate(data[,9]/data[,10], list(data$Country), mean)
bronzeratio_high <- bronzeratio_by_country[bronzeratio_by_country[,2] == 1,]
ggplot(bronzeratio_high, aes(x = reorder(Group.1, -x), y = x))+geom_bar(stat="identity")+ggtitle("Countries with all medals in bronze")+xlab("Country")+ylab("Percent of bronze medals")
