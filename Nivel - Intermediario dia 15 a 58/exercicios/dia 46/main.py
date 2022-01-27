"""
Exercicio do dia 46

Vamos criar um app para pergunta o ano de nascimento e retorna a lista das 10,
melhores musicas daquele ano.

Infelizmente houve uma atualização no API do spotify, e a solução não está mais funcionando.

"""

import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "8a5e9263838940d9a49e5fb0363be21a"
CLIENT_SECRET = "bfdea3b82a52434a840d7b791916e717"

# Credenciais do spotify

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


# Input do usuario para identificar o ano de nascimento
ENTRADA_USUARIO = str(input("Vamos relembrar das musicas da sua infancia?\nUse o formato AAAA-MM-DD\nDigite a data de seu nascimento [ex. 1996-03-19]: "))

# Requests do site billboard

resposta = requests.get(f"https://www.billboard.com/charts/hot-100/{ENTRADA_USUARIO}/")
texto_website = resposta.text

sopa = BeautifulSoup(texto_website, "html.parser")
lista_musica = sopa.find_all(name='h3', id='title-of-a-story', class_="u-line-height-125")

titulo_musica = [x.getText().strip("\n") for x in lista_musica]


# API do spotify
musicas_uri = []
ano = ENTRADA_USUARIO.split("-")[0]
for musicas in titulo_musica:
    resultado = sp.search(q=f"Musica:{musicas} Ano:{ano}", type="track")
    print(resultado)
    try:
        uri = resultado["tracks"]["items"][0]["uri"]
        musicas_uri.append(uri)
    except IndexError:
        print(f"{musicas} Não encontrada no spotify, proxima.")


# Criando playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{ano} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=musicas_uri)
