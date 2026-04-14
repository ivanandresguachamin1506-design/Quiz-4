def calcular_daño(ataque, defensa):
    daño = ataque - defensa
    if daño < 0:
        return 0
    return daño

def aplicar_daño(hp_actual, daño):
    nuevo_hp = hp_actual - daño
    if nuevo_hp < 0:
        return 0
    return nuevo_hp
def mostrar_estado(nombre, hp, hp_max=100):
    print(f"{nombre}: {hp}/{hp_max}")

def realizar_ataque(atacante, defensor, daño):
    print(f"{atacante} ataca a {defensor} por {daño} de daño!")

hp_heroe = 100
hp_enemigo = 50

print("Estado inicial:")
mostrar_estado("Héroe", hp_heroe)
mostrar_estado("Enemigo", hp_enemigo)

print("\nPrimer ataque:")

daño_heroe = calcular_daño(ataque=25, defensa=10)

realizar_ataque("Héroe", "Enemigo", daño_heroe)

hp_enemigo = aplicar_daño(hp_enemigo, daño_heroe)

mostrar_estado("Enemigo", hp_enemigo)

print("\nSegundo ataque:")

realizar_ataque("Héroe", "Enemigo", daño_heroe)
hp_enemigo = aplicar_daño(hp_enemigo, daño_heroe)

print("\nEstado final:")
mostrar_estado("Enemigo", hp_enemigo)
