def main():
    # escribe tu código abajo de esta línea
pass
anterior=float(input("Saldo del mes anterior:"))
ingresos=float(input("Ingresos:"))
egresos=float(input("Egresos:"))
cheque=float(input("Cantidad de cheques:"))

#Suma de todo
total1= (anterior+ingresos-egresos)-(cheque*13)

# Operaciones para sacar el total
total2= total1- (total1*o.075)

#Muestra del resultado final al usuario
print("El saldo final de la cuenta es:",total2)

if __name__ == '__main__':
    main()
