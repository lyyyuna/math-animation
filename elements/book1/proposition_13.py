"""
Book I, Proposition 13
一条直线和另一条直线相交所成的角，要么是两个直角，要么它们的和等于两个直角
If a straight line stands on a straight line, then it makes either two right angles or angles whose sum equals two right angles
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition13(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 13)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 13",
            ["一条直线和另一条直线相交所成的角","要么是两个直角，要么和等于两个直角"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点
        C = np.array([3.5, -0.5, 0])
        D = np.array([-3.5, -0.5, 0])
        B = np.array([0, -0.5, 0])
        A = np.array([1.5, 2.5, 0])

        # 步骤1: 显示直线CD
        line_CD = Line(C, D, color=WHITE, stroke_width=3)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, RIGHT)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, LEFT)

        self.play(Create(line_CD))
        self.play(Write(label_C), Write(label_D))
        self.wait(0.5)

        # 步骤2: 显示点B在CD上
        point_B = Dot(B, color=YELLOW, radius=0.08)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, DOWN, buff=0.3)

        self.play(FadeIn(point_B), Write(label_B))
        self.wait(0.5)

        # 步骤3: 从B向上作直线到A
        line_BA = Line(B, A, color=WHITE, stroke_width=3)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP, buff=0.2)

        construction_1 = Text(
            "直线AB与CD相交于B",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_BA))
        self.play(Write(label_A))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤4: 过B作BE垂直于CD（命题1.11）
        construction_2 = Text(
            "命题1.11: 过B作BE垂直于CD",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        E = np.array([0, 2, 0])  # BE垂直于CD
        line_BE = Line(B, E, color=RED, stroke_width=3)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, UP, buff=0.2)

        self.play(Create(line_BE))
        self.play(Write(label_E))
        self.wait(0.5)

        # 显示直角标记
        right_angle_CBE = RightAngle(
            Line(B, C),
            Line(B, E),
            length=0.3,
            color=YELLOW,
            stroke_width=2,
            quadrant=(1, 1)
        )
        right_angle_EBD = RightAngle(
            Line(B, D),
            Line(B, E),
            length=0.3,
            color=YELLOW,
            stroke_width=2,
            quadrant=(-1, 1)
        )

        self.play(Create(right_angle_CBE), Create(right_angle_EBD))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_CD, line_BA, line_BE,
            point_B,
            label_A, label_B, label_C, label_D, label_E,
            right_angle_CBE, right_angle_EBD
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

        # 证明步骤1: ∠CBE和∠EBD是两个直角
        self.play(
            right_angle_CBE.animate.set_stroke(color=YELLOW, width=4),
            right_angle_EBD.animate.set_stroke(color=YELLOW, width=4)
        )
        proof_1 = Text(
            "∵ BE⊥CD",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        proof_2 = Text(
            "∴ ∠CBE和∠EBD是两个直角",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤2: ∠CBE = ∠CBA + ∠ABE
        self.play(
            right_angle_CBE.animate.set_stroke(color=YELLOW, width=2),
            right_angle_EBD.animate.set_stroke(color=YELLOW, width=2)
        )
        proof_3 = Text(
            "∠CBE=∠CBA+∠ABE",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤3: 在等式两边都加上∠EBD
        proof_4 = Text(
            "在等式两边都加上∠EBD:",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1)

        proof_5 = Text(
            "∠CBE+∠EBD=∠CBA+∠ABE+∠EBD",
            font_size=30
        ).next_to(proof_4, DOWN, buff=0.3)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤4: 引用公理2
        proof_6 = Text(
            "(公理2: 等量加等量，和相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_5, DOWN, buff=0.3)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤5: 同理，∠DBA = ∠DBE + ∠EBA
        proof_7 = Text(
            "同理，∠DBA=∠DBE+∠EBA",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤6: 在等式两边都加上∠ABC
        proof_8 = Text(
            "在等式两边都加上∠ABC:",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1)

        proof_9 = Text(
            "∠DBA+∠ABC=∠DBE+∠EBA+∠ABC",
            font_size=30
        ).next_to(proof_8, DOWN, buff=0.3)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 证明步骤7: 因此两式相等
        proof_10 = Text(
            "∴ ∠CBE+∠EBD=∠DBA+∠ABC",
            font_size=32
        ).next_to(proof_9, DOWN, buff=0.35)
        self.play(Write(proof_10))
        self.wait(1.5)

        # 证明步骤8: 引用公理1
        proof_11 = Text(
            "(公理1: 等于同量的量彼此相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_10, DOWN, buff=0.3)
        self.play(Write(proof_11))
        self.wait(1.5)

        # 证明步骤9: 又∠CBE+∠EBD是两个直角
        self.play(
            right_angle_CBE.animate.set_stroke(color=YELLOW, width=4),
            right_angle_EBD.animate.set_stroke(color=YELLOW, width=4)
        )
        proof_12 = Text(
            "又∠CBE+∠EBD=两个直角",
            font_size=32
        ).next_to(proof_11, DOWN, buff=0.35)
        self.play(Write(proof_12))
        self.wait(1.5)

        # 证明步骤10: 结论
        self.play(
            right_angle_CBE.animate.set_stroke(color=YELLOW, width=2),
            right_angle_EBD.animate.set_stroke(color=YELLOW, width=2)
        )
        proof_13 = Text(
            "∴ ∠DBA+∠ABC=两个直角",
            font_size=32
        ).next_to(proof_12, DOWN, buff=0.35)
        self.play(Write(proof_13))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        # 先隐去前面的证明过程
        self.play(
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
            FadeOut(proof_11),
            FadeOut(proof_12),
            FadeOut(proof_13)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "两条直线相交时，邻角之和等于两直角",
            font_size=36,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "(Q.E.D.)",
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
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
