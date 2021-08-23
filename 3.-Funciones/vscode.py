var_global = 5
"""
PONER ALGORITMO
"""

def mayor2(x, y):
    """Funcion que calcula el mayor de dos numeros
    Args:
        x ([int]): [Primer número]
        y ([int]): [Segund número]

    Returns:
        [int]: [EL mayor de los dos]
    """
    global var_global
    
    var_global = 3
    temp = 0;
    if x > y :
        temp = x
    else:
        temp = y
    
    x = x + 1
    y = y + 1
    
    return temp  
    
primera = 10;
segunda = 5

mayor = mayor2(primera,segunda)

print(mayor)