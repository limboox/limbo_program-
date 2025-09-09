import flet as ft
import os, sys, subprocess

def main(page: ft.Page):
    page.window.width = 1000
    page.window.height = 600
    page.window.resizable = True
    page.window.center()
    page.title = "Dashboard - Sistema de Ventas"
    page.bgcolor = "#f5f5f5"

    # --- FUNCIONES ---
    def volver_inicio(e):
        page.window.close()
        ruta_main = os.path.join(os.path.dirname(__file__), "main.py")
        subprocess.Popen([sys.executable, ruta_main])

    # --- SIDEBAR ---
    sidebar = ft.Container(
        content=ft.Column(
            [
                ft.Text("📊 Panel", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color="transparent"),
                ft.ElevatedButton("🏠 Inicio", width=180, bgcolor="#3949ab", color="white"),
                ft.ElevatedButton("📈 Reportes", width=180, bgcolor="#3949ab", color="white"),
                ft.ElevatedButton("📦 Productos", width=180, bgcolor="#3949ab", color="white"),
                ft.ElevatedButton("👥 Clientes", width=180, bgcolor="#3949ab", color="white"),
                ft.Divider(height=30, color="transparent"),
                ft.ElevatedButton("⬅️ Cerrar sesión", width=180, bgcolor="#d32f2f", color="white", on_click=volver_inicio),
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=220,
        bgcolor="#1a237e",
        padding=20,
    )

    # --- HEADER ---
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("🎯 Dashboard Principal", size=26, weight=ft.FontWeight.BOLD, color="#1a237e"),
                ft.Text("Sistema de Gestión de Ventas", size=16, color="#616161"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor="white",
        shadow=ft.BoxShadow(blur_radius=15, color="#00000033"),
    )

    # --- TARJETAS DE ESTADÍSTICAS ---
    cards = ft.Row(
        [
            ft.Container(
                content=ft.Column([
                    ft.Text("Ventas Hoy", size=18, weight=ft.FontWeight.BOLD, color="#2196F3"),
                    ft.Text("S/. 2,350", size=22, weight=ft.FontWeight.BOLD),
                ]),
                width=200,
                height=120,
                bgcolor="white",
                padding=20,
                border_radius=15,
                shadow=ft.BoxShadow(blur_radius=12, color="#00000022"),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Clientes Nuevos", size=18, weight=ft.FontWeight.BOLD, color="#4CAF50"),
                    ft.Text("35", size=22, weight=ft.FontWeight.BOLD),
                ]),
                width=200,
                height=120,
                bgcolor="white",
                padding=20,
                border_radius=15,
                shadow=ft.BoxShadow(blur_radius=12, color="#00000022"),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Productos en Stock", size=18, weight=ft.FontWeight.BOLD, color="#FF9800"),
                    ft.Text("128", size=22, weight=ft.FontWeight.BOLD),
                ]),
                width=200,
                height=120,
                bgcolor="white",
                padding=20,
                border_radius=15,
                shadow=ft.BoxShadow(blur_radius=12, color="#00000022"),
            ),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # --- CONTENIDO PRINCIPAL ---
    contenido = ft.Column(
        [
            header,
            ft.Divider(height=20, color="transparent"),
            cards,
            ft.Divider(height=30, color="transparent"),
            ft.Text("📌 Accesos rápidos", size=20, weight=ft.FontWeight.BOLD, color="#424242"),
            ft.Row([
                ft.ElevatedButton("📈 Ver Reportes", width=200),
                ft.ElevatedButton("📦 Gestionar Productos", width=200),
                ft.ElevatedButton("👥 Clientes", width=200),
            ], spacing=20),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    # --- LAYOUT PRINCIPAL ---
    layout = ft.Row(
        [
            sidebar,
            ft.Container(content=contenido, expand=True, padding=20),
        ],
        expand=True,
    )

    page.add(layout)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
