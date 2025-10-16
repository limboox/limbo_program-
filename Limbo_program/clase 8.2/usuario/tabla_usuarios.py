import flet as ft
from conexion import ConexionDB

class TablaUsuarios(ft.Container):
    def __init__(self, page, volver_al_panel):
        super().__init__(expand=True)
        self.page = page
        self.volver_al_panel = volver_al_panel
        self.db = ConexionDB()

        # 🔹 Título
        self.titulo = ft.Text("👥 Tabla de Usuarios", size=22, weight="bold")

        # 🔹 Estructura de columnas
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nombre de Usuario")),
                ft.DataColumn(ft.Text("Email")),
                ft.DataColumn(ft.Text("Rol")),
                ft.DataColumn(ft.Text("Activo")),
                ft.DataColumn(ft.Text("Último Login")),
                ft.DataColumn(ft.Text("Creado En")),
            ],
            rows=[]
        )

        # 🔹 Botón para volver al panel principal
        self.btn_volver = ft.ElevatedButton(
            "⬅ Volver al Panel",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.volver_al_panel()
        )

        # 🔹 Contenido general
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

    # 🔹 Cargar los datos desde MySQL
    def cargar_datos(self):
        conexion = self.db.conectar()
        if conexion:
            cursor = conexion.cursor()
            query = """
                SELECT 
                    usuario_id,
                    nombre_usuario,
                    email,
                    rol,
                    activo,
                    ultimo_login,
                    creado_en
                FROM usuarios
            """
            cursor.execute(query)
            filas = cursor.fetchall()

            # Limpiar tabla antes de agregar nuevos datos
            self.tabla.rows.clear()

            for fila in filas:
                self.tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(fila[0]))),
                            ft.DataCell(ft.Text(fila[1] or "")),
                            ft.DataCell(ft.Text(fila[2] or "")),
                            ft.DataCell(ft.Text(fila[3] or "")),
                            ft.DataCell(ft.Text("✅" if fila[4] else "❌")),
                            ft.DataCell(ft.Text(str(fila[5]) if fila[5] else "-")),
                            ft.DataCell(ft.Text(str(fila[6]) if fila[6] else "-")),
                        ]
                    )
                )

            conexion.close()
            self.page.update()


# 🔹 Función que devuelve la vista completa para el dashboard
def tabla_usuarios(page, volver_al_panel):
    vista = TablaUsuarios(page, volver_al_panel)
    vista.cargar_datos()
    return vista
