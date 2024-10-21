import requests
from PIL import Image
from io import BytesIO
import os
import json #Se importan librerias para el guardado de imagenes y el archivo json

def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]
        tipos = [tipo['type']['name'] for tipo in datos['types']]
        peso = datos['weight']
        tamano = datos['height']
        imagen_url = datos['sprites']['front_default']

        return {
            'nombre': datos['name'],
            'habilidades': habilidades,
            'tipos': tipos,
            'peso': peso,
            'tamano': tamano,
            'imagen_url': imagen_url
        }
    else:
        return None

def mostrar_guardar_imagen(imagen_url, nombre):
    respuesta = requests.get(imagen_url)
    imagen = Image.open(BytesIO(respuesta.content))
    imagen.show()
    
    # Guardar imagen en la carpeta 'pokedex_imagenes'
    carpeta = 'pokedex_imagenes'
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    ruta_imagen = os.path.join(carpeta, f"{nombre}.png")
    imagen.save(ruta_imagen)
 # Guardar datos en la carpeta 'pokedex_datos'
def guardar_datos_json(pokemon, carpeta='pokedex_datos'):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    ruta_archivo = os.path.join(carpeta, f"{pokemon['nombre']}.json")
    with open(ruta_archivo, 'w') as archivo:
        json.dump(pokemon, archivo, indent=4)

# Pedir al usuario el nombre del Pokemon
nombre_pokemon = input("Introduce el nombre del Pokemon: ")
pokemon = obtener_datos_pokemon(nombre_pokemon)

if pokemon:
    print(f"Nombre: {pokemon['nombre']}")
    print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
    print(f"Tipos: {', '.join(pokemon['tipos'])}")
    print(f"Peso: {pokemon['peso'] / 10} kg")  # Convertir el peso a kg
    print(f"Tamano: {pokemon['tamano'] / 10} m")  # Convertir el tamaño a metros
    mostrar_guardar_imagen(pokemon['imagen_url'], pokemon['nombre'])
    guardar_datos_json(pokemon)
else:
    print("Pokemon no encontrado")
