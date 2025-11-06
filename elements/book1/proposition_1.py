"""
Book I, Proposition 1
在给定的有限直线上构造一个等边三角形
On a given finite straight line to construct an equilateral triangle
"""
from manim import *
from utils.base_scene import ElementsScene
from utils.geometry import construct_equilateral_triangle


class Proposition1(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 1)

        # 显示标题
        title = self.show_title(
            "卷 I, 命题 1",
            "在给定的有限直线上构造一个等边三角形"
        )

        self.wait(1)
        self.hide_title(title)

        # 1. 给定线段 AB
        A = np.array([-2, 0, 0])
        B = np.array([2, 0, 0])

        line_AB = Line(A, B, color=WHITE)
        label_A = Text("A", font_size=42).next_to(A, DOWN)
        label_B = Text("B", font_size=42).next_to(B, DOWN)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(1)

        # 2. 以 A 为圆心，AB 为半径画圆
        radius = np.linalg.norm(B - A)
        circle_A = Circle(radius=radius, color=BLUE).move_to(A)

        self.play(Create(circle_A))
        self.wait(0.5)

        # 3. 以 B 为圆心，BA 为半径画圆
        circle_B = Circle(radius=radius, color=GREEN).move_to(B)

        self.play(Create(circle_B))
        self.wait(1)

        # 4. 找到两圆交点 C
        C = construct_equilateral_triangle(A, B)
        point_C = Dot(C, color=YELLOW)
        label_C = Text("C", font_size=42).next_to(C, UP)

        self.play(FadeIn(point_C), Write(label_C))
        self.wait(0.5)

        # 5. 连接 AC 和 BC 形成三角形
        line_AC = Line(A, C, color=YELLOW)
        line_BC = Line(B, C, color=YELLOW)

        self.play(Create(line_AC), Create(line_BC))
        self.wait(1)

        # 6. 高亮三角形
        triangle = Polygon(A, B, C, color=YELLOW, fill_opacity=0.2)
        self.play(
            FadeOut(line_AB),
        )
        self.play(Create(triangle))
        self.wait(1)

        # 7. 准备证明 - 将图形移到上半部分（手机竖屏布局）
        geometry_group = VGroup(
            triangle, circle_A, circle_B,
            line_AC, line_BC,
            point_C, label_A, label_B, label_C
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 8. 证明过程 - 文字显示在下半部分
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 高亮圆A和线段AC
        self.play(
            circle_A.animate.set_stroke(color=BLUE, width=4),
            line_AC.animate.set_stroke(color=BLUE, width=4)
        )
        proof_1 = Text(
            "AC = AB (圆A的半径)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 恢复圆A和线段AC，高亮圆B和线段BC
        self.play(
            circle_A.animate.set_stroke(color=BLUE, width=2),
            line_AC.animate.set_stroke(color=YELLOW, width=2),
            circle_B.animate.set_stroke(color=GREEN, width=4),
            line_BC.animate.set_stroke(color=GREEN, width=4)
        )
        proof_2 = Text(
            "BC = BA (圆B的半径)",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 恢复所有，显示结论
        self.play(
            circle_B.animate.set_stroke(color=GREEN, width=2),
            line_BC.animate.set_stroke(color=YELLOW, width=2)
        )
        proof_3 = Text(
            "∴ AC = AB = BC",
            font_size=32,
            color=YELLOW
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1)

        # 淡出圆，强调三角形
        self.play(
            FadeOut(circle_A),
            FadeOut(circle_B)
        )

        # 9. 显示最终结论 - 分两行显示
        conclusion_line1 = Text(
            "△ABC 是等边三角形",
            font_size=36,
            color=GREEN
        ).next_to(proof_3, DOWN, buff=0.4)

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
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
