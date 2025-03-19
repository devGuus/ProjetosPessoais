import flet as ft
from pytubefix import YouTube
from moviepy import AudioFileClip
import os

def main(page: ft.Page):
    page.title = "PANDASMP3"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Cabeçalho da pagina
    page.appbar = ft.AppBar(
        title = ft.Text("PandasMP3"),
        center_title=True,
        bgcolor=ft.Colors.BLACK54,
        actions=[
            ft.Image(
                src='AppFastLink/src/assets/logo.png',
                width=60,
                height=60,
                fit=ft.ImageFit.COVER,
            )
        ]
)
    
    def baixar_video(entrada):
        url = link_download.value.strip()
        if not url:
            status_text.value = "Por favor, inserir um link válido!"
            page.update()
            return
        formato = formato_dropdown.value  # Obtém a opção escolhida (mp3 ou mp4)
        arquivo_download = "Downloads"
        os.makedirs(arquivo_download, exist_ok=True)  # Cria a pasta de download se não existir

        # Atualiza o status do download
        status_text.value = "Baixando..."
        page.update()

        yt = YouTube(url)

        if formato == "mp4":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
            arquivo = stream.download(output_path=arquivo_download)
            status_text.value = f"Download Concluído: {arquivo}"
        elif formato == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            arquivo = stream.download(output_path=arquivo_download)
            status_text.value = f"Download Concluído: {arquivo}"
            # Converte para MP3
            mp3_arquivo = arquivo.replace(".mp4", ".mp3").replace(".webm", ".mp3")
            audio_clip = AudioFileClip(arquivo)
            audio_clip.write_audiofile(mp3_arquivo, codec="libmp3lame")
            audio_clip.close()
            os.remove(arquivo)  # Remove o arquivo original de vídeo

            status_text.value = f"Download Concluído: {mp3_arquivo}"
    
        page.update()

    # Input do link
    link_download = ft.TextField(
        label="Digite o link aqui!",
        prefix_icon=ft.Icons.LINK,
        width=300,
        border_color=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(10),
        border_width=2,
    )

    formato_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("mp3", text="🎵 MP3"),
            ft.dropdown.Option("mp4", text="🎬 MP4")
        ],
        label="Escolha o formato",
        width=250,
        border_radius=10,
        filled=True,
        text_size=16
    )

    # Botão 'Baixar' para download
    botao_download = ft.ElevatedButton(
        text="Baixar",
        width=300,
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE,
        on_click=baixar_video,
    )

    status_text = ft.Text()

    page.add(
        ft.Column(
            controls=[
                link_download,
                botao_download,
                status_text,
                formato_dropdown,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()

ft.app(main, assets_dir="assets")