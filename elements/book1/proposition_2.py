"""
Book I, Proposition 2
从给定的点作一条直线等于给定的直线
To place a straight line equal to a given straight line at a given point
"""
from manim import *
import numpy as np
from utils.base_scene import ElementsScene
from utils.geometry import construct_equilateral_triangle


class Proposition2(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 2)

        # 显示标题
        title = self.show_title(
            "卷 I, 命题 2",
            "从给定的点作一条直线等于给定的直线"
        )

        self.wait(1)
        self.hide_title(title)

        # 1. 给定点 A 和线段 BC（缩小距离避免圆超出屏幕）
        A = np.array([-1.5, -0.5, 0])
        B = np.array([1, 0, 0])
        C = np.array([2.2, 0, 0])

        # 显示点 A
        point_A = Dot(A, color=YELLOW)
        label_A = Text("A", font_size=42).next_to(A, LEFT)

        self.play(FadeIn(point_A), Write(label_A))
        self.wait(0.5)

        # 显示线段 BC
        line_BC = Line(B, C, color=WHITE)
        label_B = Text("B", font_size=42).next_to(B, DOWN)
        label_C = Text("C", font_size=42).next_to(C, UP)  # C标签在上方，避免与G重叠

        self.play(Create(line_BC))
        self.play(Write(label_B), Write(label_C))
        self.wait(1)

        # 2. 连接 AB
        line_AB = Line(A, B, color=WHITE)
        self.play(Create(line_AB))
        self.wait(0.5)

        # 3. 在 AB 上构造等边三角形 ABD（使用命题1）
        D = construct_equilateral_triangle(A, B)

        # 以 A 为圆心，AB 为半径画圆（辅助）
        radius_AB = np.linalg.norm(B - A)
        circle_A = Circle(radius=radius_AB, color=BLUE, stroke_opacity=0.3).move_to(A)

        # 以 B 为圆心，BA 为半径画圆（辅助）
        circle_B = Circle(radius=radius_AB, color=GREEN, stroke_opacity=0.3).move_to(B)

        self.play(Create(circle_A), Create(circle_B))
        self.wait(0.5)

        # 显示点 D
        point_D = Dot(D, color=YELLOW)
        label_D = Text("D", font_size=42).next_to(D, UP)

        line_AD = Line(A, D, color=YELLOW)
        line_BD = Line(B, D, color=YELLOW)

        self.play(
            Create(line_AD),
            Create(line_BD),
            FadeIn(point_D),
            Write(label_D)
        )
        self.wait(1)

        # 淡化辅助圆
        self.play(FadeOut(circle_A), FadeOut(circle_B))

        # 4. 延长 DA 到 L，延长 DB 到 M
        # 计算延长方向
        dir_DA = (A - D) / np.linalg.norm(A - D)
        dir_DB = (B - D) / np.linalg.norm(B - D)

        L = D + dir_DA * radius_AB * 2.5
        M = D + dir_DB * (np.linalg.norm(C - B) + radius_AB) * 1.2

        line_DL = Line(D, L, color=WHITE)
        line_DM = Line(D, M, color=WHITE)

        label_L = Text("L", font_size=42).next_to(L, LEFT)
        label_M = Text("M", font_size=42).next_to(M, RIGHT)

        self.play(Create(line_DL))
        self.play(Write(label_L))
        self.wait(0.5)

        self.play(Create(line_DM))
        self.play(Write(label_M))
        self.wait(1)

        # 5. 以 B 为圆心，BC 为半径画圆
        radius_BC = np.linalg.norm(C - B)
        circle_B2 = Circle(radius=radius_BC, color=GREEN).move_to(B)

        self.play(Create(circle_B2))
        self.wait(0.5)

        # 6. 找到圆与 DM 的交点 G
        # 计算交点
        t = radius_BC  # 参数化距离
        G = B + dir_DB * t

        point_G = Dot(G, color=RED)
        label_G = Text("G", font_size=42).next_to(G, UP)

        self.play(FadeIn(point_G), Write(label_G))
        self.wait(0.5)

        # 7. 以 D 为圆心，DG 为半径画圆
        radius_DG = np.linalg.norm(G - D)
        circle_D = Circle(radius=radius_DG, color=BLUE).move_to(D)

        self.play(Create(circle_D))
        self.wait(0.5)

        # 8. 找到圆与 DL 的交点 H
        H = D + dir_DA * radius_DG

        point_H = Dot(H, color=RED)
        label_H = Text("H", font_size=42).next_to(H, LEFT)

        self.play(FadeIn(point_H), Write(label_H))
        self.wait(1)

        # 9. 淡化圆，保留辅助线段和点以便证明
        self.play(
            circle_B2.animate.set_stroke(opacity=0.2),
            circle_D.animate.set_stroke(opacity=0.2),
        )

        # 10. 高亮线段 AH
        line_AH = Line(A, H, color=YELLOW, stroke_width=6)

        self.play(Create(line_AH))
        self.play(
            point_H.animate.set_color(YELLOW),
        )
        self.wait(1)

        # 准备证明 - 将图形移到上半部分（保留所有辅助线）
        geometry_group = VGroup(
            line_BC, line_AB, line_AH,
            line_DL, line_DM, line_AD, line_BD,
            circle_B2, circle_D,
            point_A, point_H, point_D, point_G,
            label_A, label_B, label_C, label_H, label_D, label_G, label_L, label_M
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

        # 证明步骤1 - 高亮等边三角形的两边
        self.play(
            line_AD.animate.set_stroke(color=BLUE, width=4),
            line_BD.animate.set_stroke(color=BLUE, width=4),
        )
        proof_1 = Text(
            "DA = DB (等边△ABD)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2 - 高亮圆D和半径
        self.play(
            line_AD.animate.set_stroke(color=WHITE, width=2),
            line_BD.animate.set_stroke(color=WHITE, width=2),
            circle_D.animate.set_stroke(color=BLUE, width=3, opacity=0.8),
        )
        proof_2 = Text(
            "DH = DG (圆D的半径)",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3 - 恢复圆D
        self.play(
            circle_D.animate.set_stroke(opacity=0.2, width=2),
        )
        proof_3 = Text(
            "∴ AH = DH - DA = DG - DB = BG",
            font_size=32,
            color=YELLOW
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1)

        # 证明步骤4 - 高亮圆B和BG
        self.play(
            circle_B2.animate.set_stroke(color=GREEN, width=3, opacity=0.8),
        )
        proof_4 = Text(
            "BG = BC (圆B的半径)",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 恢复圆B
        self.play(
            circle_B2.animate.set_stroke(opacity=0.2, width=2),
        )

        # 最终结论
        conclusion_line1 = Text(
            "∴ AH = BC",
            font_size=36,
            color=GREEN
        ).next_to(proof_4, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "(Q.E.F.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.wait(2)

        # 强调结论：只保留AH和BC两条线段及相关点，淡出其他所有元素
        self.play(
            # 淡出所有辅助线和辅助点
            FadeOut(line_AB),
            FadeOut(line_DL),
            FadeOut(line_DM),
            FadeOut(line_AD),
            FadeOut(line_BD),
            FadeOut(circle_B2),
            FadeOut(circle_D),
            FadeOut(point_D),
            FadeOut(point_G),
            FadeOut(label_D),
            FadeOut(label_G),
            FadeOut(label_L),
            FadeOut(label_M),
            # 保留 label_B，因为BC线段要显示到最后
            # 淡出证明文字
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2),
        )
        self.wait(0.5)

        # 高亮最终结果：AH = BC
        self.play(
            line_AH.animate.set_stroke(color=GREEN, width=8),
            line_BC.animate.set_stroke(color=GREEN, width=8),
        )

        # 显示最终结论文字
        final_conclusion = Text(
            "AH = BC",
            font_size=48,
            color=GREEN
        ).to_edge(DOWN, buff=1)
        self.play(Write(final_conclusion))
        self.wait(2)

        # 结束
        self.play(
            FadeOut(line_BC),
            FadeOut(line_AH),
            FadeOut(point_A),
            FadeOut(point_H),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            FadeOut(label_H),
            FadeOut(final_conclusion)
        )
        self.wait(1)
