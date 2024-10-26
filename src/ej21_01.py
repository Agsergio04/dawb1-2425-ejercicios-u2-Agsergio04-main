"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
"""

def comprobar_edad(edad):
    condicion = True
    try:
        int(edad)
        if int(edad) < 18 :
            condicion = False
    
    except ValueError:
        print("*ERROR* Introduce un numero.")
  
    return condicion
   
    
def main():
    edad = input("Introduce tu edad: ")

    if comprobar_edad(edad) == True:
        print("Eres mayor de edad.")
    elif comprobar_edad(edad) == False:
        print("Eres menor de edad.")

if  __name__ == "__main__":
    main()