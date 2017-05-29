import os
import pandas as pd


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
        self.name = 'infomapa'
        self.df = None
        self._open_all_infomapa_csv()
        #self._normalize_strings()
        self.df.to_csv('infomapa.csv')


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
                fname = self.name + '/'  # directory
                fname += '_'.join(['INFOMAPA', month, str(year), 'publicacao', 'csv'])
                fname += '.csv'
                if os.path.isfile(fname):
                    df = pd.read_csv(fname, sep=';', header=1, index_col=0) \
                           .dropna(axis=1, how='all').dropna(axis=0, how='all')
                    total.append(df)

        self.df = pd.concat(total, ignore_index=True)


    def _normalize_strings(self):
        """ Pass all strings inside self.df in lower case with the first
        character upper, sort database by cities, year and month and
        reset the index.
        """

        for key in ['mnac', 'sexo', 'trnac', 'tpac', 'mlv']:
            _key = Infomapa.header[key]
            self.df[_key] = self.df[_key].str.title()

        self.df = self.df.sort_values(by=[Infomapa.header['mnac'],
                                          Infomapa.header['ano'],
                                          Infomapa.header['mes'],])
        self.df = self.df.reset_index(drop=True)


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

    print(df.head())

    #plt.figure(1, figsize=(5*1.618, 5))
    #sns.kdeplot(df[Infomapa.header['ano']])

    #sns.plt.show()
