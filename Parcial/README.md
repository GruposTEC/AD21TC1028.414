[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5556201&assignment_repo_type=AssignmentRepo)
# TC1028 Exámen Parcial 

Escribe un programa en Python que nos ayude a determina que tan alta será nuestra multa de tránsito.

El archivo se debe de llamar i**nfraccion.py** , el método se debe de llamar **calculo_multa**

El método debe de contar con su **algoritmo** (inlciuyendo la imagen del diagrama de flujo en png o jpg) y su **docstring** ( 10  pts c/u)

La situación es la siguiente:

1.- (60 pts) Usted ha manjeado un poco rápido y ha sido detenido por una gente de tránsito. Calcule el monto de su multa codificándola de la siguiente forma

- 0 : no infraccion
- 1: infraccion pequeña
- 2 : infracción grande

Si la velocidad es 60 o menos el resultado es cero, si es entre 61 y hasta ser igual a 80 el resultado es uno, si la velocidad es 81 o mayor , el resultado es dos.

A menos que sea su cumpleaños , donde la velocidad puede ser 5 km/h mayor en todos los casos.

El método deberá recibir:

1. la velocidad a la que iba manejando 
2. un valor booleano que indique si es su cumpleaños

Por ejemplo

`calcula_multa(60,False) regresará 0`

Recuerde que este método **NO** deberá contener las instrucciones `input o print`

2.- (20 pts) en el método main lea el archivo llamado velocidades.csv un conjunto de velocidades y el valor booleano que indica si cumple años o no

Estos dos elementos están en diferentes renglones, tome en cuenta esta para realizar su código

Recuerde también que estás recibiendo strings con retornos de carro al  final











