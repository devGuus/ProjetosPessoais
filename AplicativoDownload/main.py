from pytubefix import YouTube

def perguntarFormato():
    formato = input("Qual formato deseja baixar? (mp3/mp4) ") # Recebe o formato para download 
    if formato == "mp4" or formato == "MP4":
        print("Baixando...")
        stream = yt.streams.get_highest_resolution() # Pega o vídeo com maior resolução possivel
        stream.download(localArquivo) # Faz o download...
        print("Download Concluido!")
    elif formato == "mp3" or formato == "MP3":
        print("Baixando...")
        stream = yt.streams.get_audio_only() # Procura o áudio
        stream.download(localArquivo) # Baixa o áudio 
        print("Download Concluido!")
    else:
        print("Insira o formato correto ""mp3"" ou ""mp4!""")
        perguntarFormato()

# URL do vídeo
url = input("Digite a URL > ").strip()

# Local que vai baixar o arquivo
localArquivo = "C:/Users/gumar/Videos"

# Cria o objeto youtube
yt = YouTube(url)

# Função de Download
formato = perguntarFormato()