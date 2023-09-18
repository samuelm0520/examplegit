"""
    Fecha: 18/09/2023
    Autor: Samuel Montoya Mayor
    Objetivo: Ejemplo de versionamienot con git desde python 

"""
import random

print("---------------------------------------------------------")
random_number = random.randint(1, 10)
print(random_number)

print ("------------------------------------------------------------")

for i in range (0, 10):
    random_number = random.randrange(20, 100, 5)
print(random_number)

print ("------------------------------------------------------------")

for i in range(0, 10):
    random_number = random.random()
    print(random_number)

print ("------------------------------------------------------------")

for i in range(0, 10):
    random_number = random.uniform(10.5, 20.6)
    print(random_number)