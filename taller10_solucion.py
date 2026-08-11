def gestionar_curso():
    opcion = 0
    notas = []
    
    while opcion != 4:
        print("=================================")
        print("    SISTEMA DE GESTIÓN TALLER 10   ")
        print("=================================")
        print("1. Registrar calificaciones")
        print("2. Calcular promedio general")
        print("3. Mostrar estado del curso")
        print("4. Salir")
        
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
            continue
            
        if opcion == 1:
            try:
                total_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
                if total_estudiantes > 0:
                    notas = []
                    for i in range(total_estudiantes):
                        nota = float(input(f"Ingrese la nota del estudiante {i + 1} (0 - 20): "))
                        while nota < 0 or nota > 20:
                            nota = float(input(f"Nota inválida. Reingrese la nota del estudiante {i + 1} (0 - 20): "))
                        notas.append(nota)
                    print("¡Notas registradas con éxito!\n")
                else:
                    print("Debe ingresar un número mayor a cero.\n")
            except ValueError:
                print("Valor ingresado incorrecto.\n")
                
        elif opcion == 2:
            if len(notas) > 0:
                promedio = sum(notas) / len(notas)
                print(f"El promedio general del curso es: {promedio:.2f}\n")
            else:
                print("No existen registros previos. Seleccione la opción 1 primero.\n")
                
        elif opcion == 3:
            if len(notas) > 0:
                promedio = sum(notas) / len(notas)
                if promedio >= 14:
                    print(f"El curso se encuentra en un nivel: SATISFACTORIO (Promedio: {promedio:.2f})\n")
                else:
                    print(f"El curso requiere: REFUERZO ACADÉMICO (Promedio: {promedio:.2f})\n")
            else:
                print("No hay datos suficientes para evaluar el estado.\n")
                
        elif opcion == 4:
            print("Saliendo del sistema... ¡Hasta luego!")
        else:
            print("Opción inválida. Por favor, elija entre 1 y 4.\n")

if __name__ == "__main__":
    gestionar_curso()