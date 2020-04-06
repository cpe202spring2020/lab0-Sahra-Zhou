def weight_on_planets():
   # write your code here
   weight = int(input("What do you weigh on earth? "))
   w_Mars = weight * 0.38
   w_Jup = weight * 2.34
   print(f"\nOn Mars you would weigh {w_Mars} pounds.\nOn Jupiter you would weigh {w_Jup} pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
