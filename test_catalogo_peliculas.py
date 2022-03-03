from Dominio.Peliculas import Pelicula
from Servicio.CatalogoPeliculas import  CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("Opciones: ")
        print("1-Agregar película")
        print("2-Listar peliculas")
        print("3-Eliminar catálogo de peliculas")
        print("4-Salir")
        opcion = int(input(f"Escribe tu opción de 1 a 4: "))
        if opcion == 1:
            nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            cp.listar_peliculas()
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.elminar_peliculas()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        opcion = None
else:
    print("Salimos del programa...")