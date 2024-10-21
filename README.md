# Pokedex
# Para esta pokedex utilice las librerias pillow, os, request y json la primera para el manejo de imagenes de abrir y guardarlas, os para el manejo de archivos y crear una carpeta, 
# Requests la utilice para la solicitud a la pokeapi y json para guardar la informacion del pokemon solicitado por el usuario.
# La funcion obtener_datos_pokemon(nombre) hace una solicitud a la pokeapi para obtener los datos del pokémon y devuelve un diccionario con sus habilidades, tipos, peso, tamaño y url de la imagen.
# mostrar_guardar_imagen(imagen_url, nombre) descarga y muestra la imagen del Pokémon, luego la guarda en la carpeta pokedex_imagenes.
# guardar_datos_json(pokemon, carpeta) guarda los datos del pokemon en un archivo json en la carpeta pokedex_datos.
# Se pide al usuario que ingrese el nombre del pokemon, se obtienen los datos del pokemon usando obtener_datos_pokemon si se encuentran datos del pokemon, se muestran sus habilidades, tipos, peso y tamaño, y se guarda y muestra su imagen.
# También se guarda la información del pokemon en un archivo json en la carpeta especificada.
