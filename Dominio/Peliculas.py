class Pelicula:
    def __init__(self, nombrepelicula):
        self._nombrepelicula = nombrepelicula
    def __str__(self):
        return f" Aquí esta la película: {self._nombrepelicula}"
    @property
    def nombre(self):
        return self._nombrepelicula
    @nombre.setter
    def nombre(self, nombre):
        self._nombrepelicula
