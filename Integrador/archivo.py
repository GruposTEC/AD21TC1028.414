def lectura_archivo(nombre):
    matriz = []
    f = open(nombre, "r")
    for elem in f:
        separados = elem.split(",")
        matriz.append(separados)

    f.close()
    return matriz


def main():
    res = lectura_archivo("covidmx_reducido.csv")
    print(res)


if __name__ == "__main__":
    # main()

    mat = [[1, 2, 3, 4], [5, 6, 7, 8]]

    for elem in mat:
        for elem2 in elem:
            print(elem2)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j])
