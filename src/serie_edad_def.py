def pedir_edad():
    edad = None
    
    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)
        except ValueError as e:
            if edad is None:
                print("**ERROR**\nEl valor introducido no es valido.")
            else:
                edad = None
                print(f"**ERROR**\n {e} Intentalo de nuevo !!!")
    return edad


def validar_edad(edad: int):
    if edad < 0 :
        raise ValueError("La edad no puede ser negativa.")
    if edad > 125:
        raise ValueError("La edad no puede ser mayor de 125.")
    if edad == 0:
        raise ValueError("La edad no puede ser 0.")
    

def mostrar_anios_cumplidos(msg):
    linea = "1"
    for i in range(1,int(msg) + 1):
        if i > 1:
            linea += " " + str(i)
    print(f"Los años cumplidos en una cadena son : {linea}")


def main():
    edad = pedir_edad()
    
    if edad != None:
        mostrar_anios_cumplidos(edad)
        
if __name__ == "__main__":
    main()
