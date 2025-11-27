"""
Book I, Proposition 9
二等分一个给定的角
To bisect a given rectilinear angle
"""
from manim import *
from utils.base_scene import ElementsScene
from utils.geometry import construct_equilateral_triangle


class Proposition9(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 9)

        # 1. 显示标题
        title = self.show_title(
            "卷一, 命题9",
            "二等分一个给定的角"
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义角BAC的三个点
        A = np.array([0, 0, 0])
        B = np.array([-3, 2.5, 0])
        C = np.array([3, 1.5, 0])

        # 画出角BAC
        line_AB = Line(A, B, color=WHITE)
        line_AC = Line(A, C, color=WHITE)

        self.play(Create(line_AB), Create(line_AC))
        self.wait(0.5)

        # 标注点A, B, C
        label_A = Text("A", font_size=42).next_to(A, DOWN)
        label_B = Text("B", font_size=42).next_to(B, LEFT)
        label_C = Text("C", font_size=42).next_to(C, RIGHT)

        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)

        # 显示说明：这是要二等分的角
        instruction_1 = Text(
            "在AB上任取一点D",
            font_size=38,
            color=YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(instruction_1))
        self.wait(0.5)

        # 在AB上取点D
        D = A + (B - A) / np.linalg.norm(B - A) * 2.0
        point_D = Dot(D, color=YELLOW)
        label_D = Text("D", font_size=42).next_to(D, LEFT)

        self.play(FadeIn(point_D), Write(label_D))
        self.wait(1)

        # 显示说明：在AC上作AE=AD
        self.play(FadeOut(instruction_1))
        instruction_2_line1 = Text(
            "在AC上作AE，使AE=AD",
            font_size=38,
            color=YELLOW
        ).to_edge(DOWN, buff=1.0)

        instruction_2_line2 = Text(
            "(命题1.3: 从较长线段截取等于较短线段的部分)",
            font_size=28,
            color=GRAY
        ).next_to(instruction_2_line1, DOWN, buff=0.2)

        self.play(Write(instruction_2_line1))
        self.play(Write(instruction_2_line2))
        self.wait(0.5)

        # 在AC上作AE，使AE=AD
        AD_length = np.linalg.norm(D - A)
        E = A + (C - A) / np.linalg.norm(C - A) * AD_length
        point_E = Dot(E, color=YELLOW)
        label_E = Text("E", font_size=42).next_to(E, DR)

        self.play(FadeIn(point_E), Write(label_E))
        self.wait(1)

        # 显示说明：连接DE
        self.play(FadeOut(instruction_2_line1), FadeOut(instruction_2_line2))
        instruction_3 = Text(
            "连接DE",
            font_size=38,
            color=YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(instruction_3))
        self.wait(0.5)

        # 连接DE
        line_DE = Line(D, E, color=WHITE)
        self.play(Create(line_DE))
        self.wait(1)

        # 显示说明：以DE为边作等边三角形DEF
        self.play(FadeOut(instruction_3))
        instruction_4_line1 = Text(
            "以DE为边，作等边三角形DEF",
            font_size=38,
            color=YELLOW
        ).to_edge(DOWN, buff=1.0)

        instruction_4_line2 = Text(
            "(命题1.1: 在给定直线上构造等边三角形)",
            font_size=28,
            color=GRAY
        ).next_to(instruction_4_line1, DOWN, buff=0.2)

        self.play(Write(instruction_4_line1))
        self.play(Write(instruction_4_line2))
        self.wait(0.5)

        # 以DE为边构造等边三角形DEF
        F = construct_equilateral_triangle(D, E)

        # 创建等边三角形DEF
        line_DF = Line(D, F, color=BLUE)
        line_EF = Line(E, F, color=BLUE)
        point_F = Dot(F, color=YELLOW)
        label_F = Text("F", font_size=42).next_to(F, UP)

        self.play(Create(line_DF), Create(line_EF))
        self.play(FadeIn(point_F), Write(label_F))
        self.wait(1)

        # 显示说明：连接AF
        self.play(FadeOut(instruction_4_line1), FadeOut(instruction_4_line2))
        instruction_5 = Text(
            "连接AF",
            font_size=38,
            color=YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(instruction_5))
        self.wait(0.5)

        # 连接AF
        line_AF = Line(A, F, color=GREEN, stroke_width=3)
        self.play(Create(line_AF))
        self.wait(1)

        self.play(FadeOut(instruction_5))
        self.wait(0.5)

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_AC, line_DE, line_DF, line_EF, line_AF,
            point_D, point_E, point_F,
            label_A, label_B, label_C, label_D, label_E, label_F
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

        # 证明步骤1: AD=AE（作图所得）
        self.play(
            point_D.animate.set_color(BLUE),
            point_E.animate.set_color(BLUE)
        )
        proof_1 = Text(
            "∵ AD=AE (作图所得)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: AF为公共边
        self.play(
            point_D.animate.set_color(YELLOW),
            point_E.animate.set_color(YELLOW),
            line_AF.animate.set_stroke(color=BLUE, width=4)
        )
        proof_2 = Text(
            "AF为公共边",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3: DF=EF（等边三角形）
        self.play(
            line_AF.animate.set_stroke(color=GREEN, width=3),
            line_DF.animate.set_stroke(color=BLUE, width=4),
            line_EF.animate.set_stroke(color=BLUE, width=4)
        )
        proof_3 = Text(
            "DF=EF (等边三角形DEF)",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4: 因此两个三角形三边分别相等
        self.play(
            line_DF.animate.set_stroke(color=BLUE, width=2),
            line_EF.animate.set_stroke(color=BLUE, width=2)
        )
        proof_4 = Text(
            "∴ △DAF和△EAF中，DA=EA，AF为公共边，DF=EF",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5: 根据命题1.8，对应角相等
        proof_5 = Text(
            "∴ ∠DAF=∠EAF (命题1.8)",
            font_size=32,
            color=YELLOW
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤6: 引用命题1.8的说明
        proof_6 = Text(
            "(三角形三边分别相等，则等边所夹角相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_5, DOWN, buff=0.2)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 高亮角平分线AF
        self.play(
            line_AF.animate.set_stroke(color=GREEN, width=5)
        )
        self.wait(1)

        # 5. 结论 - 分两行显示
        conclusion_line1 = Text(
            "AF二等分∠BAC",
            font_size=36,
            color=GREEN
        ).next_to(proof_6, DOWN, buff=0.4)

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
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
