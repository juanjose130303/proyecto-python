class Camper:
    def __init__(self, nro_identificacion, nombre, apellidos, direccion, acudiente, nro_celular, nro_fijo, estado):
        self.nro_identificacion = nro_identificacion
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.acudiente = acudiente
        self.nro_celular = nro_celular
        self.nro_fijo = nro_fijo
        self.estado = estado
        self.notas = {
            'nota_teorica': 0,
            'nota_practica': 0,
            'quices': 0,
            'trabajos': 0
        }

    def registrar_camper(self):
        self.nro_identificacion = input("Número de identificación: ")
        self.nombre = input("Nombre: ")
        self.apellidos = input("Apellidos: ")
        self.direccion = input("Dirección: ")
        self.acudiente = input("Acudiente: ")
        self.nro_celular = input("Número de celular: ")
        self.nro_fijo = input("Número fijo: ")
        self.estado = "Inscrito"

    def actualizar_estado_aprobado(self):
        if self.estado == "Inscrito" and (self.notas['nota_teorica'] + self.notas['nota_practica']) >= 60:
            self.estado = "Aprobado"

    def registrar_prueba(self):
        if self.estado == "Inscrito":
            try:
                self.notas['nota_teorica'] = float(input("Ingrese la nota teórica: "))
                self.notas['nota_practica'] = float(input("Ingrese la nota práctica: "))
                self.notas['quices'] = float(input("Ingrese la nota de quices: "))
                self.notas['trabajos'] = float(input("Ingrese la nota de trabajos: "))
                self.actualizar_estado_aprobado()
                print("Notas registradas exitosamente.")
            except ValueError:
                print("Ingrese valores numéricos para las notas.")
        else:
            print("No se pueden registrar notas para campers no inscritos.")