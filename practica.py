from random import randrange

class Matriz() :
    # Constructor
    def __init__(self, size):
       self.size = size
       self.matriz = []

    # Generar matriz
    def createMatriz (self):
      # for que recorre las posiciones de las filas
      for i in range(self.size):
         # lista de almacenamiento
         row = []
         # for que recorre las posiciones de las columnas
         for x in range(self.size):
            # lista de números random en cada posición de fila
            row.append(randrange(10))
         # lista con las listas de filas
         self.matriz.append(row)
      
      for i in self.matriz:
         print(i)
      
    # Generar lista suma filas
    def sumRows (self):
      # Declaración lista donde guardar los valores de las sumas
      sumRow = []
      # for que recorre las posiciones de las filas
      for i in range(self.size):
        # variable de almacenamiento
        num = 0
        # for que recorre las posiciones de las columnas
        for j in range(self.size):
          # almacenamiento de la suma de las filas
          num = num + self.matriz[i][j]
        # agregación de las sumas de las filas en una lista
        sumRow.append(num)
      # salida en pantalla de la lista con las sumas de las filas 
      print('La suma de las filas es: ',sumRow)

    # Generar lista suma columnas
    def sumCols (self):
      # Declaración lista donde guardar los valores de las sumas
      sumCol = []
       # for que recorre las posiciones de las columnas   
      for i in range(self.size):
        # variable de almacenamiento
        num = 0
        # for que recorre las posiciones de las filas
        for j in range(self.size):
           # almacenamiento de la suma de las columnas
          num = num + self.matriz[j][i]
        # agregación de las sumas de las columnas en una lista
        sumCol.append(num)
      # salida en pantalla de la lista con las sumas de las columnas  
      print('La suma de las columnas es: ',sumCol)

def setMatrizSize ():  
   # Bloque Gestion de expeciones
   try :
      # entrada de datos y casting a entero
      size = int(input('Ingrese número tamaño matriz: '))
      # condición lanzamiento de error
      if size < 0 or size == False:
         raise ValueError
   # captura de errores
   except (ValueError, TypeError):
      print('Debes introducir un número entero mayor que 0')
      # recursividad input mientras el valor no sea correcto
      setMatrizSize()
   else:
      # creación del objeto
      miMatriz = Matriz(size)
      # llamada función que crea la matriz
      miMatriz.createMatriz()
      # llamada función que suma las filas
      miMatriz.sumRows()
      # llamada función que suma las columnas
      miMatriz.sumCols()

setMatrizSize()
