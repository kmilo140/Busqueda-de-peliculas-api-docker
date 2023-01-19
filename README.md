# Extracción, Transformación y compilación de una base de datos, implementando esto en una API para consultas.

En el siguiente proyecto, inicia con 4 diferentes archivos. A los cuales se le realizo primero un EDA, esto para explorar los datos recibidos. 

Posteriormente se realiza un proceso de ETL, donde se efectúa los cambios y normalizados necesario para la base de datos. 

Para realizar la API se utilizo la herramienta FastAPI. Que brinda una plataforma de fácil implementación. Por ultimo se utiliza la herramienta web Deta para disponer la app en la web.

Se utiliza también la herramienta render que utiliza un archivo Dockerfile para disponer la app en la web, esto como extra.

## Objetivo de trabajo 🚀

El proyecto consiste en realizar una ingesta de datos, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API.

Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

### Principales tecnologías utilizadas 📋

 + **Python**  
   - Pandas  
   - Numpy  
   - seaborn  
   - Chardet
   - matplotlib
   
  Python es un lenguaje de programación que te permite trabajar rápidamente e integrar sistemas de manera más efectiva.
  https://docs.python.org/3/   
  
  + **FastApi**  

 FastAPI es un marco web moderno, rápido (de alto rendimiento) para crear API con Python 3.7+ basado en sugerencias de tipo estándar de Python.  
 https://fastapi.tiangolo.com/  

 + **Uvicorn**

Uvicorn es una implementación de servidor web ASGI para Python.

Hasta hace poco, Python carecía de una interfaz mínima de servidor/aplicación de bajo nivel para marcos asíncronos. La especificación ASGI llena este vacío y significa que ahora podemos comenzar a crear un conjunto común de herramientas utilizables en todos los marcos asíncronos.    
https://www.uvicorn.org/   


### Plan de Acción ⚡

+ **Trabajo de ETL con Python** 

En primer lugar, importé las librerías Pandas (librería de Python especializada en la manipulación y el análisis de datos) y Numpy (librería que da soporte a una gran colección de funciones matemáticas de alto nivel, cuenta con una gran velocidad al estar escrito en su mayor parte en C). Luego realicé 
la carga de los datasets de Netflix, Amazon, Hulu, y Disney+ con Pandas, los mismos datasets cuentan con información de tanto películas como series durante los años en las plataformas anteriormente mencionadas.

Luego, corroboré cuantos valores faltantes se encuentran en cada columna y dependiendo del tipo de datos que se encuentran en la misma, trabajé de una forma distinta. Siempre buscando la mejor calidad en los datos en cuestión, ya que cuento con una metodología de trabajo en la que busco no eliminar las tablas
que tienen valores faltantes, ya que alguna de sus diversas filas pueden llegar a contar con información reelevante.

Luego de sobrellevar los problemas y una vez realizado el ETL, se comenzó a trabajar en las funciones requeridas para la API. Estas funciones son:

+ <img width="605" alt="image" src="https://user-images.githubusercontent.com/69985158/213351347-1b8a3fec-db95-402a-a735-fc76185440a9.png">

+ <img width="431" alt="image" src="https://user-images.githubusercontent.com/69985158/213351296-a88faaa5-d48f-45ec-be9c-b1e31c8c5ef9.png">

+ <img width="585" alt="image" src="https://user-images.githubusercontent.com/69985158/213351401-14438e86-f491-40d4-a481-89f1291ceb3b.png">

+ <img width="543" alt="image" src="https://user-images.githubusercontent.com/69985158/213351448-c3623d95-4f1c-435d-9fe7-d1db611fc621.png">

+ <img width="406" alt="image" src="https://user-images.githubusercontent.com/69985158/213351489-14be0687-3c5d-4666-b22a-b41e30dffa6b.png">


Luego de completar el ETL y las funciones que se van a utilizar posteriormente en la API, debemos elaborar un archivo Dockerfile y requirements.txt, para la implementacion en la herramienta render.

<img width="418" alt="image" src="https://user-images.githubusercontent.com/69985158/213348911-cc1ccd3a-c162-42ec-b617-3c6304daddfc.png">

En este punto ya se ha creado todos los archivos necesarios para nuestra app, a continuación subiremos este repositorio local en GitHub. 

<img width="211" alt="image" src="https://user-images.githubusercontent.com/69985158/213349282-a2a17db3-fe5c-4d27-a7a6-460c8d016334.png">

<img width="530" alt="image" src="https://user-images.githubusercontent.com/69985158/213349350-af14065a-d5f2-4ff1-8c4c-70c2428647c6.png">

Link del repositorio https://github.com/kmilo140/PI06



## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
