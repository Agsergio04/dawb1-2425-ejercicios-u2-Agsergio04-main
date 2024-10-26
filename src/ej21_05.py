def comprobar_tributacion(dinero):
    comprobar_dinero = False
    
    if dinero >= 1000:
        comprobar_dinero = True
    
    return comprobar_dinero


def comprobar_edad(anios):
    comprobracion_edad = False
    
    if anios > 16 and anios < 125:
        comprobar_edad = True
        
    return comprobracion_edad


def pedir_edad_y_tributacion():
    anios = int(input("¿Cuantos años tienes?\n"))
    dinero = float(input("¿Cuanto dinero cobras?\n"))
    
    return anios,dinero


def main():
    bandera = True
    while bandera:
        try:
            edad,sueldo = pedir_edad_y_tributacion()
            bandera = False
        except ValueError:
            print("Por favor escribe un valor valido")
            
            
    if comprobar_edad(edad) and comprobar_tributacion(sueldo):
        print("Por desgracia...Tienes que tribuar\nQue mal")
    else:
        print("Vaya que alegria,no tienes que tributar nada")    
        
if __name__ == "__main__":
    main()