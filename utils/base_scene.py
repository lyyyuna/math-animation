"""
Base scene class for Elements propositions
"""
from manim import *


class ElementsScene(Scene):
    """Base scene for all Elements propositions"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proposition_number = None
        self.book_number = None

    def setup_proposition(self, book: int, prop: int):
        """设置命题编号"""
        self.book_number = book
        self.proposition_number = prop

    def show_title(self, title_text: str, subtitle_text: str = None):
        """显示命题标题"""
        title = Text(title_text, font_size=56)
        title.to_edge(UP)
        self.play(Write(title))

        if subtitle_text:
            subtitle = Text(subtitle_text, font_size=42)
            subtitle.next_to(title, DOWN, buff=0.3)
            self.play(FadeIn(subtitle))
            self.wait(1)
            self.play(FadeOut(subtitle))

        return title

    def hide_title(self, title):
        """隐藏标题"""
        self.play(FadeOut(title))
