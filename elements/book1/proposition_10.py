from manim import *
from utils.base_scene import ElementsScene

class Proposition10(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 10)

        # 1. 显示标题和问题陈述
        title = self.show_title("卷 I, 命题 10", "二等分已知线段")
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点
        A = np.array([-2, 0, 0])
        B = np.array([2, 0, 0])

        # 步骤1: 显示已知线段AB
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, LEFT)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, RIGHT)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(1)

        # 步骤2: 以AB为边作等边三角形ABC（命题1.1）
        # 直接显示等边三角形
        C = np.array([0, 3.464, 0])  # 正三角形的顶点
        point_C = Dot(C, color=YELLOW, radius=0.08)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, UP)

        construction_1 = Text(
            "命题1.1: 以AB为边作等边△ABC",
            font_size=38,
            color=YELLOW
        ).next_to(C, UP, buff=0.8)
        self.play(Write(construction_1))
        self.wait(0.5)

        line_AC = Line(A, C, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)

        self.play(
            Create(line_AC),
            Create(line_BC),
            FadeIn(point_C),
            Write(label_C)
        )
        self.wait(1)

        self.play(FadeOut(construction_1))

        # 步骤3: 二等分角ACB（命题1.9）
        construction_2 = Text(
            "命题1.9: 作角ACB的角平分线CD",
            font_size=38,
            color=YELLOW
        ).next_to(C, UP, buff=0.8)
        self.play(Write(construction_2))
        self.wait(0.5)

        # D是AB的中点
        D = np.array([0, 0, 0])
        point_D = Dot(D, color=RED, radius=0.08)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, DOWN)

        line_CD = Line(C, D, color=YELLOW, stroke_width=3)

        self.play(Create(line_CD))
        self.play(FadeIn(point_D), Write(label_D))
        self.wait(1)

        self.play(FadeOut(construction_2))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_AC, line_BC, line_CD,
            point_C, point_D,
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

        # 证明步骤1: AC等于CB
        self.play(
            line_AC.animate.set_stroke(color=BLUE, width=5),
            line_BC.animate.set_stroke(color=BLUE, width=5)
        )
        proof_1 = Text(
            "∵ △ABC是等边三角形",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: AC=CB
        proof_2 = Text(
            "∴ AC=CB",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3: CD为公共边
        self.play(
            line_AC.animate.set_stroke(color=WHITE, width=3),
            line_BC.animate.set_stroke(color=WHITE, width=3),
            line_AB.animate.set_stroke(color=WHITE, width=3),
            line_CD.animate.set_stroke(color=GREEN, width=5)
        )
        proof_3 = Text(
            "CD为公共边",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4: 角ACD等于角BCD
        self.play(
            line_CD.animate.set_stroke(color=YELLOW, width=3)
        )

        proof_4 = Text(
            "∠ACD=∠BCD (角平分线)",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5: 两边及其夹角对应相等
        proof_5 = Text(
            "边AC、CD分别等于边BC、CD",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤6: 三角形全等
        proof_6 = Text(
            "且∠ACD=∠BCD",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤7: 应用命题1.4
        proof_7 = Text(
            "∴ △ACD≌△BCD",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤8: 引用命题
        proof_8 = Text(
            "(命题1.4: 两边及其夹角对应相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_7, DOWN, buff=0.3)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 证明步骤9: 底边相等
        # 创建AD和BD的线段高亮
        line_AD = Line(A + UP * 3.2, D + UP * 3.2, color=PURPLE, stroke_width=5)
        line_BD = Line(B + UP * 3.2, D + UP * 3.2, color=PURPLE, stroke_width=5)

        self.play(
            Create(line_AD),
            Create(line_BD)
        )

        proof_9 = Text(
            "∴ AD=BD",
            font_size=32
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        self.play(
            FadeOut(line_AD),
            FadeOut(line_BD)
        )

        # 高亮中点D
        self.play(
            point_D.animate.scale(1.5).set_color(RED)
        )

        conclusion_line1 = Text(
            "线段AB二等分于点D",
            font_size=36,
            color=GREEN
        ).next_to(proof_9, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "(Q.E.F.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.wait(2)

        # 6. 结束
        self.play(
            FadeOut(geometry_group),
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
