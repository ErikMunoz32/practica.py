"""
Programa ISR
Autor: Erik Muñoz Rodriguez

Calcular el impuesto sobre la renta (ISR) anual de una persona:

1. Datos de entrada son:
Sueldo bruto anual
Numero de dependientes

2.Restricciones
A todos los contribuyentes se les cobra una tasa de impuestos fija del 20%.
A todos los contribuyentes se les permite una deducción estándar de $10,000.
Por cada dependiente, al contribuyente se le permite una deducción adicional de $2,000.
El sueldo bruto debe ingresarse al centavo más cercano.
El ISR se expresa como un número decimal.


3. Calculos:
ISR=Sueldo bruto-(Numero de dependientes*2000)*0.20

4.Datos de salida:
Total a pagar de ISR
"""

print("Calcular ISR")

# Se piden los datos de entrada al usuario
Sueldo_Bruto=float(input(" Introduce el sueldo bruto anual:"))
Numero_de_dependientes=float(input(" Introduce el Numero de dependientes:"))

#Calculo del ISR
isr=(Sueldo_Bruto-(Numero_de_dependientes*2000))*0.20
ISR= round(isr, 2)
# Se despliega el resultado
print("La cantidad a pagar de ISR anualmente:",ISR, "pesos" )

print("Datos del Alumno")

print("Nombre del alumno: Erik Muñoz Rodriguez")
print("Matricula: 2223068499")
