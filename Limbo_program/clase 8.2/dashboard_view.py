import flet as ft
from persona.tabla_persona import tabla_persona
from docente.tabla_docentes import tabla_docentes
from usuario.tabla_usuarios import tabla_usuarios
from especialidad.tabla_especialidades import tabla_especialidades



class DashboardView(ft.Container):
    def __init__(self, page: ft.Page, cambiar_vista):
        super().__init__(expand=True)
        self.page = page
        self.cambiar_vista = cambiar_vista

        titulo = ft.Text(
            "📘 Panel Principal – Sistema de Horarios Marello",
            size=24,
            weight="bold",
        )

        tablas = [
            ("Personas", "Datos básicos (base de la identidad)"),
            ("Usuarios", "Cuentas, credenciales, y roles (enlace a personas)"),
            ("Especialidades", "Campos de estudio (Informática, Contabilidad, etc.)"),
            ("Ciclos", "Los 6 niveles académicos (I, II, III, etc.)"),
            ("Cursos", "Materias que se dictan"),
            ("Aulas", "Recurso físico limitado"),
            ("Docentes", "Quién enseña (enlace a Personas)"),
            ("Horarios_Base", "Slots fijos de tiempo"),
            ("Semanas", "Las 18 semanas del ciclo"),
            ("Estructura_Curricular", "Regla curricular (Curso–Ciclo–Especialidad)"),
            ("Asignaciones_Semanales", "Asignación final Docente + Curso + Aula + Semana"),
        ]

        grid = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=280,
            child_aspect_ratio=1.2,
            spacing=10,
            run_spacing=10,
        )

        for nombre, descripcion in tablas:
            card_content = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(nombre, size=18, weight="bold"),
                        ft.Text(descripcion, size=13, color=ft.Colors.GREY),
                    ],
                    spacing=5,
                ),
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.BLUE_50,
                ink=True,
                # captura el nombre correctamente con n=nombre
                on_click=lambda e, n=nombre: self.mostrar_tabla(n),
            )
            grid.controls.append(ft.Card(content=card_content, elevation=3))

        self.content = ft.Column(
            [titulo, grid],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
        )

    def mostrar_tabla(self, nombre_tabla: str):
        try:
            # PERSONAS
            if nombre_tabla == "Personas":
                vista = tabla_persona(
                    self.page,
                    volver_al_panel=lambda: self.cambiar_vista(
                        DashboardView(self.page, self.cambiar_vista)
                    ),
                )
                # Si la vista tiene cargar_datos(), llamarla (es seguro)
                if hasattr(vista, "cargar_datos"):
                    try:
                        vista.cargar_datos()
                    except Exception as ee:
                        print("Error cargando datos de Personas:", ee)
                self.cambiar_vista(vista)
                return

            # DOCENTES
            if nombre_tabla == "Docentes":
                vista = tabla_docentes(
                    self.page,
                    volver_al_panel=lambda: self.cambiar_vista(
                        DashboardView(self.page, self.cambiar_vista)
                    ),
                )
                if hasattr(vista, "cargar_datos"):
                    try:
                        vista.cargar_datos()
                    except Exception as ee:
                        print("Error cargando datos de Docentes:", ee)
                self.cambiar_vista(vista)
                return
            # USUARIOS
            elif nombre_tabla == "Usuarios":
                vista_usuarios = tabla_usuarios(
                    self.page,
                    volver_al_panel=lambda: self.cambiar_vista(DashboardView(self.page, self.cambiar_vista))
                    )
                self.cambiar_vista(vista_usuarios)
            # ESPECIALIDADES
            elif nombre_tabla == "Especialidades":
                vista_especialidades = tabla_especialidades(
                    self.page,
                    volver_al_panel=lambda: self.cambiar_vista(DashboardView(self.page, self.cambiar_vista))
                    )
                self.cambiar_vista(vista_especialidades)


            # OTRAS TABLAS (mensaje informativo)
            dlg = ft.AlertDialog(
                title=ft.Text("Tabla no implementada"),
                content=ft.Text(f"La vista para '{nombre_tabla}' aún no está disponible."),
                actions=[ft.TextButton("Cerrar", on_click=lambda e: self.page.dialog.close())],
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()

        except Exception as e:
            # Mensaje de error por si algo falla
            dlg = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(f"Ocurrió un error al abrir la tabla: {e}"),
                actions=[ft.TextButton("Cerrar", on_click=lambda e: self.page.dialog.close())],
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
