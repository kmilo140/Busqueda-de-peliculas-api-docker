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
@app.get('/get_word_count')
def get_word_count(plat:str, keyword:str):
    in_plat = data['id'].str.contains(plat[0])
    data_plat = data[in_plat]
    busqueda = data_plat['title'].str.contains(keyword)
    return f'En la plataforma {plat} se encuentra que hay {busqueda.value_counts()[1]} titulos que coinciden con {keyword}'
'''
Number of films per platform with a score higher than XX in a given year.
'''
@app.get('/get_score_count')
def get_score_count(plat:str, score:int, anio:int):
    in_plat = data['id'].str.contains(plat[0])
    data_plat = data[in_plat]
    in_release = data_plat["release_year"] == anio
    data_plat_release = data_plat[in_release]
    in_type = data_plat_release["category"] == "movie"
    final = data_plat_release[in_type]
    respuesta = final.apply(lambda x: x['score'] > score, axis=1).sum()
    return f'El numero de titulos en la plataforma {plat}, el año {anio} es {respuesta}'
'''
The second highest scoring film for a given platform, according to the alphabetical order of titles.
'''    
@app.get('/get_second_score')
def get_second_score(plat:str):
    in_plat = data['id'].str.contains(plat[0])
    data_plat = data[in_plat]
    in_type = data_plat["category"] == "movie"
    final = data_plat[in_type]
    respuesta = final.sort_values(['score','title'], ascending=[False, True])
    return f'La segunda película con mayor score para una plataforma {plat}, es {respuesta.iloc[1][3]} según el orden alfabético de los títulos.'
  
'''
Longest running film by year, platform and length type.
'''
@app.get('/get_longest')
def get_longest(plat:str, duration_type:str, anio:int):
    respuesta = data[(data['release_year'] == anio) & (data['id'].str.contains(plat[0])) & (data['duration_type'] == duration_type) ]
    respuesta = respuesta.sort_values('duration_int', ascending = False)
    return f'El contenido de mas duración en la plataforma {plat} del año {anio} es {respuesta.iloc[0][3]} '

'''
Number of series and movies by rating.
'''
@app.get('/get_rating_count')
def get_rating_count(ranting:str):
    in_rating = data['rating'] == ranting
    data_rating = data[in_rating]
    return f'El numero de contenido total es {data_rating.shape[0]}, incluyendo películas y series'

