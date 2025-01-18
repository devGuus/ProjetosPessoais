from pytubefix import YouTube
from pytubefix.cli import on_progress

""""
    Caso queira redefinir o cache para autenticação, somente importe da seguinte forma
    from pytubefix.helpers import reset_cache
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
"""

# Recebe o link do vídeo
link = input("Digite o Link do vídeo: ")

# Criando o objeto vídeo
video = YouTube(link) 

# Autenticação Oauth, Restrição de idade, Acessar sua conta no YT
video = YouTube(link, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)

# Informações do vídeo
print(f"\n\nTitulo do Video: {video.title}\nLink Tumbnail: {video.thumbnail_url}")

# Download 
print('\nDownload...')
video_download = video.streams.get_highest_resolution()
video_download.download() # É necessario iniciar o download para pedir a autenticação