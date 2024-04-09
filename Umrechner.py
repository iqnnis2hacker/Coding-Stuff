import math


def auswahl():
  print("Bitte wählen Sie eine Option:")
  print("1: km/h in m/s konvertieren")
  print("2: m/s in km/h konvertieren")
  wahl = input("Auswahl: ")

  if wahl == "1":
    v1 = float(input("Geschwindigkeit in km/h: "))
    result = v1 * 10 / 36  # Umrechnung km/h in m/s
    print(f"{v1} km/h sind {result} m/s.")
  elif wahl == "2":
    v2 = float(input("Geschwindigkeit in m/s: "))
    result = v2 * (3600 / 1000)  # Umrechnung m/s in km/h
    print(f"{v2} m/s sind {result} km/h.")
  else:
    print("Ungültige Auswahl.")

auswahl()

input("")