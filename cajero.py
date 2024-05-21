import threading
import time
import random
 
database_semaphore = threading.Semaphore(1)
 
def acceso_base_de_datos(cajero_id):
    print(f"Cajero {cajero_id} intentando acceder a la base de datos")
    with database_semaphore:
        print(f"Cajero {cajero_id} ha adquirido acceso a la base de datos")
        tiempo_acceso = random.uniform(1, 3)
        time.sleep(tiempo_acceso)
        print(f"Cajero {cajero_id} ha liberado la base de datos después de {tiempo_acceso:.2f} segundos")
 
cajeros = []
for i in range(5):
    cajero = threading.Thread(target=acceso_base_de_datos, args=(i,))
    cajeros.append(cajero)
    cajero.start()
 
for cajero in cajeros:
    cajero.join()
