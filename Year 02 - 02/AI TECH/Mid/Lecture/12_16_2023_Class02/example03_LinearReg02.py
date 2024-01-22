import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Data Prep
x = np.arange(0, 10, 0.1)
x_train = x.reshape(-1, 1)

print(x_train.shape)

noise = np.random.randn(x.shape[0])
y_train = 2*x +3 + noise


# Initiate & train model 
model = LinearRegression()
model.fit(x_train, y_train)


# Get value
print('coef:', model.coef_[0])
print('inter:', model.intercept_)

# print('coef: %.2f\n')


# # Draw graph
plt.scatter(x, y_train, s = 20)

predicted_y = model.predict(x_train)
plt.plot(x, predicted_y, color= 'green', linewidth= 2)

plt.show()