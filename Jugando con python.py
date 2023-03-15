print("Programa de evaluacion de notas de alumnos")

Lista_de_alumnos = []
nombre_alumno=str(input("Introduce el nombre del alumno: "))
nota_alumno=int(input("Introduce la nota del alumno: "))
Lista_de_alumnos.append(nombre_alumno)
def  evaluacion(nota):
    valoracion="aprobado"
    if nota<3:
        valoracion="suspenso"
    return valoracion

Evaluacion_alumno = {}
Evaluacion_alumno[nombre_alumno]=evaluacion(int((nota_alumno)))

while input("Va a introducir mas alumnos: ") == "si":
    nombre_alumno=input("Introduce el nombre del alumno: ")
    nota_alumno=input("Introduce la nota del alumno: ")
    Lista_de_alumnos.append(nombre_alumno)
    Evaluacion_alumno[nombre_alumno]=evaluacion(int((nota_alumno)))

print(Lista_de_alumnos)
print(Evaluacion_alumno)
