import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
# import time

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
    Función que hará una llamada a la API y de aquí se desprenderá el resto del programa.
    Se repetirá la pregunta del pokémon si no se encuentra (estatus 404) y se cerrará el programa si nos arroja una respuesta diferente.
    """
    # CICLO PARA SEGUIR PREGUNTANDO EL NOMBRE DE UN POKÉMON EN CASO DE QUE OBTENGAMOS UNA RESPUESTA DIFERENTE AL ESTATUS 200.
    while True:
        pokemon = input("Escribe el nombre de un Pokémon: ").lower()
        url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
        respuesta = requests.get(url)
        # VALIDAR SI SE ENCONTRÓ EL POKÉMON
        if respuesta.status_code == 200:
            print("¡GENIAL!. Pokémon encontrado.")
            # GUARDAMOS LOS DATOS DEL POKÉMON EN LA VARIABLE "datos"
            datos = respuesta.json()
            # LLAMADA DE LA FUNCIÓN "muestra_poke()" ENVIAMOS DE PARAMETROS LOS DATOS DEL POKÉMON
            muestra_poke(datos)
            break
        # ELIF PARA QUE SI NO ENCONTRÓ EL POKÉMON, EL USUARIO VUELVA A INTRODUCIR UN NOMBRE DE OTRO POKÉMON.
        elif respuesta.status_code == 404:
            print("Pokémon no encontrado, lo siento. \nPero puedes emprender una busqueda y nombrar así a un pokémon nunca antes visto. \nVuelve a intentar con otro Pokémon.")
        else:
            print("Ocurrió un error.")
            exit()
            
def muestra_poke(datos):
    """
    Función que nos mostrará la imagen del Pokémon y algunas estadísticas (peso, tamaño, movimientos, habilidades y tipos.)
    También hara la llamada de una función para guardar la información del pokémon.
    """
    # MANEJO DE EXCEPCIONES POR SI NO HAY UNA IMAGEN DEL POKÉMON.
    try:
        url_imagen = datos["sprites"]["front_default"]
        # GUARDAMOS LA IMAGEN EN LA VARIABLE "imagen" utilizando la librería "PIL" Y EL MÓDULO "Image" y lad funciones "open" y "urlopen"
        imagen = Image.open(urlopen(url_imagen))
    except:
        print("El Pokémon no tiene imagen.")
    # GUARDAMOS LOS DATOS QUE NOS INTERESAN EN VARIABLES.
    nombre = datos["name"]
    peso = datos["weight"]
    tamano = datos["height"]
    #LLAMAMOS A UNA FUNCIÓN PARA NO REPETIR EN CÓDIGO LA CREACIÓN DE LAS LISTAS CON LOS MOVIMIENTOS, HABILIDADES Y SU TIPO O TIPOS DEL POKÉMON.
    movimientos = creaLista(datos["moves"], "move", "name")
    habilidades = creaLista(datos["abilities"], "ability", "name")
    tipos = creaLista(datos["types"], "type", "name")
    
    #CREACIÓN DE NUESTRO DICCIONARIO.
    datosPoke = {
        "Nombre":nombre, 
        "url_imagen" : url_imagen, 
        "Peso" : peso, 
        "Tamaño" : tamano, 
        "Movimientos" : movimientos, 
        "Habilidades" : habilidades, 
        "Tipos" : tipos
        }

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
    # LLAMAMOS A LA FUNCIÓN "guarda_poke()" con el diccionario de los datos del pokémon como parámetro.
    guarda_poke (datosPoke)
    
def guarda_poke(datos):
    """
    Función que nos guargará el Pokémon en un archivo .JSON.
    En caso de que el pokémon ya se encuentre en nuestro "pokédex" ya no lo guardaremos.
    """
    #Manejo de errores por si no tenemos creado el archivo "pokemones.json
    try:
        with open ("ProyectoM4/pokédex/pokemones.json", "r") as f_pokemones:
            datosPokemones = json.load(f_pokemones)
            if len(datosPokemones["Pokemon"]) == 0:
                datosPokemones["Pokemon"].append(datos)
            else:
                for i in range(len(datosPokemones["Pokemon"])):
                    if (datos["Nombre"]) in (datosPokemones["Pokemon"][i]["Nombre"]):
                        print("Este Pokémon ya está en tu pokédex")
                        break
                    else:
                        datosPokemones["Pokemon"].append(datos)
                        with open ("ProyectoM4/pokédex/pokemones.json", "w") as f_pokemones:
                            json.dump(datosPokemones, f_pokemones)
                            print("Pokémon guardado exitosamente.")
    except FileNotFoundError:
        with open ("ProyectoM4/pokédex/pokemones.json", "w") as f_pokemones:
            datosPokemones = {}
            datosPokemones["Pokemon"] = []  
            datosPokemones["Pokemon"].append(datos)
            json.dump(datosPokemones, f_pokemones) 
            print("Pokémon guardado exitosamente.")

# IMPRESIÓN DE BIENVENIDA AL PROGRAMA
print ("""Bienvenido a tu Pokédex by Olaf.
Disfruta de tu búsqueda.\n""")

# LLAMADA DE LA FUNCIÓN "llama_api()" PARA COMENZAR EL PROGRAMA.
llama_api()