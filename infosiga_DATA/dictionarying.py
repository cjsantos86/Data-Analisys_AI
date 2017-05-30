import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re


class Infomapa():
    def __init__(self):
        self.name = 'infomapa'
        self.df = None
        self._open_all_infomapa_csv()
        self._clean_columns()
        self.df.to_csv(self.name + '/infomapa.csv')

    def _open_all_infomapa_csv(self):
        """ Open all CSV files from Infomapa data presents on current
        directory since 2001.
        """

        total = []
        year = 2000
        while year < 2020:
            year += 1
            for month in ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL',
                          'MAIO', 'JUNHO', 'JULHO', 'AGOSTO',
                          'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']:
                # directory
                fname = self.name + '/'
                # file name
                fname += '_'.join(['INFOMAPA', month, str(year), 'publicacao', 'csv'])
                fname += '.csv'
                # check if such file exist
                if os.path.isfile(fname):
                    df = pd.read_csv(fname, sep=';', header=1, index_col=0) \
                           .dropna(axis=1, how='all').dropna(axis=0, how='all')
                    df.columns = ['MunAcidente', 'Ano', 'Mes', 'Sexo',
                                  'Periodo', 'TipAcidente', 'Modal', 'FaixaEt',
                                  'Latitude', 'Longitude']
                    total.append(df)

        # concatenates all files in an unique dataframe
        self.df = pd.concat(total, ignore_index=True)

    def _clean_columns(self):
        """ Pass all strings inside self.df in lower case with the first
        character upper, sort database by cities, year and month and
        reset the index.
        """

        # Pass Latitude and Longitude columns to numeric
        self.df['Latitude'] = pd.to_numeric(self.df['Longitude'], errors='coerce')
        self.df['Longitude'] = pd.to_numeric(self.df['Longitude'], errors='coerce')

        # Strip and normalize uppers and lowers for text columns.
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col] = self.df[col].str.strip().str.title()
                self.df[col] = self.df[col].str.replace(r'N.o Dispon.vel', 'ND')
                self.df[col] = self.df[col].str.replace(r'N.o Especificado', 'NE')
                self.df[col] = self.df[col].str.normalize('NFKD') \
                                   .str.encode('ascii', errors='ignore') \
                                   .str.decode('utf-8')

        # Set MunAcidente as index
        self.df = self.df.set_index(['MunAcidente']).sort_index()


class Multas():
    def __init__(self):
        pass


class Tempo():
    def __init__(self):
        pass


if __name__ == '__main__':
    #import seaborn as sns
    #import matplotlib.pyplot as plt

    df = Infomapa().df

    #sampa = df.loc['Sao Paulo']

    #print(sampa.head())

    #nd_pattern = re.compile(r'N.o Dispon.vel')

    #s = 'Não Disponível'

    #if nd_pattern.match(s):
    #    print('match')
    #else:
    #    print('not')

    for i in range(len(df.columns)):
        for row in sorted(set(df[df.columns[i]])):
            print(row)
        print('\n')

   



    
'''
#Indexing table
df = df.set_index(['MunAcidente','Ano'])
df.head()


#Find a City
sampa = df.loc['Sao Paulo']


#New table with number of death
sampa = sampa.set_index(['TipAcidente'])
sampa.head()
sampa = sampa.groupby(level=0)['Quantidade'].agg({'Sum':np.sum})

#how to get the values (index and columns)
#print(sampa.index.values, sampa.Sum.values)

pos = np.arange(len(sampa.index.values))

bars = plt.bar(pos,sampa.Sum.values, align='center',linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')
plt.xticks(pos,sampa.index.values, alpha=0.8)
plt.title('Meu Primeiro Graficuzinho')
plt.tick_params(top='off', bottom='off',left='off',right='off',labelleft='off',labelbottom='on')

for spine in plt.gca().spines.values():
    spine.set_visible(False)
    
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)
cols = ['m','g','r','b']
plt.pie(sampa.Sum.values, labels=sampa.Sum, colors=cols, startangle=90,shadow=True,autopct='%1.1f%%')

plt.show()
'''
