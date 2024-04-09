import math


def selection():
  print("Please choose an option:")
  print("1: km/h in m/s")
  print("2: m/s in km/h)
  choose = input("Selection: ")

  if choose == "1":
    v1 = float(input("Speed in km/h: "))
    result = v1 * 10 / 36  
    print(f"{v1} km/h are {result} m/s.")
  elif choose == "2":
    v2 = float(input("Speed in m/s: "))
    result = v2 * (3600 / 1000)  
    print(f"{v2} m/s are {result} km/h.")
  else:
    print("Invalid selection.")

selection()

input("")
