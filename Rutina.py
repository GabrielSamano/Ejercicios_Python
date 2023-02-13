import matplotlib as plot
import pandas as pd

df = pd.DataFrame({'Tiempo de Lectura':[20,15,15,20,10],'Tiempo de ejemplos':[10,5,10,10,5],
'Tiempo de jercicios':[20,20,25,20,15]});

print(df)

df.plot.hist()
