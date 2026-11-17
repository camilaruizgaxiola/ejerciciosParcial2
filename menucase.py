nombre= []
producto= []
precio= []
serie= []
email= []
sucursal= []
cantidadProducto= []
opcion= 0

while True:  #aqui inicia mi ciclo
    print("bienvenido al sistema de productos e inventarios")
    print("--------- MENU PRINCIPAL ---------")
    print("1.registar producto")
    print("2.ver informacion del producto")
    print("3.borrar informacion del pructo")
    print("4.modificar informacion del producto")
    print("5.salir")
    print("---------------------------------")
    opcion=int(input("selecciona una opcion:"))

    match opcion:  
        case 1:
            nombre = input("Ingresa tu nombre:")
            producto = input("Ingresa tu producto: ")
            precio= int(input("Ingresa el precio: "))
            email = input("Ingresa tu correo: ")
            sucursal= input("Ingresa tu sucursal: ")
            cantidadProducto = input("Ingresa la cantidad de producto: ")
        case 2: 
            #print("nombre", nombre, "producto", product, "precio", price, "Serie", series, "correo", email, "sucursal", branch, 
            #"cantidadProducto", productQuantity)
            print("mostraste nombres")
        case 3:
            #nombre= ""
            #product= ""
            #price= ""
            #series= ""
            #email= ""
            #branch= ""
            #productQuantity= ""
            print("entraste a la opción 3")
        case 4:
            nombre.append(input("ingresa tu nombre"))
            product.append(input("ingresa el producto"))
            price.append(input("ingresa el precio"))
            serie.append(input/("ingresa la serie"))
            email.append(input("ingresa tu correo"))
            branch.append(input("ingresa la sucursal"))
            productQuantity.append(input("ingresa la cantidad del producto"))
        case 5:
            print=("¡HASTA LUEGO!")
            break
        case 6:
            print=("opcion no valida")