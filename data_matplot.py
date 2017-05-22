import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

'''with open('infosiga_DATA/INFOMAPA_FEVEREIRO_2017_publicacao_csv.csv','r' ) as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y, label='Loaded from file') '''

x = np.loadtxt('infosiga_DATA/fullData.arff', delimiter=',', unpack=True)

print(x)


#not working

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graf\nCheck it out')
plt.legend()
plt.show()
