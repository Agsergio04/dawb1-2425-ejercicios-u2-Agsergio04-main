def crear_triangulo(altura):
    cadena = ""
    triangulo = ""
    inicio = 1
    
    if (altura % 2 == 0):
        inicio = 0
    
    for i in range(inicio,altura + 1,2):
        cadena = str(i) + " " + cadena
        triangulo = triangulo + cadena + " \n"
    
    return triangulo


def par_o_impar(valor):
    comprobacion = True
    if (valor % 2 == 0):
        comprobacion = False
    
    return comprobacion


def comprobar_numero():
    condicion = True
    
    while condicion:
        try:
            numero = input("Introduce un número entero: ")
            numero_entero = int(numero)
            
            if numero_entero < 0:
                raise ZeroDivisionError("**ERROR***\nIntroduce un número entero positivo.")
            
            comprobacion =  numero_entero
            if numero_entero != None:
                condicion = False
        except ZeroDivisionError as mensaje:
            print(mensaje)
        except ValueError:
            print("**ERROR***\nIntroduce un número entero.")
        
    return comprobacion  


def main():
    
    altura = comprobar_numero()
    
    triangulo = crear_triangulo(altura)

    print(triangulo)
    
if __name__ == "__main__":  
    main()
