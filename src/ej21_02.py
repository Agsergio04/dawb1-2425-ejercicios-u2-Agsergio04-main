"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
"""
def pedir_contraseña():
    parametro = input("Introduce la contraseña: ")
    return parametro

def comprobar_contrasenia(contrasenia,pregunta):
    comprobacion = True
    
    if contrasenia == pregunta:
        comprobacion = False
        
    return comprobacion
def main():
    contrasenia = "python"
    
    pregunta = pedir_contraseña().lower()
    
    while comprobar_contrasenia(contrasenia,pregunta):
        print("Contraseña incorecta,vuelva a introducirla de nuevo")
        pregunta = pedir_contraseña().lower()
        
    print("Has iniciado sesion correctamente")
    
    
if __name__ == "__main__":
    main()