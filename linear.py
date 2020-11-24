import pandas as pd
from sklearn import linear_model
training_dataset = pd.read_csv("home_data.csv")
regression_model = linear_model.LinearRegression()
regression_model.fit(training_dataset[['grade']], training_dataset.price) 
print ("Model trained.")
input_area = int(input("Enter grade: "))
price = regression_model.predict([[input_area]])
print ("gia tien: ", round(price[0], 2))