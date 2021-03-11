# water melon code
residuo=0
w=int(input("ingrese peso de la sandia:"))
if w>=1 and w<100:
    residuo=w%2
    if residuo ==0 and w!=2:
      print("si")
    else:
        print("no")
else:
    print("el peso debe estar entre 1 y 100")
