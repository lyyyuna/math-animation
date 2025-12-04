"""
Book I, Proposition 11
由给定的直线上一已知点作一直线和给定的直线成直角
To draw a straight line at right angles to a given straight line from a given point on it
"""
from manim import *
from utils.base_scene import ElementsScene
from utils.geometry import construct_equilateral_triangle


class Proposition11(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 11)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 11",
            ["由给定的直线上一已知点","作一直线和给定的直线成直角"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点
        A = np.array([-3, 0, 0])
        B = np.array([3, 0, 0])
        C = np.array([0, 0, 0])  # C是AB上的任意点

        # 步骤1: 显示已知直线AB和点C
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        point_C = Dot(C, color=YELLOW, radius=0.08)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, LEFT)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, RIGHT)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, DOWN, buff=0.3)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(0.5)
        self.play(FadeIn(point_C), Write(label_C))
        self.wait(1)

        # 步骤2: 在AC上任取一点D
        D = np.array([-1.5, 0, 0])
        point_D = Dot(D, color=RED, radius=0.08)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, DOWN, buff=0.3)

        construction_1 = Text(
            "在AC上任取一点D",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(FadeIn(point_D), Write(label_D))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤3: 在CB上作CE等于CD（命题1.3）
        construction_2 = Text(
            "命题1.3: 在CB上作CE等于CD",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        E = np.array([1.5, 0, 0])  # CE = CD = 1.5
        point_E = Dot(E, color=RED, radius=0.08)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, DOWN, buff=0.3)

        # 高亮CD
        line_CD = Line(C, D, color=BLUE, stroke_width=4)
        self.play(Create(line_CD))
        self.wait(0.5)

        # 创建CE，与CD等长
        line_CE = Line(C, E, color=BLUE, stroke_width=4)
        self.play(Create(line_CE))
        self.play(FadeIn(point_E), Write(label_E))
        self.wait(1)

        # 恢复线段颜色
        self.play(
            line_CD.animate.set_stroke(color=WHITE, width=3),
            line_CE.animate.set_stroke(color=WHITE, width=3)
        )
        self.play(FadeOut(construction_2))

        # 步骤4: 以DE为边，作等边三角形FDE（命题1.1）
        construction_3 = Text(
            "命题1.1: 以DE为边作等边△FDE",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        # 计算等边三角形的第三个顶点F
        F = construct_equilateral_triangle(D, E)
        point_F = Dot(F, color=GREEN, radius=0.08)
        label_F = Text("F", font_size=42, color=WHITE).next_to(F, UP)

        # 画圆（表示作图过程）
        radius_DE = np.linalg.norm(E - D)
        circle_D = Circle(radius=radius_DE, color=BLUE, stroke_width=2).move_to(D)
        circle_E = Circle(radius=radius_DE, color=GREEN, stroke_width=2).move_to(E)

        self.play(Create(circle_D))
        self.play(Create(circle_E))
        self.wait(0.5)

        self.play(FadeIn(point_F), Write(label_F))
        self.wait(0.5)

        # 连接DF和EF
        line_DF = Line(D, F, color=YELLOW, stroke_width=3)
        line_EF = Line(E, F, color=YELLOW, stroke_width=3)

        self.play(Create(line_DF), Create(line_EF))
        self.wait(1)

        # 淡出圆
        self.play(FadeOut(circle_D), FadeOut(circle_E))
        self.play(FadeOut(construction_3))

        # 步骤5: 连接FC
        construction_4 = Text(
            "连接FC",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_4))
        self.wait(0.5)

        line_FC = Line(F, C, color=RED, stroke_width=3)
        self.play(Create(line_FC))
        self.wait(1)

        self.play(FadeOut(construction_4))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_CD, line_CE, line_DF, line_EF, line_FC,
            point_C, point_D, point_E, point_F,
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

        # 证明步骤1: DC等于CE
        self.play(
            line_CD.animate.set_stroke(color=BLUE, width=5),
            line_CE.animate.set_stroke(color=BLUE, width=5)
        )
        proof_1 = Text(
            "∵ DC=CE (作图)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: CF是公共边
        self.play(
            line_CD.animate.set_stroke(color=WHITE, width=3),
            line_CE.animate.set_stroke(color=WHITE, width=3),
            line_FC.animate.set_stroke(color=GREEN, width=5)
        )
        proof_2 = Text(
            "CF是公共边",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3: 两边DC、CF分别等于边EC、CF
        self.play(
            line_FC.animate.set_stroke(color=RED, width=3)
        )
        proof_3 = Text(
            "边DC、CF分别等于边EC、CF",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4: 底DF等于底FE
        self.play(
            line_DF.animate.set_stroke(color=PURPLE, width=5),
            line_EF.animate.set_stroke(color=PURPLE, width=5)
        )
        proof_4 = Text(
            "又底DF=底FE (△FDE是等边三角形)",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5: 三角形全等
        self.play(
            line_DF.animate.set_stroke(color=YELLOW, width=3),
            line_EF.animate.set_stroke(color=YELLOW, width=3)
        )
        proof_5 = Text(
            "∴ △DCF≌△ECF",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤6: 引用命题1.8
        proof_6 = Text(
            "(命题1.8: 三边对应相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_5, DOWN, buff=0.3)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤7: 角相等
        proof_7 = Text(
            "∴ ∠DCF=∠ECF",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤8: 且它们是邻角，和为平角
        proof_8 = Text(
            "且它们是邻角，和为180°",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 证明步骤9: 每个角为直角
        proof_9 = Text(
            "∴ ∠DCF=∠ECF=90°",
            font_size=32
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 证明步骤10: 引用定义
        proof_10 = Text(
            "(定义1.10: 邻角相等为直角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_9, DOWN, buff=0.3)
        self.play(Write(proof_10))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        # 高亮垂线FC
        self.play(
            line_FC.animate.set_stroke(color=RED, width=5)
        )

        conclusion_line1 = Text(
            "FC是过点C与直线AB成直角的直线",
            font_size=36,
            color=GREEN
        ).next_to(proof_10, DOWN, buff=0.4)

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
            FadeOut(proof_10),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
