import flet as ft

def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 200
    page.window.resizable = False
    page.window.maximizable = False
    page.window.full_screen = False
    page.window.center()
    page.title = "segunda clase - programacion consurrente"
# el color opaco en los textos es por que no se esta usando esa funcion
    btn_compra = ft.ElevatedButton(
        text="🛒 realizar compra",
        width=200,
        height=100,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor= "#4CAF50",
            color="white"
        )  
    )

    btn_login = ft.ElevatedButton(
        text="🔑 Iniciar sesion",
        width=200,
        height=100,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor= "#2196F3",
            color="white"
        )  
    )

    fila_botones = ft.Row(
        controls=[btn_compra, btn_login],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    page.add(
        ft.Divider(height=6, color="transparent"),
        fila_botones
    )

    page.update()

ft.app(target=main)