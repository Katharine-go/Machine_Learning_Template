# Data Preprocessing Template

# Importing the dataset
dataset = read.csv("Data.csv")

# Taking care of missing data
# 在R中以列为单位进行数据处理dataset$列名称
dataset$Age[is.na(dataset$Age)] = mean(dataset$Age,na.rm = T)
# is.na判断数据是否为null，dataset$Age[is.na...]得到为null的数据位置
# mean表示取平均值,na.rm=T表示将值为na的数据去除，rm=remove
dataset$Salary[is.na(dataset$Salary)] = mean(dataset$Salary,na.rm = T)

# Encoding categorical data
dataset$Country = factor(dataset$Country,levels = c('France','Spain','Germany'),labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,levels = c('No','Yes'),labels = c(0,1))

# Splitting the dataset into the Training set and Test set
install.packages('caTools')
library(caTools)
#勾选caTools或者运行代码library（caTools）
# Console中输入set.seed(123)
# split = sample.split(dataset$Purchased,SplitRatio = 0.8)
# 查看split 
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

# Feature Scaling
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])
#国家和是否购买不是数值，不需要进行特征缩放