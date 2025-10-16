import flet as ft
from conexion import ConexionDB

class TablaDocentes(ft.Container):
    def __init__(self, page, volver_al_panel):
        super().__init__(expand=True)
        self.page = page
        self.volver_al_panel = volver_al_panel
        self.db = ConexionDB()

        self.titulo = ft.Text("👨‍🏫 Tabla de Docentes", size=22, weight="bold")
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Código Docente")),
                ft.DataColumn(ft.Text("Nombres")),
                ft.DataColumn(ft.Text("Apellidos")),
                ft.DataColumn(ft.Text("Especialidad ID")),
                ft.DataColumn(ft.Text("Activo")),
                ft.DataColumn(ft.Text("Observaciones")),
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

    # 🔹 Función para cargar los datos desde MySQL
    def cargar_datos(self):
        conexion = self.db.conectar()
        if conexion:
            cursor = conexion.cursor()
            query = """
                SELECT 
                    d.docente_id,
                    d.codigo_docente,
                    p.nombres,
                    p.apellidos,
                    d.especialidad_id,
                    d.activo,
                    d.observaciones
                FROM docentes d
                JOIN personas p ON d.persona_id = p.persona_id
            """
            cursor.execute(query)
            filas = cursor.fetchall()

            # Limpiar la tabla antes de llenarla
            self.tabla.rows.clear()

            for fila in filas:
                self.tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(fila[0]))),
                            ft.DataCell(ft.Text(fila[1] or "")),
                            ft.DataCell(ft.Text(fila[2] or "")),
                            ft.DataCell(ft.Text(fila[3] or "")),
                            ft.DataCell(ft.Text(str(fila[4]) if fila[4] else "")),
                            ft.DataCell(ft.Text("✅" if fila[5] else "❌")),
                            ft.DataCell(ft.Text(fila[6] or "")),
                        ]
                    )
                )

            conexion.close()
            self.page.update()

# 👉 Igual que en Personas: devuelve la vista con datos cargados
def tabla_docentes(page, volver_al_panel):
    vista = TablaDocentes(page, volver_al_panel)
    vista.cargar_datos()
    return vista
