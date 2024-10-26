def calculo_tipo_impositivo(entrada):
    calculo = None  
    if entrada < 0:
        calculo = None
    elif entrada < 10000:
        calculo = 5
    elif entrada < 20000:
        calculo = 15
    elif entrada < 35000:
        calculo = 20
    elif entrada < 60000:
        calculo = 30
    else: 
        calculo = 45
    
    return calculo

def main():
    condicion = True

    while condicion:
        try:
            entrada = float(input("Introduce tu nómina anual: "))
            improvisto = calculo_tipo_impositivo(entrada)
            
            if improvisto is None: 
                raise ZeroDivisionError("Introduce un número que no sea negativo")
            if entrada != 0:
                print(f"Tu impuesto es del {improvisto} %")
            if entrada == 0:
                condicion = False
    
            
        except ZeroDivisionError as mensaje:
            print(mensaje)
        except ValueError:
            print("**ERROR**\nIntroduce un numero.")

if __name__ == "__main__":  
    main()
