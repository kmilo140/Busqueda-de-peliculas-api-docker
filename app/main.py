from fastapi import FastAPI
import pandas as pd
import numpy as np



app = FastAPI()

@app.get("/")
def helloworld():
    return "Hello World"

'''
We load the csv with all the API data.
'''

data = pd.read_csv('https://raw.githubusercontent.com/kmilo140/PI06/master/Datasets/data_string.csv')

'''
Number of times a keyword appears in the title of movies/series, by platform.

'''
@app.get('/Número de veces que una palabra clave aparece en el título de películas/series, por plataforma')
def get_word_count(plataforma:str, palabra_clave:str):
    if plataforma in ["netflix", "amazon prime", "hulu", "disney plus"]:
        in_plat = data['id'].str.contains(plataforma[0])
        data_plat = data[in_plat]
        busqueda = data_plat['title'].str.contains(palabra_clave)
        return f'En la plataforma {plataforma} se encuentra que hay {busqueda.value_counts()[1]} titulos que coinciden con {palabra_clave}'
    else:
        return("Debe introducir una de estas opciones en plataforma netflix, amazon prime, hulu o disney plus")

'''
Number of films per platform with a score higher than XX in a given year.
'''
@app.get('/Número de películas por plataforma con una puntuación superior a XX en un año determinado.')
def get_score_count(plataforma:str, calificacion:int, anio:int):
    if plataforma in ["netflix", "amazon prime", "hulu", "disney plus"] and 1 < calificacion <= 100 and 1920 < anio < 2021:
        in_plat = data['id'].str.contains(plataforma[0])
        data_plat = data[in_plat]
        in_release = data_plat["release_year"] == anio
        data_plat_release = data_plat[in_release]
        in_type = data_plat_release["category"] == "movie"
        final = data_plat_release[in_type]
        respuesta = final.apply(lambda x: x['score'] > calificacion, axis=1).sum()
        return f'El numero de titulos en la plataforma {plataforma}, el año {anio} es {respuesta}'
    else:
        return("Debe introducir una de estas opciones en plataforma netflix, amazon prime, hulu o disney plus.  Valificacion entre 1 y 100.  Y anio entre 1920 a 2021")
'''
The second highest scoring film for a given platform, according to the alphabetical order of titles.
'''    
@app.get('/La segunda película más taquillera para una plataforma determinada, según el orden alfabético de los títulos')
def get_second_score(plataforma:str):
    if plataforma in ["netflix", "amazon prime", "hulu", "disney plus"]:
        in_plat = data['id'].str.contains(plataforma[0])
        data_plat = data[in_plat]
        in_type = data_plat["category"] == "movie"
        final = data_plat[in_type]
        respuesta = final.sort_values(['score','title'], ascending=[False, True])
        return f'La segunda película con mayor score para una plataforma {plataforma}, es {respuesta.iloc[1][3]} según el orden alfabético de los títulos.'
    else:
        return("Debe introducir una de estas opciones en plataforma netflix, amazon prime, hulu o disney plus")
'''
Longest running film by year, platform and length type.
'''
@app.get('/Película más longeva por año, plataforma y tipo de duración.')
def get_longest(plataforma:str, tipo_de_duracion:str, anio:int):
    if plataforma in ["netflix", "amazon prime", "hulu", "disney plus"] and tipo_de_duracion in["temporada", "minutos"] :
        tipo_de_duracion= "min"
        tipo_de_duracion= "season"        
        respuesta = data[(data['release_year'] == anio) & (data['id'].str.contains(plataforma[0])) & (data['duration_type'] == tipo_de_duracion) ]
        respuesta = respuesta.sort_values('duration_int', ascending = False)
        return f'El contenido de mas duración en la plataforma {plataforma} del año {anio} es {respuesta.iloc[0][3]} '
    else:
         return("Debe introducir una de estas opciones en plataforma netflix, amazon prime, hulu o disney plus.  En tipo de duracion minutos o temporada.  Y en año 1920 a 2021 ")

'''
Number of series and movies by rating.
'''
@app.get('/Número de series y películas por clasificación.')
def get_rating_count(clasificacion:str):
    in_rating = data['rating'] == clasificacion
    data_rating = data[in_rating]
    return f'El numero de contenido total es {data_rating.shape[0]}, incluyendo películas y series'

