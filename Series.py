import pandas as pd
#se crea una serie con ayuda de pandas
ps = pd.Series([20,15,24,65])

print(ps)

ps1 = pd.Series([1,5,9,10,15])
# Se convierte la serie en lista con pandas
print(ps1)
print(type(ps1))
print(ps1.to_list())
