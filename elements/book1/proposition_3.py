"""
Book I, Proposition 3
两条不相等的线段，在长的线段上可以截取一条线段使它等于另一条线段
Given two unequal straight lines, to cut off from the longer a straight line equal to the shorter
"""
from manim import *
import numpy as np
from utils.base_scene import ElementsScene


class Proposition3(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 3)

        # 显示标题
        title = self.show_title(
            "卷 I, 命题 3",
            ["两条不相等的线段",
            "在长的线段上可以截取一条线段使它等于另一条线段"]
        )

        self.wait(1)
        self.hide_title(title)

        # 1. 给定两条不等的线段 AB (较长) 和 C (较短)
        # AB 是较长的线段
        A = np.array([-3, 0.5, 0])
        B = np.array([3, 0.5, 0])

        # C 是较短的线段
        C_left = np.array([-1.5, -2, 0])
        C_right = np.array([0.5, -2, 0])

        # 显示线段 AB
        line_AB = Line(A, B, color=WHITE)
        label_A = Text("A", font_size=42).next_to(A, LEFT)
        label_B = Text("B", font_size=42).next_to(B, RIGHT)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(0.5)

        # 显示线段 C
        line_C = Line(C_left, C_right, color=WHITE)
        label_C = Text("C", font_size=42).next_to(line_C, DOWN)

        self.play(Create(line_C))
        self.play(Write(label_C))
        self.wait(1)

        # 2. 由 A 作 AD 等于线段 C（命题1.2）
        # 这里使用命题1.2的结果，直接在点A处构造长度等于C的线段AD
        # 注意：D不在AB上，而是通过命题1.2的复杂构造得到的

        length_C = np.linalg.norm(C_right - C_left)

        # D 点的位置：不在AB上，而是在A的其他方向
        # 这里为了简化展示，将D放在A的左上方
        D = A + np.array([-length_C * 0.6, length_C * 0.8, 0])

        point_D = Dot(D, color=YELLOW)
        label_D = Text("D", font_size=42).next_to(D, UP)

        # 显示构造 AD 的过程（提示使用命题1.2）
        prop2_hint = Text("由命题1.2: 在点A作AD等于C", font_size=38, color=BLUE_C).to_edge(UP)
        self.play(Write(prop2_hint))
        self.wait(0.5)

        line_AD = Line(A, D, color=BLUE, stroke_width=4)
        self.play(
            Create(line_AD),
            FadeIn(point_D),
            Write(label_D)
        )
        self.wait(1)
        self.play(FadeOut(prop2_hint))
        self.wait(0.5)

        # 3. 以 A 为圆心，以 AD 为半径画圆 DEF（公设3）
        radius_AD = length_C
        circle_A = Circle(radius=radius_AD, color=BLUE).move_to(A)

        postulate3_hint = Text("公设3: 以任意点为圆心，任意长度为半径画圆",
                              font_size=38, color=BLUE_C).to_edge(UP)
        self.play(Write(postulate3_hint))
        self.wait(0.5)

        self.play(Create(circle_A))
        self.wait(0.5)

        # 添加F点标签（圆上的另一个点，标记圆为DEF）
        # F点在圆的左下角，确保与E不重合
        angle_F = np.radians(240)  # 240度，即左下方向（稍微调整以避免与E重合）
        F = A + np.array([radius_AD * np.cos(angle_F), radius_AD * np.sin(angle_F), 0])
        label_F = Text("F", font_size=42).next_to(F, DOWN + LEFT, buff=0.15)

        self.play(
            Write(label_F)
        )
        self.wait(0.5)

        self.play(FadeOut(postulate3_hint))
        self.wait(0.5)

        # 4. 圆与 AB 的交点 E
        # E是圆DEF与线段AB的交点
        # 计算交点：从A沿AB方向，距离为圆的半径
        direction_AB = (B - A) / np.linalg.norm(B - A)
        E = A + direction_AB * length_C

        point_E = Dot(E, color=RED)
        label_E = Text("E", font_size=42, color=YELLOW).next_to(E, DOWN, buff=0.3)

        # 高亮圆与AB的交点E
        self.play(
            FadeIn(point_E),
            Write(label_E)
        )
        self.wait(0.5)

        # 画出从圆心 A 到 E 的半径，说明AE是半径
        radius_AE = Line(A, E, color=GREEN, stroke_width=4)
        self.play(Create(radius_AE))
        self.wait(1)

        # 准备证明 - 将图形移到上半部分
        geometry_group = VGroup(
            line_AB, line_C, line_AD, radius_AE,
            circle_A,
            point_D, point_E,
            label_A, label_B, label_C, label_D, label_E, label_F
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 证明过程
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1 - A 是圆 DEF 的圆心
        self.play(
            circle_A.animate.set_stroke(color=BLUE, width=4),
        )
        proof_1 = Text(
            "∵ A 是圆 DEF 的圆心",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2 - AE = AD（定义1.15）
        self.play(
            circle_A.animate.set_stroke(color=BLUE, width=2),
            radius_AE.animate.set_stroke(color=GREEN, width=6),
            line_AD.animate.set_stroke(color=GREEN, width=6),
        )
        proof_2 = Text(
            "∴ AE = AD  (定义1.15)",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3 - C = AD
        self.play(
            radius_AE.animate.set_stroke(color=GREEN, width=4),
            line_AD.animate.set_stroke(color=YELLOW, width=6),
            line_C.animate.set_stroke(color=YELLOW, width=6),
        )
        proof_3 = Text(
            "又 ∵ 线段 C = AD  (由作图)",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4 - AE 和 C 都等于 AD
        self.play(
            line_C.animate.set_stroke(color=WHITE, width=2),
        )
        proof_4 = Text(
            "∴ AE 和 C 都等于 AD",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5 - AE = C（公理1: 与同一事物相等的事物彼此相等）
        self.play(
            radius_AE.animate.set_stroke(color=GREEN, width=6),
            line_C.animate.set_stroke(color=GREEN, width=6),
        )
        proof_5 = Text(
            "∴ AE = C  (公理1: 与同量相等的量彼此相等)",
            font_size=32,
            color=YELLOW
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 最终结论
        conclusion_line1 = Text(
            "从 AB 上截取的线段 AE 等于 C",
            font_size=36,
            color=GREEN
        ).next_to(proof_5, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "(Q.E.F.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.wait(2)

        # 结束
        self.play(
            FadeOut(geometry_group),
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2),
        )
        self.wait(1)
