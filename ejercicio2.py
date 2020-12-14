# gestionar todas las provincias de Panamá
provincias = {'BOCAS DEL TORO':['Almirante','Bocas del Toro','Changuinola','Chiriqui Grande'],
              'COCLE':['Agua Dulce','Antón','La Pintada','Natá','Olá','Penonomé'],
              'COLON':['Colón','Chagres','Donoso','Portobelo','Santa Isabel','Omar Torrijos Herrera'],
              'CHIRIQUI':['Alanje','Barú','Boquerón','Boquete','Bugaba','David','Dolega','Gualaca','Remedios',
                          'Renacimiento','San Félix','San Lorenzo','Tierras Altas','Tolé'],
              'DARIEN':['Chepigana','Santa Fe','Pinogana'],
              'HERRERA':['Chitré','Las Minas','Los Pozos','Ocú','Parita','Pesé','Santa Maria'],
              'LOS SANTOS':['Guararé','Las Tablas','Los Santos','Macaracas','Pedasi','Pocrí','Tonosi'],
              'PANAMA':['Balboa','Chepo','Chimán','Panamá','San Miguelito','Taboga'],
              'VERAGUAS':['Atalaya','Calobre','Cañazas','La Mesa','Las Palmas','Mariato','Montijo','Río de Jesus',
                          'San Francisco','Santa Fe','Santiago','Soná'],
              'PANAMA OESTE':['Arraiján','Capira','Chame','La Chorrera','San Carlos']}

while(True):
    try:
        print("\n1) Consultar distritos.")
        print("2) Salir.\n")
        opcion = int(input("Opcion: "))
        if (opcion == 1):
            provincia = input("\nIngrese el nombre de la provincia (sin tíldes): ")
            resultado = provincias.get(provincia.upper())
            if (resultado == None):
                print("\nNo se encontro la provincia ingresada")
            else:
                print()
                for i in range(len(resultado)):
                    print(resultado[i])
        if (opcion == 2):
            print("Gracias por usar el programa!")
            break
    except:
        print("\nESCOJA UNA DE LAS DOS OPCIONES!(1 ó 2)\n")
    