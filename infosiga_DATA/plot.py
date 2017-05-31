import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Infomapa():
    header = {'mnac' : 'Município Acidente',
              'ano'  : 'Ano',
              'mes'  : 'Mês',
              'sexo' : 'Sexo',
              'trnac': 'Turno Acidente',
              'tpac' : 'Tipo de Acidente',
              'mlv'  : 'Meio de Locomoção da Vítima',
              'fxet' : 'Faixa Etária',
              'lat'  : 'Latitude Acidente',
              'lon'  : 'Longitude Acidente',
             }

    def __init__(self):
        self.df = None
        self._open_all_infomapa_csv()
        self._normalize_strings()
        self.df.to_csv('infomapa.csv')


    def _open_all_infomapa_csv(self):
        """ Open all CSV files from Infomapa data presents on current
        directory since 2001.
        """

        total = []
        year = 2000
        while year < 2020:
            year += 1
            for month in range(1,13):
                fname = '-'.join(['infomapa', str(year), str(month).zfill(2)])
                fname += '.csv'
                if os.path.isfile(fname):
                    total.append(pd.read_csv(fname, sep=';', header=0))

        self.df = pd.concat(total, ignore_index=True)


    def _normalize_strings(self):
        """ Pass all strings inside self.df in lower case with the first
        character upper, sort database by cities, year and month and
        reset the index.
        """

        for key in ['mnac', 'sexo', 'trnac', 'tpac', 'mlv','fxet']:
            _key = Infomapa.header[key]
            self.df[_key] = self.df[_key].str.title()

        self.df = self.df.sort_values(by=[Infomapa.header['mnac'],
                                          Infomapa.header['ano'],
                                          Infomapa.header['mes'],
                                          Infomapa.header['fxet'],])
        self.df = self.df.reset_index(drop=True)

df = Infomapa().df



#Subplot working
'''
fig = plt.figure()
fig.add_subplot(2,1,2)
sns.kdeplot(df[Infomapa.header['ano']])

fig.add_subplot(2,1,1)
sns.kdeplot(df[Infomapa.header['mes']], df[Infomapa.header['ano']])
'''

#Analysis test
df2 = df[df[Infomapa.header['mnac']] == 'Sao Paulo']

df.head()
plt.figure(1, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
sns.countplot(y='Faixa Etária', hue='Tipo de Acidente', data=df2, palette="Greens_d")
df.sort_values([Infomapa.header['fxet'],Infomapa.header['mlv']],ascending=[True, False], inplace=True)
#Analysis test2
'''

plt.figure(1, figsize=(5*1.618, 5))
sns.kdeplot(df[Infomapa.header['ano']])

plt.figure(3, figsize=(5*1.618, 5))
sns.kdeplot(df[Infomapa.header['mes']], df[Infomapa.header['ano']])

plt.figure(2, figsize=(5*1.618, 5))
sns.distplot(df[Infomapa.header['fxet']].size())
'''
#sns.violinplot(x='Faixa Etária', y='Mês', data=df, jitter=True)
plt.figure(2, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
sns.countplot(x=df[Infomapa.header['fxet']], data=df, palette="Greens_d")
df.sort_values([Infomapa.header['fxet'],Infomapa.header['mlv']],ascending=[True, False], inplace=True)
render_template('IBGE _ Cidades _ São Paulo - SP', result=figdata_png.decode('utf8'))
sns.plt.show()
