"""
Book I, Proposition 17
在任意三角形中，任何两角之和小于两直角和
In any triangle, the sum of any two angles is less than two right angles
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition17(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 17)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 17",
            ["在任意三角形中", "任何两角之和小于两直角和"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 三角形ABC
        A = np.array([-1.0, 2.0, 0])
        B = np.array([-3.0, -1.0, 0])
        C = np.array([1.5, -1.0, 0])

        # 步骤1: 显示三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)
        line_CA = Line(C, A, color=WHITE, stroke_width=3)

        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, LEFT, buff=0.2)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, DOWN, buff=0.2)

        construction_1 = Text(
            "三角形ABC",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_AB), Create(line_BC), Create(line_CA))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤2: 延长BC至D
        D = np.array([4.5, -1.0, 0])
        line_CD = Line(C, D, color=BLUE, stroke_width=3)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, RIGHT, buff=0.2)

        construction_2 = Text(
            "延长BC至点D",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        self.play(Create(line_CD))
        self.play(Write(label_D))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_BC, line_CA, line_CD,
            label_A, label_B, label_C, label_D
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 文字显示在下半部分
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1: ∠ACD是外角
        proof_1 = Text(
            "∵ ∠ACD是△ABC的外角",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: 外角大于内对角
        proof_2 = Text(
            "∴ ∠ACD>∠ABC",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        proof_3 = Text(
            "(命题1.16: 外角大于任一内对角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_2, DOWN, buff=0.2)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤3: 两边同加∠ACB
        proof_4 = Text(
            "两边同加∠ACB:",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        proof_5 = Text(
            "∠ACD+∠ACB>∠ABC+∠ACB",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 先隐去部分证明过程，为后续腾出空间
        self.play(
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5)
        )
        self.wait(0.5)

        # 证明步骤4: 邻角和等于两直角
        proof_6 = Text(
            "∵ ∠ACD+∠ACB=两直角",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_6))
        self.wait(1.5)

        proof_7 = Text(
            "(命题1.13: 邻角之和等于两直角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_6, DOWN, buff=0.2)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤5: 结论
        proof_8 = Text(
            "∴ ∠ABC+∠ACB<两直角",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 证明步骤6: 同理其他两对角
        proof_9 = Text(
            "同理，∠BAC+∠ACB<两直角",
            font_size=32
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        proof_10 = Text(
            "同理，∠CAB+∠ABC<两直角",
            font_size=32
        ).next_to(proof_9, DOWN, buff=0.35)
        self.play(Write(proof_10))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        self.play(
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9),
            FadeOut(proof_10)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "在任意三角形中",
            font_size=36,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "任意两内角之和小于两直角和",
            font_size=36,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.25)

        conclusion_line3 = Text(
            "(Q.E.D.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line2, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.play(Write(conclusion_line3))
        self.wait(2)

        # 6. 结束
        self.play(
            FadeOut(geometry_group),
            FadeOut(proof_title),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2),
            FadeOut(conclusion_line3)
        )
        self.wait(1)
