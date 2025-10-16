import flet as ft
from conexion import ConexionDB

class TablaEspecialidades(ft.Container):
    def __init__(self, page, volver_al_panel):
        super().__init__(expand=True)
        self.page = page
        self.volver_al_panel = volver_al_panel
        self.db = ConexionDB()

        # 🔹 Título
        self.titulo = ft.Text("🎓 Tabla de Especialidades", size=22, weight="bold")

        # 🔹 Tabla
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Código")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Descripción")),
                ft.DataColumn(ft.Text("Creado En")),
                ft.DataColumn(ft.Text("Actualizado En")),
            ],
            rows=[]
        )

        # 🔹 Botón volver
        self.btn_volver = ft.ElevatedButton(
            "⬅ Volver al Panel",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.volver_al_panel()
        )

        # 🔹 Contenedor general
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

    # 🔹 Método para cargar los datos
    def cargar_datos(self):
        conexion = self.db.conectar()
        if conexion:
            cursor = conexion.cursor()
            query = """
                SELECT 
                    especialidad_id,
                    codigo,
                    nombre,
                    descripcion,
                    creado_en,
                    actualizado_en
                FROM especialidades
            """
            cursor.execute(query)
            filas = cursor.fetchall()

            # Limpia la tabla antes de llenarla
            self.tabla.rows.clear()

            for fila in filas:
                self.tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(fila[0]))),
                            ft.DataCell(ft.Text(fila[1] or "")),
                            ft.DataCell(ft.Text(fila[2] or "")),
                            ft.DataCell(ft.Text(fila[3] or "")),
                            ft.DataCell(ft.Text(str(fila[4]) if fila[4] else "-")),
                            ft.DataCell(ft.Text(str(fila[5]) if fila[5] else "-")),
                        ]
                    )
                )

            conexion.close()
            self.page.update()


# 🔹 Función que devuelve la vista completa
def tabla_especialidades(page, volver_al_panel):
    vista = TablaEspecialidades(page, volver_al_panel)
    vista.cargar_datos()
    return vista
