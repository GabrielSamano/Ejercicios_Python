import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Pulso', y='Calorias', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()
