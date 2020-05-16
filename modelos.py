class Alumno:
    
    def __init__(self, nombre, codigo_alumno):
        self.nombre = nombre
        self.codigo_alumno = codigo_alumno
        self.notas = []
        self._promedio = 0

    @staticmethod
    def obtener_desde_consola():
        nombre = input("Ingrese el nombre del alumno: ")
        codigo_alumno = input("Ingrese el codigo del alumno: ")
        return Alumno(nombre, codigo_alumno)

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_promedio(self):
        if len(self.notas) > 0:
            self._promedio = sum(self.notas) // len(self.notas)
        return self._promedio

    def __str__(self):
        nombre = f"Nombre del Alumno: {self.nombre}"
        codigo = f"Codigo del Alumno: {self.codigo_alumno}"
        notas_a_imprimir = ""
        for i, nota in enumerate(self.notas):
            notas_a_imprimir += f"Nota #{i+1} : {nota}\n"
        if len(self.notas) == 0:
            notas_a_imprimir = "El alumno no tiene notas registradas."
        promedio = f"Promedio del Alumno: {self.obtener_promedio()}"
        return "\n".join((nombre, codigo, notas_a_imprimir, promedio))


class Docente:
    
    def __init__(self, nombre, codigo_docente):
        self.nombre = nombre
        self.codigo_docente = codigo_docente

    @staticmethod
    def obtener_desde_consola():
        nombre = input('Ingresar el nombre del docente: ')
        codigo = input('Ingresar el codigo del docente: ')
        return Docente(nombre, codigo)

    def __str__(self):
        nombre = f"Nombre del docente: {self.nombre}"
        codigo = f"Codigo del docente: {self.codigo_docente}"
        return "\n".join((nombre, codigo))

