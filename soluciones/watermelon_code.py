#watermelon code 
#Bautista
 
try:
  weight=int(input("Weight: "))        
  if weight>=1 and weight<=100 and weight!=2:
    if weight%2==0:
      print("Yes")
    else:
      print("No")
  else:
    print("Value out of Range")
except:
    print("Value Error")
