import random

users = {"Esteban":"***"}
usernames = list(users.keys())

prices = {"Concierto Peso Pluma":950, "Podcast de Padilla":300, "Tributo Michael Jackson":500, "Kendrick Lamar(ft. Drake)":800, "PawPatrol Soundtrack":100 }
concerts = list(prices.keys())

zonas = ["Gradas Naranja", "Gradas", "General B", "General A", "VIP"]

def buy(price):
    tickets = int(input("Cuantos boletos quieres comprar: "))

    while tickets > 4:
        tickets = int(input("\nNo puedes comprar mas de 4 boletos, intenta con menos: "))

    precio = price
    price = price * tickets
    print(f"\n-------------------------- El monto de un boleto es de ${precio} --------------------------\n-------------------- El monto total a pagar es por {tickets} boletos es de ${price} --------------------\n\n ------------ MÉTODOS DE PAGO ------------\n 1 - Tarjeta de Crédito o Débito\n 2 - Tienda Física")

    metodo = input("\nSelecciona tu método de pago: ")

    if metodo == "1":
        nCard = input("\nIngresa tu numero de targeta: ")

        while len(nCard) != 10:
            nCard = input("\nPor favor ingresa un numero de tageta válido (10 dígitos): ")    
        
        fecha = input("\nIngresa la fech de caducidad en esta forma 00-00 : ")

        secCode = input("\nIngresa tu código de seuridad: ")

        while len(secCode) != 3:
            secCode = input("\nPor favor ingresa un código de seguridad válido (3 dígitos): ")

        print("\n --------------- LA COMPRA SE COMPLETO CORRECTAMENTE ---------------\n")
    elif metodo == "2":
        code = random.randint(10000000,99999999)

        print(f"\n      Ve a la planta física más cercana e ingresa el siguiente código -------- {code} --------\n")

print("---------- BIENBENIDO A TICKET MASTER ----------\n--------------- INICIO DE SESIÓN --------------- ")

start = input(f"\n¿Quieres iniciar sesión? s/n: ")

while start == "s" or start == "S" or start == "si" or start == "Si" or start == "SI":
    start = start + "."

    username = input("\nIngresa tu nombre de usuario: ")
    password = input("\nIngresa tu contraseña: ")

    while password != users["Esteban"] or username != usernames[0]:
        print("\nSu nombre o contraseña son incorrectos, por favor intente de nuevo.")
        username = input("\nIngresa tu nombre de usuario: ")
        password = input("\nIngresa tu contraseña: ")

    print(f"\n----- Bienvenido {username}, Estos son los eventos disponibles -----\n 1 - Concierto Peso Pluma\n 2 - Podcast de Padilla\n 3 - Tributo Michael Jackson\n 4 - Kendrick Lamar(ft. Drake)\n 5 - PawPatrol Soundtrack")
    event = input("\nSelecciona el evento: ")

    if event == "1" or event == concerts[0]:
        print(f"\n--------- {concerts[0]} ---------\n 1 - {zonas[0]}\n 2 - {zonas[1]}\n 3 - {zonas[2]}\n 4 - {zonas[3]}\n 5 - {zonas[4]}")
        zone = input("\nSelecciona en que zona deseas estar: ")

        if zone == "1" or zone == zonas[0]:
            buy(prices["Concierto Peso Pluma"])
        elif zone == "2" or zone == zonas[1]:
            buy((prices["Concierto Peso Pluma"]+500))
        elif zone == "3" or zone == zonas[2]:
            buy((prices["Concierto Peso Pluma"]+1000))
        elif zone == "4" or zone == zonas[3]:
            buy((prices["Concierto Peso Pluma"]+1500))
        elif zone == "5" or zone == zonas[4]:
            buy((prices["Concierto Peso Pluma"]+2000))

    if event == "2" or event == concerts[1]:
        print(f"\n--------- {concerts[1]} ---------\n 1 - {zonas[0]}\n 2 - {zonas[1]}\n 3 - {zonas[2]}\n 4 - {zonas[3]}\n 5 - {zonas[4]}")
        zone = input("\nSelecciona en que zona deseas estar: ")

        if zone == "1" or zone == zonas[0]:
            buy(prices["Podcast de Padilla"])
        elif zone == "2" or zone == zonas[1]:
            buy((prices["Podcast de Padilla"]+500))
        elif zone == "3" or zone == zonas[2]:
            buy((prices["Podcast de Padilla"]+1000))
        elif zone == "4" or zone == zonas[3]:
            buy((prices["Podcast de Padilla"]+1500))
        elif zone == "5" or zone == zonas[4]:
            buy((prices["Podcast de Padilla"]+2000))

    if event == "3" or event == concerts[2]:
        print(f"\n--------- {concerts[2]} ---------\n 1 - {zonas[0]}\n 2 - {zonas[1]}\n 3 - {zonas[2]}\n 4 - {zonas[3]}\n 5 - {zonas[4]}")
        zone = input("\nSelecciona en que zona deseas estar: ")

        if zone == "1" or zone == zonas[0]:
            buy(prices["Tributo Michael Jackson"])
        elif zone == "2" or zone == zonas[1]:
            buy((prices["Tributo Michael Jackson"]+500))
        elif zone == "3" or zone == zonas[2]:
            buy((prices["Tributo Michael Jackson"]+1000))
        elif zone == "4" or zone == zonas[3]:
            buy((prices["Tributo Michael Jackson"]+1500))
        elif zone == "5" or zone == zonas[4]:
            buy((prices["Tributo Michael Jackson"]+2000))
    
    if event == "4" or event == concerts[3]:
        print(f"\n--------- {concerts[3]} ---------\n 1 - {zonas[0]}\n 2 - {zonas[1]}\n 3 - {zonas[2]}\n 4 - {zonas[3]}\n 5 - {zonas[4]}")
        zone = input("\nSelecciona en que zona deseas estar: ")

        if zone == "1" or zone == zonas[0]:
            buy(prices["Kendrick Lamar(ft. Drake)"])
        elif zone == "2" or zone == zonas[1]:
            buy((prices["Kendrick Lamar(ft. Drake)"]+500))
        elif zone == "3" or zone == zonas[2]:
            buy((prices["Kendrick Lamar(ft. Drake)"]+1000))
        elif zone == "4" or zone == zonas[3]:
            buy((prices["Kendrick Lamar(ft. Drake)"]+1500))
        elif zone == "5" or zone == zonas[4]:
            buy((prices["Kendrick Lamar(ft. Drake)"]+2000))

    if event == "5" or event == concerts[4]:
        print(f"\n--------- {concerts[4]} ---------\n 1 - {zonas[0]}\n 2 - {zonas[1]}\n 3 - {zonas[2]}\n 4 - {zonas[3]}\n 5 - {zonas[4]}")
        zone = input("\nSelecciona en que zona deseas estar: ")

        if zone == "1" or zone == zonas[0]:
            buy(prices["PawPatrol Soundtrack"])
        elif zone == "2" or zone == zonas[1]:
            buy((prices["PawPatrol Soundtrack"]+500))
        elif zone == "3" or zone == zonas[2]:
            buy((prices["PawPatrol Soundtrack"]+1000))
        elif zone == "4" or zone == zonas[3]:
            buy((prices["PawPatrol Soundtrack"]+1500))
        elif zone == "5" or zone == zonas[4]:
            buy((prices["PawPatrol Soundtrack"]+2000))
            
    start = input("¿Deseas hacer otra compra? s/n: ")