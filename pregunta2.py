# -*- coding: utf-8 -*-
"""Pregunta2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GPCKhb3Aw0Csqb3513FQtfUawcq0pVh8
"""

#DATOS:QUISPE CRISOSTOMO EDISON

def CalcularMC():
  Peso = float(input("Ingrese su Peso: "))
  Talla = float(input("Ingrese su Talla: "))
  if Talla <= 0:
    print("Su Talla tiene que ser Mayor a 0")
    return
  MC = Peso / (Talla ** 2)
  print(f"Tu Indice de Masa Corporal (IMC) es: {MC}")
CalcularMC()