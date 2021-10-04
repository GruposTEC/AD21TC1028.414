# 1 import grafica_matplotlib
# 2 import grafica_matplotlib as graf
# 3 from grafica_matplotlib import grafica
from grafica_matplotlib import grafica as gr


def main():
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    # 1grafica_matplotlib.grafica(x, y)
    # 2graf.grafica(x, y)
    # 3grafica(x, y)
    gr(x, y)


if __name__ == "__main__":
    main()
