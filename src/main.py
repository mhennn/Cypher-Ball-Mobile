import flet as ft
import threading
from components import ShakeButton, QuestionBox, RequestAnswer
from API import APIServer

def run_server():
    APIServer.run()

def clicked_shake(page, question_box):
    request_answer = RequestAnswer()
    answer = request_answer.retrieve_answer()
    question_box.value = answer
    page.update()

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.GREEN
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 

    box_question = QuestionBox(text_align="center",
                    border_color="white",
                    border_width=1,
                    border_radius=20,
                    label="Ask ME",
                    disabled=True)
    
    page.add(box_question)
    page.add(
        ShakeButton(content="Shake", on_click=lambda e:clicked_shake(page, box_question), width=150, height=40)
    )
    page.update()

if __name__ == "__main__":
    threading.Thread(
        target=run_server,
        daemon=True
    ).start()
    
    ft.run(main)