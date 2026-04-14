import random
from datetime import datetime

def generar_nombre():
    nombres = ["Arthas", "Luna", "Drako", "Eldrin", "Kael", "Fracois", "Marco", "Ragvaldd", "Enki"]
    return random.choice(nombres)

def generar_clase():
    clases = ["Guerrero", "Mago", "Arquero", "Asesino", "Paladín", "Mago oscuro"]
    return random.choice(clases)

def generar_hp():
    return random.randint(80, 120)

def mostrar_fecha():
    fecha_actual = datetime.now()
    print("Fecha de la aventura:")
    print(f"Día: {fecha_actual.day}, Mes: {fecha_actual.month}, Año: {fecha_actual.year}")
    print("-" * 40)

if __name__ == "__main__":
    mostrar_fecha()
    
    print("Héroes generados:\n")
    for i in range(1, 4):
        nombre = generar_nombre()
        clase = generar_clase()
        hp = generar_hp()
        print(f"Héroe {i}:")
        print(f"Nombre: {nombre}")
        print(f"Clase: {clase}")
        print(f"HP: {hp}")
        print("-" * 20)