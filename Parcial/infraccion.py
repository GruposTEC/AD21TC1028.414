# pseudocodigo
def calculo_multa(veloc, cumple):
    """Metodo que calcula la multa de una persona

    Args:
        veloc ([int]): [La velocidad ala que va el vehiculo]
        cumple ([bool]): [Es su cumpleanios o no]

    Returns:
        [int]: [El tipo de multa]
    """
    multa = 0

    if cumple == True:
        veloc = veloc - 5

    if veloc <= 60:
        multa = 0
    else:
        if veloc > 60 and veloc <= 80:
            multa = 1
        else:
            multa = 2

    return multa


#print(calculo_multa(90, False))

def main():
    f = open("velocidades.csv", "r")
    cont = 0
    for datos in f:
        if cont % 2 != 0:
            boleano = datos
            if(boleano == "True"):
                boleano = True
            else:
                boleano = False
            print(calculo_multa(int(vel), boleano))
            cont = 0
        else:
            vel = datos
            cont = cont + 1


main()
