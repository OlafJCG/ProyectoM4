<img src="https://pro-becas-images-s3.s3.eu-west-1.amazonaws.com/public_documents/79937fb7-1917-4660-b7e7-6d4b78dd0129" width="200">

# <p align = "center"> Proyecto M4 </p>
# <p align = "center"> CONSTRUYE UNA POKÉDEX. <br><p align="center">
  <p align = "center"><img src = "Imagenes/png-transparent-pokemon-red-and-blue-pokemon-firered-and-leafgreen-misty-kanto-pokedex-jinbe-gadget-electronic-device-pokemon.png" width="400">
</p >
<p align = "center"> -OLAF DE JESÚ CRUZ GUTIÉRREZ- </p>

<H1 align="center">¿Cómo lo hice? </H1>
<p>
Comencé probando la API en un API tester y familiarizandome con la estructura de los datos de los Pokémones (las unidades en que están expresados el peso por ejemplo) en la documentación de la API.
<p>Posteriormente comencé importando las librerías:
</p>
<p><img src = "Imagenes/Lib.PNG" width="400"> 
  <br>-Requests: La utilicé para hacer la petición a la API.
  <br>-matplotlib con pyplot para usar las funciones que permiten mostrarnos la imagen que obtendremos con otras librerías.
  <br>-El objeto "Image" del módulo "PIL" para abrir la imagen que obtenemos con la siguiente librería.
  <br>-El objeto "urlopen" de "request" que a su vez se encuentra dentro del módulo "urllib" para abrir la url ya extraída de la API.
  <br>-"json" para el manejo del archivo en formato JSON.
  <br>-"os" para verificar si el archivo JSON está vacío.
  
<p>
  Inicié con una impresión de un texto como bienvenida y posteriormente la llamada de la función que hace la llamada a la API y de esa función se desencadenan las demás.
  <br>Dentro de la función que hace la llamada a la API, hay condicionales.
<p>-Principalmente comprobamos que si la respuesta de la API es satisfactoria (200) procedamos al demás código.
  <br>-Si la respuesta arrojara un código "404" nos indica que el pokémon no fue encontrado, por lo que el programa volverá a preguntar por otro pokémon.
  <br>-Finalmente si arrojara un código diferente, se cerraría el programa.
  <p>Obteniendo un código "200" nos imprime un mensaje de que el pokémon ha sido encontrado y el paso siguiente sería llamar a la función que se encargará de imprimirnos la información del pokémon así como su imagen.
    <p>Dentro de la función de "muestra_poke(datos)" trabajamos con los datos que obtuvimos de la API del Pokémon. Pero vamos a guardar solamente los que nos interesan (Nombre, URL de la imagen, la imagen, movimientos, habilidades, altura, peso y el tipo de pokémon). Igualmente crearemos un diccionario con los datos para guardarlos dentro del archivo "JSON", pero el uso del diccionario se usará en otra función. Por el momento lo último que hará esta función será imprimirnos la información que se extrajo del pokémon, así como mostrarnos la imagen del pokémon gracias a la librería "pyplot"
      <p>Ya dentro de la función "guarda_poke(datos)" trabajaremos con el diccionario que creamos. Pero antes haremos algunas validaciones para evitar la mayor cantidad de errores posibles por el momento con el manejo de un archivo "json". Validamos si hay un archivo "json" existente, si el archivo se encuentra vacío o si ya contiene el pokémon que estamos deseando guardar.
        </p>
<H2 align="center">Algunas pruebas. </H2>
<p align = "left"><img src = "Imagenes/no_encontrado.PNG" width="600">
  <br> Podemos ver el mensaje de bienvenida al programa, y una prueba de que el pokémon no se encuentra en la API. Así como también la pregunta de nueva cuenta para ingresar otro nombre de algún pokémon.
  <p align = "left"><img src = "Imagenes/encontrado.PNG" width="300"><img src = "Imagenes/encontrado1.PNG" width="200"><img src = "Imagenes/Figure_1.png" width="400">
  <br>    En este ejemplo podemos ver que el pokémon se encontró en la API y el programa nos imprimió los datos que nos interesaban, así como un mensaje de "Guardado exitoso".
    <p align = "left"><img src = "Imagenes/duplicado.PNG" width="300">
      <br>Y por último en este ejemplo podemos ver que se mostró la información del pokémon, pero se muestra el mensaje de que el pokémon ya se encuentra en nuestro "pokédex" y por lo tanto ya no se guarda.
