import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json

def creaLista(datos, llave, nombre):
    """
    Función que crea una lista a partir de ciertos datos recibidos.
    """
    lista = []
    for i in range(len(datos)):
        dato = datos[i][llave][nombre]
        lista.append(dato)
    return lista

# def impresión ():

def llama_api ():
    """
    Función que hará una llamada a la API.
    """
    while True:
        pokemon = input("Escribe el nombre de un Pokémon: ").lower()
        url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("¡GENIAL!. Pokémon encontrado.")
            datos = respuesta.json()
            muestra_poke(datos)
            break
        elif respuesta.status_code == 404:
            print("Pokémon no encontrado, lo siento. \nPero puedes emprender una busqueda y nombrar así a un pokémon nunca antes visto. \nVuelve a intentar con otro Pokémon.")
        else:
            print("Ocurrió un error.")
            exit()
            
def muestra_poke(datos):
    """
    Función que nos mostrará la imagen del Pokémon y algunas estadísticas (peso, tamaño, movimientos, habilidades y tipos.)
    """
    try:
        url_imagen = datos["sprites"]["front_default"]
        imagen = Image.open(urlopen(url_imagen))
    except:
        print("El Pokémon no tiene imagen.")

    peso = datos["weight"]
    tamaño = datos["height"]
    movimientos = creaLista(datos["moves"], "move", "name")
    habilidades = creaLista(datos["abilities"], "ability", "name")
    tipos = creaLista(datos["types"], "type", "name")
    
    # datosPoke = []
    # datosPoke.append()

    guarda_poke (datos)
    i = 1
    print("Movimientos: ")
    for movimiento in movimientos:
        print(f"{i}.- {movimiento}")
        i += 1

    print("Habilidades: ")
    i = 1
    for habilidad in habilidades:
        print(f"{i}.- {habilidad}")
        i += 1
    print(tipos)

    print(f"{peso} hectogramos o {peso*100} gramos.")
    print(f"{tamaño} decimetros o {tamaño*10} centimetros.")


    plt.title(datos["name"].title()) 
    imgplot = plt.imshow(imagen)
    plt.show()
    
def guarda_poke(datos):
    """
    Función que nos guargará el Pokémon en un archivo .JSON
    """
    with open ("ProyectoM4/pokédex/pokemones.json", "w") as f_pokemones:
        json.dump(datos, f_pokemones)

print ("""Bienvenido a tu Pokédex by Olaf.
Disfruta de tu búsqueda.\n""")

llama_api()