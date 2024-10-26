#######################################################################
"""
Esto mas que nada para poner al principio de cada programa en vez de 
poner esto copio y pego
"""
def main():
    pass
if __name__ == main():
    main()
#######################################################################
""" 
Una funcion que sirve para mirar si una cadena introducida puede ser
valida como numero a operar.Siendo general para todos los numeros
"""
def comprobar_numero(numero: str) -> bool:
    
    
    #Comprovar si es un numero negativo
    if numero.startswith("-"):
        numero = numero[1:]
        
    #Metodo para intercambiar comas por puntos
    if numero.count(",") > 0:  
        numero = numero.replace(",",".")
        
    #Comprovar el numero si tene decimales  
    if numero.count(".") < 1:
        
        numero = numero.replace(".","")
    
        
    return  numero.isdigit()
#######################################################################   