def calcular_precio(edad):
    mensaje = ""

    if edad < 4:
        mensaje = "puedes entrar gratis"
    elif 4 < edad < 18:
        mensaje = "para entrar debes pagar 5 euros"
    elif edad > 8:
        mensaje = "para entrar debes pagar 10 euros"

    return mensaje

def pedir_edad():
    return int(input("Introduce tu edad: "))


def main():
    bandera = None

    while bandera:
        try:
            edad = pedir_edad()

            if edad == 0:
                break

            mensaje = calcular_precio(edad)

            print(f"Tienes {edad} años,asi que {mensaje}") 

        except ValueError:
            print("**ERROR**\nIntroduce una edad valida.")    
if __name__ == "__main__":
    main()