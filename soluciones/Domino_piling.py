#Domino Pyling CODEFORCE #by:Bautista
dim=input("")                
dim_lista=dim.split(" ")    
dim_entero=[int(i)for i in dim_lista]  
espacio=dim_entero[0]*dim_entero[1]   
if espacio%2==0:
    print(int(espacio/domino)) 
elif espacio%2!=0:
  print(int((espacio-1)/2))
