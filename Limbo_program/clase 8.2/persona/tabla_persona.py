import flet as ft
from conexion import ConexionDB

class TablaPersonas(ft.Container):
    def __init__(self, page, volver_al_panel):
        super().__init__(expand=True)
        self.page = page
        self.volver_al_panel = volver_al_panel
        self.db = ConexionDB()

        self.titulo = ft.Text("👤 Tabla de Personas", size=22, weight="bold")
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nombres")),
                ft.DataColumn(ft.Text("Apellidos")),
                ft.DataColumn(ft.Text("Documento")),
                ft.DataColumn(ft.Text("Email")),
            ],
            rows=[]
        )

        self.btn_volver = ft.ElevatedButton(
            "⬅ Volver al Panel",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.volver_al_panel()
        )

        self.content = ft.Column(
            [
                self.btn_volver,
                self.titulo,
                ft.Divider(),
                self.tabla
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

    def cargar_datos(self):
        conexion = self.db.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT persona_id, nombres, apellidos, numero_documento, email FROM personas")
            filas = cursor.fetchall()

            # Limpia la tabla antes de volver a llenar
            self.tabla.rows.clear()

            for fila in filas:
                self.tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(fila[0]))),
                            ft.DataCell(ft.Text(fila[1] or "")),
                            ft.DataCell(ft.Text(fila[2] or "")),
                            ft.DataCell(ft.Text(fila[3] or "")),
                            ft.DataCell(ft.Text(fila[4] or "")),
                        ]
                    )
                )

            conexion.close()
            self.page.update()

# 👉 Esta función solo crea y devuelve el componente visual:
def tabla_persona(page, volver_al_panel):
    vista = TablaPersonas(page, volver_al_panel)
    vista.cargar_datos()
    return vista
