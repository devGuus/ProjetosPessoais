from pytubefix import YouTube

url = input("Digite a URL do vídeo: ")
yt = YouTube(url)

for stream in yt.streams:
    print(stream)

video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()
print(f"Stream selecionado: {video_stream}")

if video_stream:
    video_stream.download(output_path="downloads/", filename="audio.mp3")