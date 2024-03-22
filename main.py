#importación de librerías requests, bs4 y pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Define la URL de la página a la que vas a hacer web scraping
url = "https://cnnespanol.cnn.com/"

#Realiza la petición a la página web y guarda el HTML en la variable response
response = requests.get(url)

#Verifica que la petición haya sido exitosa
if response.status_code == 200:
  
    #Crea un objeto BeautifulSoup a partir del HTML de la
    #página web y lo guarda en la variable soup
    soup = BeautifulSoup(response.content, "html.parser")
    
    #Busca todos los elementos h2 con la clase 'news_title'
    titles = soup.find_all('h2', class_='news__title')
    
    #Extrae el texto de cada título y lo almacenaen en 
    #una lista llamada titles_text
    titles_text = [title.get_text().strip() for title in titles] 
    
    #Crea un DataFrame con los títulos extraídos
    df = pd.DataFrame(titles_text, columns=['Title'])

    #Graba el DataFrame en un archivo CSV
    df.to_csv('news.csv', index=False, encoding='utf-8-sig')

    #Muestra un mensaje de éxito
    print("Archivo 'news.csv' creado con éxito")

    