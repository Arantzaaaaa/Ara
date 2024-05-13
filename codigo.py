#Autoras: Ceron Urbina Itzel Anaid, Luna Colula Nicole, Sanchez Ramirez Arantza
import os
import subprocess

def ejecutar_comando(comando):
    subprocess.run(comando, shell=True)

def mostrar_historial():
    subprocess.run("history", shell=True)

def menu():
    print("1. Copiar archivo 'holamundo.txt'a la carpeta Python")
    print("2. Eliminar carpeta 'Python'")
    print("3. Eliminar archivo llamado 'Archivo.txt'")
    print("4. Cambiar nombre del archivo 'holamundo.txt' a 'holis.txt'")
    print("5. Salir ")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            ejecutar_comando("cp holamundo.txt 'Python'")
        elif opcion == '2':
            ejecutar_comando("rm -r Python")   
        elif opcion == '3':
            ejecutar_comando("rm Archivo.txt")
        elif opcion == '4':
            ejecutar_comando("mv holamundo.txt holis.txt")  
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida. ")

if __name__ == "__main__":
    main()
