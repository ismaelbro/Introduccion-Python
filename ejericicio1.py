# Alí Baba y los Curenta Ladrones
i = 1
nombre = input("Ingrese su nombre: ")
while(i <= 10):
    print("\nIntento "+str(i))
    llave = input("Ingrese la frase mágica: ")
    i += 1
    if(llave == 'Ábrete Sésamo'):
        print("\nFlicidades!!!, esa es la frase.")
        break

if (i == 11):
    print(nombre+" la puerta se cerro eternamente :(")