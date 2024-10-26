def division_numero(primer_numero,segundo_numero):
    resultado  = 0
    
    numerador,denominador = primer_numero,segundo_numero
    
    resultado = numerador / denominador
    
    return resultado

def main():
    bandera = True
    while bandera:
        try:
            primer_numero = int(input("Introduce un numero: "))
            segundo_numero = int(input("Introduce otro numero: "))
            
            resultado = division_numero(primer_numero,segundo_numero)
        except ValueError:
            print("**ERROR**\nTienes que poner un numero.")
        except ZeroDivisionError:
            print("**ERROR**\nNo puedes dividir por 0.")
            bandera = False
        else: 
            print(f"El resultado de dividir {primer_numero:.2f} entre {segundo_numero:.2f} es {resultado:.2f}")

if __name__ == "__main__":
    main()