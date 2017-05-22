import matplotlib.pyplot as plt


population_ages = [18,64,17,54,63,65,50,39,29,58,93,48,84,43,42,38,12,46,35,99]

#ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graf\nCheck it out')
plt.legend()
plt.show()

