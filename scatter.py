import matplotlib.pyplot as plt

x =[1,2,3,4]
y =[5,9,13,17]

plt.scatter(x,y, label='skitscat',color='g')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graf\nCheck it out')
plt.legend()
plt.show()

