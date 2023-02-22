#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:49:40 2023

@author: jrodg85
"""

a = int(input("introduzca un numero entero mayor que 0 "))
while a<0:
    print ("El numero introducido",a,"es menor que 0.")
    a= int(input("Introduzca un numero entero mayor que 0 "))
print("El numero introducido es ", a)


def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print ("los numeros primos hasta ", a, " son los siguientes \n")


b=2
while b<=a:
    if is_prime(b)== True:
        print(b, end=(" "))
        b+=1
    else:
        b+=1
    

