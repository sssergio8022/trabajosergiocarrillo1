import pandas as pd
import random

# Cargar datos desde el archivo CSV
df = pd.read_csv("pokemon.csv")

# Limpiar nombres de columnas
df.columns = df.columns.str.strip().str.lower()

# Convertir a lista de diccionarios
pokemon_list = df.to_dict(orient="records")

# Función para mostrar Pokémon disponibles
def mostrar_pokemon():
    print("\n📋 Lista de Pokémon:")
    for i, p in enumerate(pokemon_list):
        print(f"{i + 1}. {p['name']} ({p['type_1']}) - ATK: {p['attack']}, DEF: {p['defense']}, HP: {p['hp']}")

# Función para agregar un nuevo Pokémon
def agregar_pokemon():
    name = input( Nombre del Pokémon: ")
    tipo = input(" Tipo: ")
    attack = input("⚔ Ataque: ")
    defense = input("🛡 Defensa: ")
    hp = input(" HP: ")

    nuevo_pokemon = {"name": name, "type_1": tipo, "attack": attack, "defense": defense, "hp": hp}
    pokemon_list.append(nuevo_pokemon)
    print(f" {name} ha sido agregado a la lista.")

# Función para eliminar un Pokémon
def eliminar_pokemon():
    mostrar_pokemon()
    try:
        index = int(input("\n❌ Escribe el número del Pokémon a eliminar: ")) - 1
        if 0 <= index < len(pokemon_list):
            eliminado = pokemon_list.pop(index)
            print(f" {eliminado['name']} ha sido eliminado.")
        else:
            print(" Número inválido.")
    except ValueError:
        print(" Entrada no válida.")

# Función para escoger Pokémon y simular batalla
def batalla():
    if len(pokemon_list) < 2:
        print(" No hay suficientes Pokémon para una batalla.")
        return

    mostrar_pokemon()
    
    try:
        p1 = int(input("\n Escribe el número del primer Pokémon: ")) - 1
        p2 = int(input(" Escribe el número del segundo Pokémon: ")) - 1

        if p1 == p2:
            print(" No puedes elegir el mismo Pokémon.")
            return

        if 0 <= p1 < len(pokemon_list) and 0 <= p2 < len(pokemon_list):
            pokemon1 = pokemon_list[p1]
            pokemon2 = pokemon_list[p2]

            score1 = int(pokemon1["attack"]) + int(pokemon1["defense"]) + int(pokemon1["hp"]) + random.randint(0, 10)
            score2 = int(pokemon2["attack"]) + int(pokemon2["defense"]) + int(pokemon2["hp"]) + random.randint(0, 10)

            print(f"\n⚔ Batalla entre {pokemon1['name']} y {pokemon2['name']}!")
            print(f"{pokemon1['name']} (Puntos: {score1}) vs {pokemon2['name']} (Puntos: {score2})")

            if score1 > score2:
                print(f"\n ¡{pokemon1['name']} gana la batalla!")
            elif score1 < score2:
                print(f"\n ¡{pokemon2['name']} gana la batalla!")
            else:
                print("\n ¡Es un empate!")
        else:
            print(" Uno de los números es inválido.")
    except ValueError:
        print(" Entrada no válida.")

# Menú principal
while True:
    print("\n MENÚ DE POKÉMON ")
    print("1️⃣ Ver Pokémon disponibles")
    print("2️⃣ Agregar un nuevo Pokémon")
    print("3️⃣ Eliminar un Pokémon")
    print("4️⃣ Iniciar una batalla")
    print("5️⃣ Salir")

    opcion = input("🔹 Escoge una opción: ")

    if opcion == "1":
        mostrar_pokemon()
    elif opcion == "2":
        agregar_pokemon()
    elif opcion == "3":
        eliminar_pokemon()
    elif opcion == "4":
        batalla()
    elif opcion == "5":
        print(" ¡Hasta la próxima!")
        break
    else:
        print(" Opción no válida. Intenta otra vez.")
