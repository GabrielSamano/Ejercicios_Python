import pandas as pd

data = {
    "Rutina": ["Brazo", "Pecho", "Pierna"],
    "Tiempo": [15,10,20]
}

myvar = pd.DataFrame(data)

print(myvar)
