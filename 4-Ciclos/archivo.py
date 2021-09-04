f = open("/home/avmejia/TEC/AGO-DIC-21/TC1028/AD21TC1028.414/4-Ciclos/lista.csv", "r")
#f = open("C:\\avmejia\\TEC\\AGO-DIC-21\\TC1028\\AD21TC1028.414\\4-Ciclos\\lista.csv", "r")

for alumno in f:
    print(type(alumno))
    print(alumno)
