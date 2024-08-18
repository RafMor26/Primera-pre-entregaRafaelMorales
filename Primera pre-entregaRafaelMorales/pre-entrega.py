

def agregar_usuario(BD):
    while True:
        usuario = input('Ingrese su USUARIO: ')
        contrasena = input('Ingrese CONTRASEÑA: ')
        confirmacion = input('Ingrese de nuevo su CONTRASEÑA para confirmar: ')

        
        while  contrasena != confirmacion:
            print('### NO INGRESASTE BIEN LA CONFIRMACION ###')
            confirmacion = input('Ingrese de nuevo su CONTRASEÑA: ')
        else:
            print('USUARIO y CONTRASEÑA confirmados')
                   
        BD[usuario] = contrasena

        while True:
            continuar = input('¿Deseas agregar otro USUARIO? (SI/NO): ')
            if continuar == 'SI':
                break  
            elif continuar == 'NO':
                return  
            else:
                print('Por favor, ingrese una opcion valida: "SI" para si o "NO" para no en MAYUSCULAS')
        
             

def leerBD(BD):
    print('La informacion almacenada en la base de datos es: ')
    for i in BD:
        print(f'USUARIO: " {i} " CONTRASEÑA: " {BD[i]} "')



base = {}

# agregar_usuario(base)
# leerBD(base)











