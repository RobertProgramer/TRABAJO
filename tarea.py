def agregar2():
    nombre=input("Nombre del funcionario >> ")
    cargo=input("Cargo del funcionario >> ")
    salario=float(input("Salario del funcionario >> "))
    agregar['nombre']=nombre
    agregar['cargo']=cargo
    agregar['salario']=salario
    funcionario.append(agregar)
    return True

def eliminar():
    print("Digite porque medio desea eliminar\n")
    opcion=int(input("[1] - por posicion, [2] - cancelar>>>"))
    if opcion==1:
        z=1
        for x in funcionario:
            print(f" {z} - {x}")
            z=z+1
        n1=int(input("Que posicion desea eliminar >>"))
        if n1>len(funcionario):
            print("esa porsicion no existe")
            return True
        elif n1=="":
            print("esa porsicion no existe")
            return True
        else:
            del funcionario[n1-1]
    elif opcion==2:
        return True
    else:
        input("Ese valor no existe, Enter para continuar...")
        return True

def buscar():
    n1=input("Digita el nombre a buscar >>")
    for key in funcionario:
        N2=key['nombre']
        if N2==n1:
            h=1
            break
    if h==1:
        print(f"EL funcionario {n1} si existe")
    else: 
        print(f"EL funcionario {n1} no existe")
    input("\npulsa Enter para continuar")


funcionario=[]
while True:
    print ("Selecciona una opción")
    print ("1 - Agregar Funcionario")
    print ("2 - Mostrar Funcionario")
    print ("3 - ELiminar Funcionario")
    print ("4 - Buscar Funcionario")
    print ("0 - salir\n")
    agregar={}
    opcion = input(">> ")

    if opcion=="1":
        agregar2()
    elif opcion=="2":
        if funcionario==[]:
            input("La lista esta Vacia \n Enter para continuar..")
        else:
            for x in funcionario:
                print(x)
            input("\npulsa Enter para continuar")
    elif opcion=="3":
        if funcionario==[]:
            input("La lista esta Vacia \n Enter para continuar..")
        else:
            eliminar()
    elif opcion=="4":
        if funcionario==[]:
            input("La lista esta Vacia \n Enter para continuar..")
        else:
            buscar()
    elif opcion=="0":
        break
    else:
        print ("Introduce un numero entre 0 y 4")

