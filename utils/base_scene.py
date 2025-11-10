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

    def show_title(self, title_text: str, subtitle_text = None):
        """显示命题标题

        Args:
            title_text: 主标题文本
            subtitle_text: 副标题，可以是字符串或字符串列表
        """
        title = Text(title_text, font_size=56)
        title.to_edge(UP)
        self.play(Write(title))

        if subtitle_text:
            # 支持单个字符串或字符串列表
            subtitles = subtitle_text if isinstance(subtitle_text, list) else [subtitle_text]

            # 创建所有副标题文本对象
            subtitle_objects = []
            for i, sub_text in enumerate(subtitles):
                subtitle = Text(sub_text, font_size=42)
                if i == 0:
                    subtitle.next_to(title, DOWN, buff=0.3)
                else:
                    subtitle.next_to(subtitle_objects[i-1], DOWN, buff=0.25)
                subtitle_objects.append(subtitle)

            # 同时显示所有副标题
            self.play(*[FadeIn(sub) for sub in subtitle_objects])
            self.wait(2)
            self.play(*[FadeOut(sub) for sub in subtitle_objects])

        return title

    def hide_title(self, title):
        """隐藏标题"""
        self.play(FadeOut(title))
