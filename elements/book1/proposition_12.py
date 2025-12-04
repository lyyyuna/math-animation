"""
Book I, Proposition 12
由给定的无限直线外一已知点作该直线的垂线
To draw a perpendicular to a given infinite straight line from a given point not on it
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition12(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 12)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 12",
            ["由给定的无限直线外一已知点","作该直线的垂线"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点
        A_x = -4.5
        B_x = 4.5
        A = np.array([A_x, -0.8, 0])
        B = np.array([B_x, -0.8, 0])
        C = np.array([0, 2, 0])  # C是AB外一点

        # 步骤1: 显示已知直线AB和点C
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        point_C = Dot(C, color=YELLOW, radius=0.08)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, LEFT)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, RIGHT)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, UP, buff=0.3)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(0.5)
        self.play(FadeIn(point_C), Write(label_C))
        self.wait(1)

        # 步骤2: 在AB另一侧任取一点D
        D = np.array([1.0, -1.2, 0])
        point_D = Dot(D, color=RED, radius=0.08)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, DOWN, buff=0.3)

        construction_1 = Text(
            "在AB另一侧任取一点D",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(FadeIn(point_D), Write(label_D))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤3: 以C为圆心，CD为半径作圆EFG（公设3）
        construction_2 = Text(
            "公设3: 以C为圆心，CD为半径作圆",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        # 连接CD（显示半径）
        line_CD = Line(C, D, color=BLUE, stroke_width=3)
        self.play(Create(line_CD))
        self.wait(0.5)

        # 计算圆的半径
        radius_CD = np.linalg.norm(D - C)
        circle_EFG = Circle(radius=radius_CD, color=BLUE, stroke_width=2).move_to(C)

        self.play(Create(circle_EFG))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 步骤4: 找到圆与直线AB的交点E和G
        construction_3 = Text(
            "圆与直线AB交于点E、G",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        # 计算交点E和G
        # 直线AB: y = -0.8
        # 圆心C: (0, 2, 0)
        # 圆的方程: x^2 + (y-2)^2 = radius_CD^2
        # 代入 y = -0.8: x^2 + (-0.8-2)^2 = radius_CD^2
        # x^2 = radius_CD^2 - 2.8^2
        y_line = -0.8
        x_intersect = np.sqrt(radius_CD**2 - (y_line - C[1])**2)

        E = np.array([-x_intersect, y_line, 0])
        G = np.array([x_intersect, y_line, 0])

        point_E = Dot(E, color=GREEN, radius=0.08)
        point_G = Dot(G, color=GREEN, radius=0.08)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, DOWN, buff=0.3)
        label_G = Text("G", font_size=42, color=WHITE).next_to(G, DOWN, buff=0.3)

        self.play(FadeIn(point_E), Write(label_E))
        self.play(FadeIn(point_G), Write(label_G))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 步骤5: 作H为EG的中点（命题1.10）
        construction_4 = Text(
            "命题1.10: 作H为EG的中点",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_4))
        self.wait(0.5)

        H = (E + G) / 2  # H是EG的中点
        point_H = Dot(H, color=PURPLE, radius=0.08)
        label_H = Text("H", font_size=42, color=WHITE).next_to(H, DOWN, buff=0.3)

        # 高亮EG
        line_EG = Line(E, G, color=YELLOW, stroke_width=4)
        self.play(Create(line_EG))
        self.wait(0.5)

        self.play(FadeIn(point_H), Write(label_H))
        self.wait(1)

        # 恢复线段颜色
        self.play(line_EG.animate.set_stroke(color=WHITE, width=3))
        self.play(FadeOut(construction_4))

        # 步骤6: 连接CG、CH、CE
        construction_5 = Text(
            "连接CG、CH、CE",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_5))
        self.wait(0.5)

        line_CG = Line(C, G, color=GREEN, stroke_width=3)
        line_CH = Line(C, H, color=RED, stroke_width=3)
        line_CE = Line(C, E, color=GREEN, stroke_width=3)

        self.play(Create(line_CG))
        self.play(Create(line_CH))
        self.play(Create(line_CE))
        self.wait(1)

        self.play(FadeOut(construction_5))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, circle_EFG, line_CD, line_EG,
            line_CG, line_CH, line_CE,
            point_C, point_D, point_E, point_G, point_H,
            label_A, label_B, label_C, label_D, label_E, label_G, label_H
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

        # 证明步骤1: GH等于HE
        self.play(
            line_EG.animate.set_stroke(color=BLUE, width=5)
        )
        proof_1 = Text(
            "∵ GH=HE (H是EG中点)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: HC是公共边
        self.play(
            line_EG.animate.set_stroke(color=WHITE, width=3),
            line_CH.animate.set_stroke(color=PURPLE, width=5)
        )
        proof_2 = Text(
            "HC是公共边",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3: 边GH、HC分别等于边EH、HC
        self.play(
            line_CH.animate.set_stroke(color=RED, width=3)
        )
        proof_3 = Text(
            "边GH、HC分别等于边EH、HC",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4: 底CG等于底CE
        self.play(
            line_CG.animate.set_stroke(color=GREEN, width=5),
            line_CE.animate.set_stroke(color=GREEN, width=5)
        )
        proof_4 = Text(
            "又底CG=底CE (圆的半径)",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5: 三角形全等
        self.play(
            line_CG.animate.set_stroke(color=GREEN, width=3),
            line_CE.animate.set_stroke(color=GREEN, width=3)
        )
        proof_5 = Text(
            "∴ △CHG≌△CHE",
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
            "∴ ∠CHG=∠CHE",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤8: 它们是邻角且相等
        proof_8 = Text(
            "且它们是邻角，和为180°",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 证明步骤9: 每个角为直角
        proof_9 = Text(
            "∴ ∠CHG=∠CHE=90°",
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
        # 高亮垂线CH，淡出辅助圆
        self.play(
            circle_EFG.animate.set_stroke(opacity=0.3),
            line_CD.animate.set_stroke(opacity=0.3),
            line_CG.animate.set_stroke(opacity=0.3),
            line_CE.animate.set_stroke(opacity=0.3),
            line_CH.animate.set_stroke(color=RED, width=5)
        )

        conclusion_line1 = Text(
            "CH是过点C与直线AB成直角的直线",
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
