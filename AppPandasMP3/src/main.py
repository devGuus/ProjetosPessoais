import flet as ft
from pytubefix import YouTube
import os

def main(page: ft.Page):
    page.title = "PANDASMP3"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Cabeçalho da página
    page.appbar = ft.AppBar(
        title=ft.Text("PandasMP3"),
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
    
    def iniciar_download(result: ft.FilePickerResultEvent):
        # Função chamada após o usuário selecionar o diretório.
        if not result.path:
            status_text.value = "❌ Nenhuma pasta selecionada!"
            page.update()
            return
        
        pasta = result.path
        os.makedirs(pasta, exist_ok=True)
        
        url = link_download.value.strip()
        formato = formato_dropdown.value
        
        if not url:
            status_text.value = "❌ Insira um link válido!"
            page.update()
            return
        
        if not formato:
            status_text.value = "❌ Selecione um formato (MP3 ou MP4)!"
            page.update()
            return
        
        status_text.value = "⬇️ Baixando..."
        page.update()
        
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution() if formato == "mp4" else yt.streams.get_audio_only()
        arquivo = stream.download(output_path=pasta)
        
        status_text.value = f"✅ Download concluído: {arquivo}"
        page.update()
    
    def selecionar_pasta(e):
        # Abre o seletor de diretório e chama `iniciar_download` após a escolha.
        seletor_pasta.get_directory_path()
    
    # Criando o seletor de diretório
    seletor_pasta = ft.FilePicker()
    seletor_pasta.on_result = iniciar_download
    page.overlay.append(seletor_pasta)
    
    # Input do link
    link_download = ft.TextField(
        label="Digite o link aqui!",
        prefix_icon=ft.Icons.LINK,
        width=300,
        border_color=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(10),
        border_width=2,
    )
    
    # Opções para download
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
    
    # Botão para selecionar pasta e baixar
    botao_download = ft.ElevatedButton(
        text="Baixar",
        width=300,
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE,
        on_click=selecionar_pasta,
    )
    
    status_text = ft.Text()
    
    page.add(
        ft.Column(
            controls=[
                link_download,
                formato_dropdown,
                botao_download,
                status_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()

ft.app(main, assets_dir="assets")