import json

class RutaEntrenamiento:
    def __init__(self):
        self.datos_rutas = []

    def agregar_ruta(self):
        print("\nAgregar Ruta:")
        nombre = input("Ingrese el nombre de la ruta: ")
        tecnologias = input("Ingrese las tecnologías de la ruta (separadas por coma): ").split(',')
        duracion = self.input_entero("Ingrese la duración de la ruta en semanas: ")

        ruta = {
            "nombre": nombre,
            "tecnologias": tecnologias,
            "duracion": duracion
        }

        self.datos_rutas.append(ruta)
        self.guardar_datos()

        print(f"Ruta '{nombre}' agregada correctamente.")

    def ver_rutas(self):
        print("\nRutas Disponibles:")
        for ruta in self.datos_rutas:
            print(f"Nombre: {ruta['nombre']}, Tecnologías: {', '.join(ruta['tecnologias'])}, Duración: {ruta['duracion']} semanas")

    def guardar_datos(self):
        with open("rutas_data.json", "w") as archivo:
            json.dump(self.datos_rutas, archivo, indent=2)

    def cargar_datos(self):
        try:
            with open("rutas_data.json", "r") as archivo:
                self.datos_rutas = json.load(archivo)
        except FileNotFoundError:
            self.datos_rutas = []

    @staticmethod
    def input_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    ruta_entrenamiento = RutaEntrenamiento()
    ruta_entrenamiento.cargar_datos()

    ruta_entrenamiento.agregar_ruta()
    ruta_entrenamiento.ver_rutas()
