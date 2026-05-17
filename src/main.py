import flet as ft
from components import ShakeButton
from components import QuestionBox

def clicked_shake(e):
    pass

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.GREEN
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 

    page.add(
        QuestionBox(text_align="center",
                    border_color="white",
                    border_width=1,
                    border_radius=20,
                    label="Ask ME")
    )
    
    page.add(
        ShakeButton(content="Shake", on_click=clicked_shake, width=150, height=40)
    )

    page.update()

ft.run(main)