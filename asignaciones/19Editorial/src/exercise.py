def main():
    # escribe tu código abajo de esta línea
    pass
import math
palaras= int(input("Dame el numero de palabras:"))
cuartilla= int(math.ceil(palabras/475))

#Operaciones para calcular el precio
precio= (cuartilla*60)
preciofinal= precio - (precio*0.10)

#Muestra del costo de la publicación al usuario
print("El costo de la publicacion es:",preciofinal) 

if __name__ == '__main__':
    main()
