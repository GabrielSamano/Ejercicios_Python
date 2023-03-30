# Alcance de variables, local y global
# Local
def Myfunc():
    x = 5
    print(x)

Myfunc()
# Global
x= 5
print(x)

# Consulta Local de una funcion dentro de una funcion.

def FirstFunc():
    x = 100
    def Seconfun():
        print(x)
    Seconfun()
FirstFunc()

