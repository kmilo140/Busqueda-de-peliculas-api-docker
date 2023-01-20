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

<p align="center"> <img width="605" alt="image" src="https://user-images.githubusercontent.com/69985158/213351347-1b8a3fec-db95-402a-a735-fc76185440a9.png"></p> 

 <p align="center"> <img width="431" alt="image" src="https://user-images.githubusercontent.com/69985158/213351296-a88faaa5-d48f-45ec-be9c-b1e31c8c5ef9.png"></p> 

<p align="center"> <img width="585" alt="image" src="https://user-images.githubusercontent.com/69985158/213351401-14438e86-f491-40d4-a481-89f1291ceb3b.png"></p> 

<p align="center"> <img width="543" alt="image" src="https://user-images.githubusercontent.com/69985158/213351448-c3623d95-4f1c-435d-9fe7-d1db611fc621.png"></p> 

<p align="center"> <img width="406" alt="image" src="https://user-images.githubusercontent.com/69985158/213351489-14be0687-3c5d-4666-b22a-b41e30dffa6b.png"></p> 


Luego de completar el ETL y las funciones que se van a utilizar posteriormente en la API, debemos elaborar un archivo Dockerfile y requirements.txt, para la implementacion en la herramienta render.

<p align="center"> <img width="418" alt="image" src="https://user-images.githubusercontent.com/69985158/213348911-cc1ccd3a-c162-42ec-b617-3c6304daddfc.png"></p> 

En este punto ya se ha creado todos los archivos necesarios para nuestra app, a continuación subiremos este repositorio local en GitHub. 

<p align="center"> <img width="211" alt="image" src="https://user-images.githubusercontent.com/69985158/213349282-a2a17db3-fe5c-4d27-a7a6-460c8d016334.png"></p> 

<p align="center"> <img width="530" alt="image" src="https://user-images.githubusercontent.com/69985158/213349350-af14065a-d5f2-4ff1-8c4c-70c2428647c6.png"></p> 

+  **Deta**
 
Deta es una nube gratuita diseñada pensando en la experiencia del desarrollador y del usuario.
Nuestra misión es reducir drásticamente la brecha entre las ideas y las aplicaciones en la nube que funcionan.

Deta Micros es un tiempo de ejecución en la nube ligero pero escalable vinculado a un punto final HTTP. Están destinados a poner sus aplicaciones en funcionamiento increíblemente rápido. Concéntrese en escribir su código y Deta se encargará de todo lo demás.

Para crear un proyecto, vamos a nuestra página de inicio y seleccionamos “Nuevo proyecto”.
 
<p align="center"> <img width="343" alt="image" src="https://user-images.githubusercontent.com/69985158/213577352-4ecabc7d-a971-4006-8c74-65b7f05ffc61.png"></p> 

Luego, en nuestra máquina, abrimos una terminal y, dentro de la carpeta donde queremos colocar nuestro proyecto, creamos un nuevo micro.

deta new --python image_converter --project image_converter

Si todo está bien, veremos en nuestro terminal el mensaje “Creado con éxito un nuevo micro”, con la información de nuestro micro.

<p align="center"> <img width="224" alt="image" src="https://user-images.githubusercontent.com/69985158/213577631-fcbb7ccf-671f-437b-9305-5921be1f8d2a.png"></p> 

<p align="center"> <img width="718" alt="image" src="https://user-images.githubusercontent.com/69985158/213577789-45427365-85bb-4d62-8c0a-81c3972f2e12.png"></p> 

El deploy FastAPI en DETA esta realizado el link para entrar a nuestra API seria este https://i2sdty.deta.dev/docs.

+  **Render**

Para hacer el deploy de nuestra app en Render, es necesario elaborar un archivo Dockerfile. para que esta herramienta web puede levantar nuestra aplicación. es muy simple la realizar el deploy, una vez se tenga el repositorio en un GitHub, con los archivos necesarios. lo conectamos. y listo. la web levantara nuestra aplicación. 

<p align="center"> <img width="919" alt="image" src="https://user-images.githubusercontent.com/69985158/213584009-7ba16824-ae1c-424b-ada4-b971bc467498.png"></p> 

<p align="center"> <img width="932" alt="image" src="https://user-images.githubusercontent.com/69985158/213584158-3ea2881f-57d2-4e3d-9daf-9a3971cfadd5.png"></p> 

y listo ya se tendrá disponible la app en Render. el link de la app es https://fastapi-b1fr.onrender.com.


🦾 con ❤️ por [Camilo Ardila🤖](https://github.com/kmilo140) 😊  
