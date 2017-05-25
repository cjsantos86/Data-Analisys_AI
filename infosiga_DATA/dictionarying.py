import pandas as pd



df = pd.read_csv('infosiga.csv', encoding="latin-1", index_col=0)
for col in df.columns:
    if col[:19]=='MunicÃ­pio Acidente':
        df.rename(columns={col:'MunAcidente' + col[19:]}, inplace=True)
    if col[:14]=='Turno Acidente':
        df.rename(columns={col:'Periodo' + col[14:]}, inplace=True)
    if col[:4]=='MÃªs':
        df.rename(columns={col:'Mes' + col[4:]}, inplace=True)
    if col[:16]=='Tipo de Acidente':
        df.rename(columns={col:'TipAcidente' + col[11:]}, inplace=True)
    if col[:36]=='Meio de LocomoÃÂ§ÃÂ£o da VÃÂ­tima':
        df.rename(columns={col:'Modal' + col[36:]}, inplace=True)
    if col[:15]=='Faixa EtÃÂ¡ria':
        df.rename(columns={col:'FaixaEt' + col[15:]}, inplace=True)
    if col[:17]=='Latitude Acidente':
        df.rename(columns={col:'Latitude' + col[14:]}, inplace=True)
    if col[:18]=='Longitude Acidente':
        df.rename(columns={col:'Longitude' + col[16:]}, inplace=True)
   
df = df.set_index(['MunAcidente','Ano','Mes'])
df.head()

print(df.columns)
print(df)
    
