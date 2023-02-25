# Programa para implementar los operadores aritmeticos
print("----------------------------------------")
print("---------OPERADORES ARITMETICOS---------")
print("----------------------------------------")

# input
x= int(input("Digite el valor de x: ")) 
y= int(input("Digite el valor de y: "))

# procesing 
s = x + y
r = x - y
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

print("-----------------------------------------")
print("---------------RESULTADOS----------------")
print("-----------------------------------------")

print("Suma: " + str(s))
print("Resta: " + str(r))
print("Multiplicacion: " + str(m))
print("Division: " + str(d))
print("Modulo : " + str(mod))
print("Division entera: " + str(de))
print("Potencia: " + str(p))