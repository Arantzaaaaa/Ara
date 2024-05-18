def contar_palabras(archivo):
    with open(archivo,'r') as file:
       contenido= file.read()
       palabras= contenido.split()
       num_palabras=len(palabras)
    return num_palabras

#programa principal


archivo= 'Escritorio/palabras.txt'
total_palabras=contar_palabras(archivo)
print("las palabras son", total_palabras)
