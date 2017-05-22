import numpy as np
import pandas as pd

f = open("test.arff", 'r')

myList = []
df = []
df1 = []*422
for line in f:
    myList.append(line)    
myList = [i.split('\n',1)[0] for i in myList]
f.close()

print(myList[120])

for x in range(len(myList)):
    df = myList[x]
    df = df.split(',')
    df1.append(df)
    
#df1[13] == ['@data']
#df1[14+][0] == Nomes Cidades
#df1[14+][1] == Ano
#df1[14+][2] == Mes
#df1[14+][3] == Sexo
'''--- Masculino
   --- Feminino
   --- 99999
'''
#df1[14+][4] == Periodo
'''--- Turno do Acidente
   --- Manhã
   --- Tarde
   --- Noite
   --- Madrugada
   --- 99999
'''
#df1[14+][5] == Tip Acid
'''---Colisão – acidente de trânsito envolvendo 02 ou mais veículos em
circulação.
   --- Atropelamento – colisão de um veículo em movimento com pedestre(s).
   --- Choque – colisão de um veículo em movimento com um obstáculo fixo
ou veículo fora de circulação da via.
   --- Outros – acidente de trânsito que não se enquadra em nenhum dos
tipos acima. Ex.: capotamento, tombamento, quedas, etc.
   --- 99999 – não constam informações sobre o tipo de acidente
na base de dados.
'''
#df1[14+][6] == Modal
'''--- Motocicleta
   --- Pedestre
   ---Automóvel 
   --- Bicicleta
   --- Ônibus
   --- Outros: qualquer meio de locomoção diferente dos acima (ex.: trator,
charrete, etc)
   --- 99999: não foi possível a identificação do veículo por meio do
boletim de ocorrência
'''
#df1[14+][7] == Idade
'''--- 17 anos
   --- 20 anos
   --- 27anos
   --- 32 anos
   --- 37 anos
   --- 42anos
   --- 47 anos
   --- 52 anos
   --- 57 anos
   --- 62 anos
   --- 67 anos
   --- 72 anos
   --- 77 anos
   --- 80 anos ou mais
   --- 99999: a idade da vítima não consta no registro
'''
#df1[14+][8] == Lat
#df1[14+][9] == Long
    
cidade = df1[14][0]
ano = df1[14][1]
unknow = 99999
print(df1[320][3])

'''
x = 14
feminino = 0
masculino = 0
s_desconhecido = 0
manha = 0
tarde = 0
noite = 0
madrugada = 0
p_desconhecido = 0
colisao = 0
atropelamento = 0
while (x <= 422):
    if(df1[x][3] == 'FEMININO'):
        feminino +=  1
        print(feminino)
    
   elif(df1[x][3] == 'MASCULINO'):
        masculino = masculino + 1

    elif(df1[x][3] == 99999):
        s_desconhecido = s_desconhecido + 1

    elif(df1[x][4] == 'MANHA'):
        manha = manha + 1

    elif(df1[x][4] == 'TARDE'):
         tarde = tarde + 1

    elif(df1[x][4] == 'NOITE'):
         noite = noite + 1

    elif(df1[x][4] == 'MADRU'):
         madrugada = madrugada + 1

    elif(df1[x][4] == 99999):
        p_desconhecido = p_desconhecido + 1

    elif(df1[x][5] == 'COLISAO'):
         colisao = colisao + 1

    elif(df1[x][5] == 'ATROPELAMENTO'):
         atropelamento = atropelamento + 1

    elif(df1[x][5] == 'CHOQUE'):
         choque = choque + 1

    elif(df1[x][5] == 'OUTROS'):
         outros = outros + 1

    elif(df1[x][5] == 99999):
        tip_desconhecido = tip_desconhecido + 1

    elif(df1[x][6] == 'MOTOCICLETA'):
         motocicleta = motocicleta + 1

    elif(df1[x][6] == 'PEDESTRE'):
         pedestre = pedestre + 1

    elif(df1[x][6] == 'BICICLETA'):
         bicicleta = bicicleta + 1

    elif(df1[x][6] == 'ONIBUS'):
         pedestre = pedestre + 1

    elif(df1[x][6] == 'AUTOMOVEL'):
         onibus = onibus + 1

    elif(df1[x][6] == 'OUTROS'):
         outros = outros + 1

    elif(df1[x][6] == 99999):
        m_desconhecido = m_desconhecido + 1

    elif(df1[x][7] == 17):
        a_17 = a_17 + 1

    elif(df1[x][7] == 20):
        a_20 = a_20 + 1

    elif(df1[x][7] == 27):
        a_27 = a_27 + 1

    elif(df1[x][7] == 32):
        a_32 = a_32 + 1

    elif(df1[x][7] == 37):
        a_37 = a_37 + 1

    elif(df1[x][7] == 42):
        a_42 = a_42 + 1

    elif(df1[x][7] == 47):
        a_47 = a_47 + 1

    elif(df1[x][7] == 52):
        a_52 = a_52 + 1

    elif(df1[x][7] == 57):
        a_57 = a_57 + 1

    elif(df1[x][7] == 62):
        a_62 = a_62 + 1

    elif(df1[x][7] == 67):
        a_62 = a_67 + 1

    elif(df1[x][7] == 72):
        a_77 = a_77 + 1

    elif(df1[x][7] == 77):
        outros = outros + 1

    elif(df1[x][7] == 80):
        a_80 = a_80 + 1

    elif(df1[x][7] == 99999):
        a_desconhecido = a_desconhecido + 1
    x += 1  

'''  

