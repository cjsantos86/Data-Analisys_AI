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
        self.df['Quantidade'] = 1

class Multas():
    def __init__(self):
        pass


class Tempo():
    def __init__(self):
        pass


    
def graphs(dataframe):
    
    dfg = dataframe
    '''
    cidades = dfg.index.values.tolist
    print(cidades)

    '''
    #Find a City
    sampa = dfg.loc['Sao Paulo']

    #group of features in graph
    sampagroup=sampa.groupby(['TipAcidente','FaixaEt']).size()
    sampagroup=sampagroup.unstack()
    plt.figure(3, figsize=(5*1.618, 5))
    sampagroup.plot(kind='bar')
    plt.figure(4, figsize=(5*1.618, 5))
    sampagroup.plot.bar(stacked=True)
    
   
    #New table with number and type of death
    sampaTA = sampa.set_index(['TipAcidente']).groupby(level=0)['Quantidade'].agg({'Sum':np.sum})
    pos = np.arange(len(sampaTA.index.values))
    plt.figure(1, figsize=(5*1.618, 5))
    bars = plt.bar(pos,sampaTA.Sum.values, align='center',linewidth=0, color='lightslategrey')
    bars[0].set_color('#c71919')
    bars[2].set_color('#dbcd19')
    plt.xticks(pos,sampaTA.index.values, alpha=1)
    plt.title(' Número de mortes no trânsito e suas Causas em São Paulo',alpha=1)
    plt.tick_params(top='off', bottom='off',left='off',right='off',labelleft='off',labelbottom='on')

    for spine in plt.gca().spines.values():
        spine.set_visible(False)
     
    for bar in bars:
        plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, str(int(bar.get_height())), 
                 ha='center', color='k', fontsize=11)
   

    #New table with number and rate age of death
    sampaFE = sampa.set_index(['FaixaEt']).groupby(level=0)['Quantidade'].agg({'Sum':np.sum})
    pos2 = np.arange(len(sampaFE.index.values))
    sampaFE.head()
    plt.figure(2, figsize=(5*1.618, 5))
    bars2 = plt.bar(pos2,sampaFE.Sum.values, align='center',linewidth=0, color='lightslategrey')
    bars2[1].set_color('#c71919')
    bars2[2].set_color('#dbcd19')
    plt.xticks(pos2,sampaFE.index.values, alpha=1)
    plt.title(' Número de mortes no trânsito com as respectivas Faixas Etarias em São Paulo',alpha=1)
    plt.tick_params(top='off', bottom='off',left='off',right='off',labelleft='off',labelbottom='on')

    for spine in plt.gca().spines.values():
        spine.set_visible(False)
     
    for bar in bars2:
        plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, str(int(bar.get_height())), 
                 ha='center', color='k', fontsize=11)

    plt.show()
   
if __name__ == '__main__':
    #import seaborn as sns
    #import matplotlib.pyplot as plt

    df = Infomapa().df
    graphs(df)
