"""
Book I, Proposition 18
在任意三角形中，大边对大角
In any triangle the greater side subtends the greater angle
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition18(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 18)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 18",
            ["在任意三角形中", "大边对大角"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 三角形ABC，AC > AB
        A = np.array([-1.0, 2.0, 0])
        B = np.array([-3.0, -1.0, 0])
        C = np.array([2.5, -1.0, 0])  # C距离A更远，使AC > AB

        # 步骤1: 显示三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)
        line_CA = Line(C, A, color=WHITE, stroke_width=3)

        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, LEFT, buff=0.2)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, RIGHT, buff=0.2)

        construction_1 = Text(
            "三角形ABC，其中AC>AB",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_AB), Create(line_BC), Create(line_CA))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤2: 在AC上取点D，使AD=AB（命题1.3）
        AB_length = np.linalg.norm(A - B)
        AC_direction = (C - A) / np.linalg.norm(C - A)
        D = A + AC_direction * AB_length

        point_D = Dot(D, color=YELLOW, radius=0.08)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, RIGHT + UP, buff=0.15)

        construction_2a = Text(
            "在AC上取点D，使AD=AB",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        construction_2b = Text(
            "(命题1.3: 从较长线段截取等于较短线段)",
            font_size=32,
            color=GRAY
        ).next_to(construction_2a, DOWN, buff=0.15)
        self.play(Write(construction_2a))
        self.play(Write(construction_2b))
        self.wait(0.5)

        self.play(FadeIn(point_D), Write(label_D))
        self.wait(1)
        self.play(FadeOut(construction_2a), FadeOut(construction_2b))

        # 步骤3: 连接BD
        line_BD = Line(B, D, color=GREEN, stroke_width=3)

        construction_3 = Text(
            "连接BD",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        self.play(Create(line_BD))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_BC, line_CA, line_BD,
            point_D,
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

        # 证明步骤1: ∠ADB是外角
        proof_1 = Text(
            "∵ ∠ADB是△BCD的外角",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: 外角大于内对角
        proof_2 = Text(
            "∴ ∠ADB>∠DCB",
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

        # 证明步骤3: 等腰三角形底角相等
        proof_4 = Text(
            "∵ AB=AD，∴ ∠ADB=∠ABD",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        proof_5 = Text(
            "(命题1.5: 等腰三角形底角相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_4, DOWN, buff=0.2)
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

        # 证明步骤4: 推导结论
        proof_6 = Text(
            "∴ ∠ABD>∠ACB",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_6))
        self.wait(1.5)

        proof_7 = Text(
            "∵ ∠ABC>∠ABD",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        proof_8 = Text(
            "(公理5: 整体大于部分)",
            font_size=28,
            color=GRAY
        ).next_to(proof_7, DOWN, buff=0.2)
        self.play(Write(proof_8))
        self.wait(1.5)

        proof_9 = Text(
            "∴ ∠ABC>∠ACB",
            font_size=32
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        self.play(
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "在任意三角形中",
            font_size=36,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "较大的边所对的角较大",
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
