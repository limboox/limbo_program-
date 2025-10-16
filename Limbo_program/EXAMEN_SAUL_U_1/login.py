import flet as ft

def main(page: ft.Page):
    def login_clicked(e):
        if username.value == "admin" and password.value == "1234":
            show_admin()
        if username.value == "client" and password.value == "2345":
            show_user()
        if username.value == "visit" and password.value == "3456":
            show_visit()
        if username.value == "recep" and password.value == "4567":
            show_recep()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuario o contraseña incorrectos"), bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

    def show_admin():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido, Admin 👑", size=25),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: show_login())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()
    def show_user():
        page.controls.clear()
        page.hoteles = 5  
        contador = ft.Text(str(page.hoteles), size=20, color="blue")
        def reservar(e):
            if page.hoteles > 0:
                page.hoteles -= 1
                contador.value = str(page.hoteles)
                page.snack_bar = ft.SnackBar(ft.Text("✅ Reserva correcta"), bgcolor="green")
            else:
                page.snack_bar = ft.SnackBar(ft.Text("❌ No hay hoteles disponibles"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
        marco = ft.Container(
            content=ft.Row([
                ft.Text("Hoteles disponibles:", size=18),
                contador
            ]),
            bgcolor="#eeeeee",
            padding=10,
            border_radius=5
        )
        page.add(
            ft.Column(
                [
                    ft.Text("Reseva Tu Hotel 🙋", size=25),
                    marco,
                    ft.ElevatedButton("Reservar hotel", on_click=reservar),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: show_login())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()
    def show_visit():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido, Visitante 👑", size=25),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: show_login())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()
    def show_recep():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido, Recepcionista 👑", size=25),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: show_login())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()
    def show_login():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Login", size=30, weight="bold"),
                    username,
                    password,
                    login_btn
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()
    username = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    login_btn = ft.ElevatedButton("Iniciar sesión", on_click=login_clicked)
    show_login()

ft.app(target=main)
