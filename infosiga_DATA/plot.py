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
        self.df = None
        self._open_all_infomapa_csv()
        self._normalize_stings()
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
                print(fname)
                if os.path.isfile(fname):
                    total.append(pd.read_csv(fname, sep=';', header=0))

        self.df = pd.concat(total, ignore_index=True)


    def _normalize_stings(self):
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

df = Infomapa().df

print(df)
