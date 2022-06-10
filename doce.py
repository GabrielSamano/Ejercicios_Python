# Iteradores
mytup = {"Apple","Sams","Andorid"};
myit= iter(mytup)

print(next(myit))
print(next(myit))
print(next(myit))

# Creando un Iterador
class MYiten:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MYiter()
Myiter = iter(myclass)

for x in Myiter:
    print(x)



