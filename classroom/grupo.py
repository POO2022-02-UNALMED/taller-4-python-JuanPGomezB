

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, as1, as2, as3):
        # for x in args.values():
        #     self._asignaturas.append(Asignatura(x))
        self._as1=as1
        self._as2=as2
        self._as3=as3
        self._asignaturas = []
        self._asignaturas.append(Asignatura(self._as1))
        self._asignaturas.append(Asignatura(self._as2))
        self._asignaturas.append(Asignatura(self._as3))

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista + [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        cadena="Grupo de estudiantes: "+self._grupo
        return cadena 