import matplotlib.pyplot as plt

x=list(range(0,11))
y=[i**2 for i in x]
z=[i**3 for i in y]
    

plt.ylabel("Square and Cube")
plt.xlabel("Number")

plt.plot(x,y,'g^',x,z,'rs')
#   plt.plot(x,y,'r--')
#   plt.plot(x,y,'g^')
plt.show()