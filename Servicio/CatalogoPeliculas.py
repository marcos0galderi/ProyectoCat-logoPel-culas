import os
class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print(f"Catálogo de películas".center(50,"-"))
            print(archivo.read())
    @classmethod
    def elminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f"Archivo {cls.ruta_archivo} eliminado")
