import numpy as np
#Team_codeforce #Bautista 
contador=0
try:
  Numero_problemas=int(input("Numero de problemas:"))  #input para insertar numero de problemas 
  for i in range (Numero_problemas):            #un for para crear tantos arreglos de tres elementos entre 0 a 1 como numeros de problemas del intput 
    z=np.random.randint(0,2,3)                   
    if sum(z)>=2:                   #sumatoria de los elementos de los arreglos para saber que si pasan el filtro del codigo
      contador+=1                   #contador para llevar el numero de arreglos que si pasan la condicion 
    print(z)                        #se imprimen los arreglos 
  print(contador)                   #se imprime el numero de arreglos que pasan la condicion 
except:
  print("Value Error, inserte un numero :)")
