import matplotlib.pyplot as plt 

x_values = list(range(0,10))
y_values = list(x**2 for x in x_values)

plt.scatter(x_values,y_values)
plt.show()