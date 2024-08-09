"""
Descripcion: 
****Horas de contenido de un curso de Python****
- Soy Dalto: 1.5h
- Minimo: 2.5h
- Promedio: 4h
- Maximo: 7h

****Crudo****
- Soy dalto: 3.5h
- Promedio: 5h

Ejercicio:
a- Diferencia en % de contenido entre el curso Soy Dalto y el resto.
b- Porcentaje de contenido inservible que se reduce con respecto al actual y el promedio.
c- Ver 10 horas de este curso a cuantas horas de video equivale a ver otros.
"""


soy_dalto = 1.5
minimo = 2.5
promedio = 4
maximo = 7

por_min = ((minimo-soy_dalto)*100)/2.5
por_prom = ((promedio-soy_dalto)*100)/4
por_max = ((maximo-soy_dalto)*100)/7

por_max=round(por_max,2)

print(f"""____Ejercicio a____ \n
Diferencia en porcentaje (%) con respecto a: \n
- Minimo: {por_min}%\n
- Promedio: {por_prom}%\n
- Maximo: {por_max}%\n\n """)

crudo_dalto = ((3.5 - soy_dalto)*100) / 3.5
crudo_dalto = round(crudo_dalto,2)

crudo_promedio = ((5-promedio) * 100/5)

print(f"""_____Ejercicio b_____\n
Diferencia en porcentaje (%) de contenido inservible:\n
- Soy Dalto: {crudo_dalto}% \n
- Promedio: {crudo_promedio}% \n\n""")

horas = 10
equiv_mini = (horas * minimo) / soy_dalto
equiv_mini = round(equiv_mini,2)

equiv_prom = (horas * promedio) / soy_dalto
equiv_prom = round(equiv_prom,2)

equiv_max = (horas * maximo) / soy_dalto
equiv_max = round(equiv_max,2)

print("_____Ejercicio c_____\n")
print(f"""Ver {horas} horas del curso Soy dalto equivale a ver: \n
-  {equiv_mini}h con respecto al minimo\n
-  {equiv_prom}h con respecto al promedio\n
-  {equiv_max}h con respecto al maximo\n""")




