numero = float(input("Ingrese un numero: \n"))

if numero > 0:
    print(f"el numero", {numero} ,"es positivo")
    if numero % 2 == 0:
        print(f"su numero" ,{numero},"es par")
    else:
        print(f"su numero" , {numero},"es impar")
elif numero < 0:
    print(f"el numero", {numero} ,"es negativo")
    if numero % 2 == 0:
        print(f"su numero" ,{numero},"es par")
    else:
        print(f"su numero" , {numero},"es impar")
else:
    print("el numero es cero")
