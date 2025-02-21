import requests 
from bs4 import BeautifulSoup
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#funcao para procurar a musica no spotify
def procurar_musica(nome_musica):
    client_id = '6a50038785c94550b3e87d3b88d2e6c0'
    client_secret = '37abdc02f34741c68e21a0f8eb46d5fe'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Realizar a busca
    resultados = sp.search(q=nome_musica, type='track', limit=1)
    
    
    for track in resultados['tracks']['items']:
        musica = {
            'nome': track['name'],
            'artista': track['artists'][0]['name'],
            'spotify_url': track['external_urls']['spotify'],
            'image': track['album']['images'][0]['url']
        }
        
    return musica

#funcao para buscar os dados da billboard no json
def billboard_10_ano_mes_JSON(data_str):
    with open('top_100_2016-2020.json', 'r') as file:
        data = json.load(file)
        mes = str(data_str).split('-')[1]
        ano = str(data_str).split('-')[0]
        if ano in data and mes in data[ano]:
            return data[ano][mes]
        else:
            return None

#funcao para buscar os dados da billboard no site da billboard
def billboard_10_ano_mes_API(data_str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    
    page = requests.get(f'https://www.billboard.com/charts/hot-100/{data_str}/', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []
    for e in soup.find_all(attrs={'class':'o-chart-results-list-row'}):
        
        if e.li.find_next('span').get_text(strip=True) == '10':
            break; 
        data.append({
            'title':e.h3.get_text(strip=True),
            'author':e.h3.find_next('span').get_text(strip=True)
        
        })
    return data
