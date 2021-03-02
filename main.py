#examen Liliana Esmeral
#Punto 1
def descuentoPorKilos(kilos):
    print(kilos)
    if (kilos >= 0) & (kilos < 2):
        print("El descuento es del 0%")
    elif (kilos >= 2) & (kilos < 5):
        print("El descuento es del 10%")
    elif (kilos >= 5) & (kilos < 10):
        print("El descuento es del 15%")
    elif kilos >= 10:
        print("El descuento es del 20%")

#Punto 2
def valorFinal(neto, clave):
    if clave == "010":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.2)}")
    elif clave == "020":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.4)}")
    elif clave == "030":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.55)}")
    elif clave == "040":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.75)}")

#Punto 3
def proveedorEstereos(marca, precio):
    precio_desc = precio
    if precio >= 4000:
        precio_desc = precio_desc - (precio_desc * 0.2)
    total = precio_desc + (precio_desc*0.3)
    if marca == "NOSY":
        total = total - (total*0.1)
    print(f"El monto total que debe pagar el cliente es: {total}")

#Punto 4
def reforestacionGobColombiano(hectareas):
    if hectareas > 5:
        pino = hectareas*0.8
        oyamel = hectareas*0.15
        cedro = hectareas*0.5
    else:
        pino = hectareas*0.45
        oyamel = hectareas*0.25
        cedro = hectareas*0.3
    print(f"Se sembrarán {pino} hectareas de Pino, {oyamel} hectareas de Oyamel y {cedro} hectareas de cedro")

#Punto 5
def numerosDiferentes(n1, n2, n3):
    if (n1 > n2) & (n1 > n3):
        print(f"El mayor es n1: {n1}")
    elif (n2 > n1) & (n2 > n3):
        print(f"El mayor es n2: {n2}")
    elif (n3 > n1) & (n3 > n2):
        print(f"El mayor es n3: {n3}")
    else:
        print("Los números son iguales")

#Prueba método 1
descuentoPorKilos(1)
descuentoPorKilos(2)
descuentoPorKilos(8)
descuentoPorKilos(25)
#Prueba método 2
valorFinal(100000,"010")
valorFinal(100000,"020")
valorFinal(100000,"030")
valorFinal(100000,"040")
valorFinal(100000,"050") #No imprime nada
#Prueba método 3
proveedorEstereos("NOSY",100000)
proveedorEstereos("NOSY",2000)
proveedorEstereos("YAMAHA",100000)
#Prueba método 4
reforestacionGobColombiano(5)
reforestacionGobColombiano(4)
#Prueba método 5
numerosDiferentes(95,34,29)
numerosDiferentes(12,94,29)
numerosDiferentes(95,34,290)

