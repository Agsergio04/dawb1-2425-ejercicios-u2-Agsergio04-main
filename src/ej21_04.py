def par_o_impar(numero):
    comprobacion = "Impar" 
    if (numero % 2 == 0):
        comprobacion = "par"
    
    return comprobacion

def main():
    bandera = True
    while bandera:
        try:
            entrada = input("Introduce un numero entero. \nEscribe fin para salir!!\n").lower()
            
            if entrada == "fin":
                break
        
            entrada = int(entrada)
            print(par_o_impar(entrada))
            
        except ValueError :
            print("**ERROR**\nIntroduce un numero valido")
            
            
if __name__ == "__main__":
    main()