from pytubefix import YouTube
from pytubefix.cli import on_progress

""""
    Caso queira redefinir o cache para autenticação, somente importe da seguinte forma
    from pytubefix.helpers import reset_cache
"""

url = input("Digite a URL do áudio > ")
video = YouTube(url) # Criando objeto video

# Retorna aonde o download está %
video = YouTube(url, on_complete_callback= on_progress)

# Informações do vídeo
#print(f"\n\nTitulo do Video: {video.title}\n\nLink Tumbnail: {video.thumbnail_url}\n\n")

# Dowload do video
video_download = video.streams.get_audio_only()
video_download.download()