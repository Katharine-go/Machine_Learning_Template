# Mutiple Linear Regression

# Importing the dataset
dataset = read.csv("50_Startups.csv")

dataset$State = factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit,SplitRatio = 0.8)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

# Fitting Muilting Linear Regression to the Training set
regressor = lm(formula = Profit ~ R.D.Spend, data= training_set)
# 因变量 ～ 自变量1 + 自变量2 + ... / ~ .(表示用所有的自变量预测因变量)

# Predict the Test set results
y_pred = predict(regressor,newdata = test_set)

# Building the optimal model using Backward Elimination
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data= training_set)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend , data= training_set)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend , data= training_set)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend , data= training_set)
summary(regressor)

# Predict the Test set results
y_pred = predict(regressor,newdata = test_set)
