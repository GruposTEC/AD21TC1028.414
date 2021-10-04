import matplotlib.pyplot as plt


def grafica(x, y):
    plt.title("Ejercicio de graficacion")
    plt.xlabel("Días del mes")
    plt.ylabel("Casos Covid19")

    plt.axis([0, 5, 0, 7])  # xmin , xmax, ymin, ymax

    x2 = ["01/20/21", "", "03/20/21", "", "05/20/21"]

    plt.xticks(x, x2, rotation=90)
    plt.plot(x, y)
    plt.show()


def main():
    x = [1, 2, 3, 4, 5]
    y = ["0.5", "1", "6", "3", "5.5"]
    grafica(x, y)


print(__name__)
if __name__ == "__main__":
    main()
