# Extracción, Transformación y compilación de una base de datos, implementando esto en una API para consultas.

![Alt Text](https://labibliotecadealexandria.com/wp-content/uploads/2022/07/Etapas-do-Data-Science-para-aplicar-na-sua-empresa.gif)

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

## Video explicativo 📺

[![Alt text](https://img.youtube.com/vi/jtLWpcPDXrg/0.jpg)](https://youtu.be/jtLWpcPDXrg)


### Principales tecnologías utilizadas 📋

 + **Python**  
   - Pandas  
   - Numpy  
   - seaborn  
   - matplotlib
   
  Python es un lenguaje de programación que te permite trabajar rápidamente e integrar sistemas de manera más efectiva.
  https://docs.python.org/3/   
  
  + **Docker**
  
  nos va a permitir crear aplicaciones que vamos a poder transportar de un entorno a otro fácilmente, que van a ejecutarse en un contenedores aislados dentro de       nuestro sistema operativo y que, además, se van a comportar exactamente igual en cualquier máquina con Docker instalado.
  
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

Luego de sobrellevar los problemas y una vez realizado el ETL, se comenzó a trabajar en las funciones requeridas para la API. 


Luego de completar el ETL y las funciones que se van a utilizar posteriormente en la API, debemos elaborar un archivo Dockerfile y requirements.txt, para la implementacion en la herramienta render.

En este punto ya se ha creado todos los archivos necesarios para nuestra app, a continuación subiremos este repositorio local en GitHub. 



+  **Deta**
 
Deta es una nube gratuita diseñada pensando en la experiencia del desarrollador y del usuario.
Nuestra misión es reducir drásticamente la brecha entre las ideas y las aplicaciones en la nube que funcionan.

El deploy FastAPI en DETA esta realizado el link para entrar a nuestra API sería este https://i2sdty.deta.dev/docs.

+  **Render**

Para hacer el deploy de nuestra app en Render, es necesario elaborar un archivo Dockerfile. Para que esta herramienta web puede levantar nuestra aplicación. es muy simple la ejecutar el deploy, una vez se tenga el repositorio en un GitHub, con los archivos necesarios. lo conectamos. y listo. la web levantará nuestra aplicación. 

Y listo ya se tendrá disponible la app en Render. el link de la app es https://fastapi-b1fr.onrender.com.




🦾 con ❤️ por [Camilo Ardila🤖](https://github.com/kmilo140) 😊  
