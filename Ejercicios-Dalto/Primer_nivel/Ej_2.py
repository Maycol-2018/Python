"""
Descripción: Teniendo en cuenta que una persona habla 2 palabras por segundo.
a- Pedirle al usuario un texto
- Calcular cuanto tardaria en decir esa frase. 
- ¿Cuantas palabras dijo?

b- Si te tarda más de un minuto 
- Mostrar un mensaje ""para che, tampoco te pedi un testamento"

c- Si una persona habla un 30% más rapido que el promedio cuanto tardaria él en decirlo"""

pala_seg = 2

texto = input("Ingresar un texto\n -")
lista = texto.split(" ")

print("""_____Ejercicio a_____""")
cant_palabras = len(lista)
tiempo_empleado = cant_palabras/pala_seg

print(f"\nUna persona se tardaria en decir esa frase {tiempo_empleado} segundos")
print(f"Dijiste -> {cant_palabras} palabras")

print("""\n_____Ejercicio b_____""")

if tiempo_empleado > 4:
    print("Para che, tampoco te pedi un testamento")
else:
    print("Fuiste muy concreto")

print("""\n_____Ejercicio c_____""")
dalto = pala_seg + (30*pala_seg) / 100
tiempo_empleado = cant_palabras / dalto
tiempo_empleado = round(tiempo_empleado,2)

print(f"Si una persona habla un 30% más rapido, él tardaria en decir la misma frase en {tiempo_empleado} segundos")
