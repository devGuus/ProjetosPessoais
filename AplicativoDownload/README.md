# YouTube Downloader

Este script permite baixar vídeos do YouTube no formato MP3 (áudio) ou MP4 (vídeo) utilizando a biblioteca `pytubefix`.

## 📌 Requisitos

Antes de executar o código, certifique-se de que você tem os seguintes requisitos instalados:

- Python 3.x
- Biblioteca `pytubefix`

Para instalar a biblioteca, use o seguinte comando:

```bash
pip install pytubefix
```

## 🚀 Como usar

1. Execute o script Python.
2. Insira a URL do vídeo do YouTube que deseja baixar.
3. Escolha o formato desejado (`mp3` para áudio ou `mp4` para vídeo).
4. O arquivo será baixado no diretório especificado no código.

## 📜 Código

```python
from pytubefix import YouTube

def perguntarFormato():
    formato = input("Qual formato deseja baixar? (mp3/mp4) ")
    if formato.lower() == "mp4":
        print("Baixando...")
        stream = yt.streams.get_highest_resolution()
        stream.download(localArquivo)
        print("Download Concluído!")
    elif formato.lower() == "mp3":
        print("Baixando...")
        stream = yt.streams.get_audio_only()
        stream.download(localArquivo)
        print("Download Concluído!")
    else:
        print("Formato inválido! Escolha entre 'mp3' ou 'mp4'.")
        perguntarFormato()

# URL do vídeo
temp_url = input("Digite a URL do vídeo: ").strip()

# Local onde o arquivo será salvo
localArquivo = "C:/Users/gumar/Videos"

# Criar objeto YouTube
yt = YouTube(temp_url)

# Iniciar o download
perguntarFormato()
```

## 📂 Local de Download

O arquivo será salvo no caminho:

```
C:/Users/gumar/Videos
```

Caso queira alterar o local de salvamento, modifique a variável `localArquivo` no código.

## 🛠 Possíveis Melhorias

- Adicionar suporte para escolher o diretório de salvamento.
- Melhorar tratamento de erros para URLs inválidas.
- Converter MP3 automaticamente para remover o formato `.mp4` no áudio.

## 📞 Suporte

Caso tenha dúvidas ou precise de ajuda, sinta-se à vontade para abrir uma *issue* ou contribuir com melhorias! 🚀

