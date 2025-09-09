import flet as ft
import os
import sys
import subprocess

def main(page: ft.Page):
    if not page.web:
        page.window.width = 500
        page.window.height = 400
        page.window.resizable = False
        page.window.center()

    page.title = "Login - Sistema de Ventas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # === Fondo con imagen centrada y ajustada al tamaño de la ventana ===
    page.bgimage = ft.DecorationImage(
        src="https://img.freepik.com/free-vector/gradient-technology-futuristic-background_23-2149122416.jpg",  
        fit=ft.ImageFit.COVER,
        alignment=ft.alignment.center
    )

    # --- CAMPOS DE LOGIN ---
    usuario_input = ft.TextField(
        label="👤 Usuario",
        width=280,
        border_color="blue",
        border_width=2,
        color="white",
        label_style=ft.TextStyle(color="white70"),
    )
    password_input = ft.TextField(
        label="🔑 Contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        border_color="blue",
        border_width=2,
        color="white",
        label_style=ft.TextStyle(color="white70"),
    )
    recordar = ft.Checkbox(
        label="Recuérdame", 
        value=False, 
        check_color="white", 
        fill_color="#4CAF50",
        label_style=ft.TextStyle(color="white70"),
    )
    mensaje_error = ft.Text("", color="red")

    # --- FUNCIONES ---
    def abrir_dashboard():
        page.window.close()
        ruta_dashboard = os.path.join(os.path.dirname(__file__), "dashboard.py")
        subprocess.Popen([sys.executable, ruta_dashboard])

    def validar_login(e):
        usuario = usuario_input.value.strip()
        clave = password_input.value.strip()

        if usuario == "saul salvador" and clave == "2929":
            mensaje_error.value = ""
            page.update()
            abrir_dashboard()
        else:
            mensaje_error.value = "❌ Usuario o contraseña incorrectos"
            page.update()

    # --- TARJETA TRANSLÚCIDA ---
    login_card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Igresar", size=24, weight=ft.FontWeight.BOLD, color="white"),
                usuario_input,
                password_input,
                recordar,
                mensaje_error,
                ft.ElevatedButton(
                    "LOGIN",
                    width=280,
                    bgcolor="#3949ab",
                    color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=validar_login
                ),
                ft.TextButton("¿Olvidaste tu contraseña?", style=ft.ButtonStyle(color="white70"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
        width=350,
        padding=30,
        bgcolor=ft.Colors.with_opacity(0.25, "black"),
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=20, color="#00000088"),
    )

    page.add(login_card)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
