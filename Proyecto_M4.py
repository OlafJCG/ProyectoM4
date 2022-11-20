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

def impresion_listas (lista):
    """
    Función que imprime listas en forma enumerada con un ciclo for.
    """
    i = 1
    for dato in lista:
        print(f"{i}.- {dato}")
        i += 1

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
    nombre = datos["name"]
    peso = datos["weight"]
    tamano = datos["height"]
    movimientos = creaLista(datos["moves"], "move", "name")
    habilidades = creaLista(datos["abilities"], "ability", "name")
    tipos = creaLista(datos["types"], "type", "name")
    
    datosPoke = {
        "Nombre":nombre, 
        "url_imagen" : url_imagen, 
        "Peso" : peso, 
        "Tamaño" : tamano, 
        "Movimientos" : movimientos, 
        "Habilidades" : habilidades, 
        "Tipos" : tipos
        }
    guarda_poke (datosPoke)

    # IMPRESIÓN DE LA INFORMACIÓN DEL POKÉMON
    print("Movimientos: ")
    impresion_listas (movimientos)
    print("Habilidades: ")
    impresion_listas (habilidades)
    if len(tipos) == 1:
        print("Tipo")
    else:
        print("Tipos")
    impresion_listas(tipos)
    print(f"{peso} hectogramos.")
    print(f"{tamano} decimetros.")

    # TÍTULO CON CADENA FORMATEADA PARA LA IMAGEN DEL POKÉMON
    plt.title(nombre.title()) 
    # ESTAS LÍNEAS NOS MUESTRAN LA IMAGEN DEL POKÉMON
    imgplot = plt.imshow(imagen)
    plt.show()
    
def guarda_poke(datos):
    """
    Función que nos guargará el Pokémon en un archivo .JSON
    """
    #Manejo de excepciones por si no tenemos creado el archivo "pokemones.json
    try:
        with open ("ProyectoM4/pokédex/pokemones.json", "r") as f_pokemones:
            datosPokemones = json.load(f_pokemones)
    except FileNotFoundError:
        with open ("ProyectoM4/pokédex/pokemones.json", "w") as f_pokemones:
            datosPokemones = {}
            datosPokemones["Pokemon"] = []     

    for i in range(len(datosPokemones["Pokemon"])):
        if (datos["Nombre"]) in (datosPokemones["Pokemon"][i]["Nombre"]):
            print("Este Pokémon ya está en tu pokédex")
            break
        else:
            datosPokemones["Pokemon"].append(datos)
        

    with open ("ProyectoM4/pokédex/pokemones.json", "w") as f_pokemones:
        json.dump(datosPokemones, f_pokemones)

print ("""Bienvenido a tu Pokédex by Olaf.
Disfruta de tu búsqueda.\n""")

llama_api()