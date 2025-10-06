from matpltlib import pyplot as pit
import numpy as np

# yeesh He went straight in on this one
# So here im visualizing creating Line plots and Bar plots
# Seems like matpltlib is not yet installed  along with numpy

#Customising line plort
x=np.arange(1,10,0.1)
y=2*x+5

plt.plot(x,y,color='r')
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

x=np.arange(1,10,0.1)
y1=2*x+5
y2=3*x+10

plt.subplot(1,2,1)
plt.plot(x,y1)

plt.subplot(1,2,2)
plt.plot(x,y2)

#Bar- plot

fruit={'apple':30,'mango':45, 'banana':10}
names=list(fruit.keys())
quantity=list(fruit.values())

names,quantity
(['apple', 'mango', 'banana'], [30, 45, 10])

plt.bar(names,quantity)
plt.show()

# Customizing bar plot
# oooh you can put .barh to put ehm horizontaly
plt.bar(names,quantity, color='orange')
plt.title('Distribution of fruits')
plt.xlable('Fruits')
plt.ylabel('quantity')
plt.show()


# Scatter plot
x=[12,20,30,40,50,60,70,80,90]
a=[1,2,3,4,5,6,7,8,9] 
b=[5,6,7,8,3,2,1,4,9]

# s represents the size of the point and marker changes the shape
# Figure changes the size of th whole figure
plt.figure(figsize=(10,10))
plt.scatter(x,a,s=200)
plt.scatter(x,b,s=500,marker='2')
plt.legend(['a','b'])
plt.title('X vs a&b')
plt.xlabel('x')
plt.ylabel('a&b')
plt.show()

# Histogram
data=[1,1,1,4,5,6,3,0,2,7,3,9,1,7,8,5,4,3,2,2]

plt.hist(data)
plt.show()

import pandas as pd

pd.read_csv('iris.csv')
iris.head()

# Bins increases the numba of distribution in the histogram
plt.hist(iris['Sepal.length'], color='red', bins=50)
plt.show()

# Box plot

one = [1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,6,7,8,7,6]
three=[6,7,8,8,5,3,2,1,6]

data=list([one,two,three])

plt.boxplot(data)
plt.show

# Violin Plot

one = [1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,6,7,8,7,6]
three=[6,7,8,8,5,3,2,1,6]

data=list([one,two,three])

# Added Meadians and means
plt.violinplot(data, showmedians=True, showmeans=True)
plt.grid(True)
plt.title("Distribution of data")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show


# Pie chart 

fruit=['apple', 'mango', 'orange', 'grapes']
quantity=[30,45,65,100]
# Aded from shadow to percentage and also the 0.0 - separates
plt.pie(quantity, labels=fruit,autoct= '%0.1f%%', shadow=True, explode=(0.0.1,0,1))
plt.show()

# Donut
# Its the same as a pic just the Donut shape with radius dff's
fruit=['apple', 'mango', 'orange', 'grapes']
quantity=[30,45,65,100]

pie1=plt.pie(quantity, labels=fruit,autoct= '%0.1f%%',radius=2)
pie2=plt.pie([5],colors='w',radius=1)


plt.show()

# Area plot

x=[10,20,30,40,50,60,70,80,90]
y=[1,2,3,4,6,7,8,5,4]

plt.stackplot(x,y)
plt.show()

# Dff btwn a bar plot and a Historgram - Historgram is used for numerical values and a Bar plot used for categorical values 