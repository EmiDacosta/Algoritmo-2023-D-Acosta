# Desarrollar una función que permita convertir un número romano en un número decimal.

def de_romano_a_decimal(numeroromano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # String vacio
    if len(numeroromano)==0:
        return 0
    
    #String de 1 len
    elif len(numeroromano)==1:
        return romanos[numeroromano]
    #string 1<2 (Casos como el valor de 4: IV)
    elif romanos[numeroromano[0]]< romanos[numeroromano[1]]:
        return romanos[numeroromano[1]] - romanos[numeroromano[0]] + de_romano_a_decimal(numeroromano[2:])
    #string 1>=2
    else:
        return romanos[numeroromano[0]] + de_romano_a_decimal(numeroromano[1:])

    

print(de_romano_a_decimal(input("Ingrese un numero (EN MAYUSCULA): ")))
