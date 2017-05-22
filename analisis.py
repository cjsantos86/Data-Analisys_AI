import matplotlib.pyplot as plt

x =[1,2,3,4]
y =[5,9,13,17]

x2 =[5,6,7,8]
y2 =[15,16,17,18]

plt.bar(x,y, label="Bars1", color='r')
plt.bar(x2,y2, label="Bars2", color='c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graf\nCheck it out')
plt.legend()
plt.show()

