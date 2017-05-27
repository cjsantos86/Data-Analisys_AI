import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('infosiga.csv', encoding="latin-1", index_col=0)
for col in df.columns:
    if col[:19]=='MunicÃ­pio Acidente':
        df.rename(columns={col:'MunAcidente' + col[19:]}, inplace=True)
    if col[:14]=='Turno Acidente':
        df.rename(columns={col:'Periodo' + col[14:]}, inplace=True)
    if col[:4]=='MÃªs':
        df.rename(columns={col:'Mes' + col[4:]}, inplace=True)
    if col[:16]=='Tipo de Acidente':
        df.rename(columns={col:'TipAcidente' + col[16:]}, inplace=True)
    if col[:36]=='Meio de LocomoÃÂ§ÃÂ£o da VÃÂ­tima':
        df.rename(columns={col:'Modal' + col[36:]}, inplace=True)
    if col[:15]=='Faixa EtÃÂ¡ria':
        df.rename(columns={col:'FaixaEt' + col[15:]}, inplace=True)
    if col[:17]=='Latitude Acidente':
        df.rename(columns={col:'Latitude' + col[17:]}, inplace=True)
    if col[:18]=='Longitude Acidente':
        df.rename(columns={col:'Longitude' + col[18:]}, inplace=True)

#add a category in table
df['Quantidade'] = 1
print(df.columns)

df.Sexo.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NAO DISPONIVEL': 'ND',
                  'NÃÂ£o Especificado' : 'NE',}, inplace=True)

df.Periodo.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NAO DISPONIVEL': 'ND',
                  'NÃÂ£o Especificado' : 'NE',
                 'ManhÃÂ£' : 'Manha'}, inplace=True)

df.TipAcidente.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NAO DISPONIVEL': 'ND',
                  'NÃÂ£o Especificado' : 'NE',
                 'ManhÃÂ£' : 'Manha',
                 'ColisÃÂ£o' : 'Colisao'}, inplace=True)

df.Modal.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NAO DISPONIVEL': 'ND',
                  'NÃÂ£o Especificado' : 'NE',
                  'AutomÃÂ³vel' : 'Automovel',
                  'CaminhÃÂ£o' : 'Caminhao'}, inplace=True)

df.FaixaEt.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NÃÂ£o Especificado' : 'NE',
                  'NAO DISPONIVEL': 'ND'}, inplace=True)

df.Latitude.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NÃÂ£o Especificado' : 'NE',
                  'NAO DISPONIVEL': 'ND'}, inplace=True)

df.Longitude.replace({'NÃÂ£o DisponÃÂ­vel' : 'ND',
                  'Nao Disponivel' : 'ND',
                  'NÃÂ£o Especificado' : 'NE',
                  'NAO DISPONIVEL': 'ND'}, inplace=True)




print(df.Longitude,df.Latitude)




#s = df.loc['Modal']
#print(s)

df['Latitude'] = pd.to_numeric('Latitude', errors='coerce')
#df['Longitude Acidente'] = pd.to_numeric(df['Longitude Acidente'], errors='coerce')                        

#Indexing table
df = df.set_index(['MunAcidente','Ano'])
df.head()

'''
#Find a City
sampa = df.loc['Sao Paulo']
print(sampa)

#New table with number of death
df = df.groupby(level=0)['Quantidade'].agg({'Sum':np.sum})
print(df)


#Mask [pequeno, Medio , Grande] apply in table above

df = df.groupby(level=0)['Quantidade'].agg({'Sum':np.sum})
df = df.groupby(level=0)['Sum'].agg({'Avg': np.average})
print(pd.cut(df['Avg'], 3, labels=["Pequeno","Medio","Grande"]))
'''
'''
#Death per 100k Hab.
df = df.groupby(level=0)['Quantidade'].agg({'Sum':np.sum})

print(df)
'''    
