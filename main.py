import numpy as np
from sklearn import linear_model

# Next, you would need to define your X and y variables.
# X would be your independent variable (e.g. square footage) and y would be your dependent variable (e.g. house price).

X = np.array([[1000], [1200], [1500]])
y = np.array([200000, 300000, 400000])

# Then, you would need to fit your model using sklearn's linear_model.

model = linear_model.LinearRegression()
model.fit(X, y)

# Finally, you would use your model to predict house prices.
result = model.predict([[1000]])
# This would predict that a house with 2000 square feet would cost around 500000.
print(result)