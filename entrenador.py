class Entrenador:
    def __init__(self, id_entrenador, nombre, horario_entrenador):
        self.id_entrenador = id_entrenador
        self.nombre = nombre
        self.horario_entrenador = horario_entrenador.lower()  # Convertir a minúsculas para facilitar la comparación
        self.rutas_asignadas = []

    def asignar_ruta(self, ruta):
        if self.horario_entrenador == 'activo':
            if ruta not in self.rutas_asignadas:
                self.rutas_asignadas.append(ruta)
                return True
            else:
                print(f"La ruta {ruta} ya está asignada a este entrenador.")
        else:
            print("El horario del entrenador no está activo. No se puede asignar ruta.")
        return False

    def desasignar_ruta(self, ruta):
        if ruta in self.rutas_asignadas:
            self.rutas_asignadas.remove(ruta)
            print(f"La ruta {ruta} ha sido desasignada al entrenador {self.nombre}.")
            return True
        else:
            print(f"La ruta {ruta} no está asignada a este entrenador.")
        return False

    def __str__(self):
        return f"ID: {self.id_entrenador}, Nombre: {self.nombre}, Horario: {self.horario_entrenador}, Rutas Asignadas: {self.rutas_asignadas}"