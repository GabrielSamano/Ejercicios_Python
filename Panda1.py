import pandas as pd

data = {
    "Rutina": ["Brazo", "Pecho", "Pierna"],
    "Tiempo": [15,10,20]
}

myvar = pd.DataFrame(data, index = ["Dia 1", "Dia 2", "Dia 3"])

print(myvar)
