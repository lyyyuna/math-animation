"""
Book I, Proposition 19
在任意三角形中，大角对大边
In any triangle the greater angle is opposite the greater side
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition19(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 19)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 19",
            ["在任意三角形中", "大角对大边"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 三角形ABC，∠ABC > ∠BCA
        # 要使∠ABC > ∠BCA，需要AC > AB（大角对大边）
        A = np.array([0, 1.8, 0])
        B = np.array([-1.5, -1.5, 0])  # B靠近A，使AB较短
        C = np.array([2.8, -1.5, 0])   # C远离A，使AC较长

        # 步骤1: 显示三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)
        line_CA = Line(C, A, color=WHITE, stroke_width=3)

        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, LEFT, buff=0.2)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, RIGHT, buff=0.2)

        construction_1 = Text(
            "三角形ABC，其中∠ABC>∠BCA",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_AB), Create(line_BC), Create(line_CA))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 显示已知和求证
        given_text = Text(
            "已知: ∠ABC>∠BCA",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        prove_text = Text(
            "求证: AC>AB",
            font_size=38,
            color=YELLOW
        ).next_to(given_text, DOWN, buff=0.15)

        self.play(Write(given_text))
        self.play(Write(prove_text))
        self.wait(2)
        self.play(FadeOut(given_text), FadeOut(prove_text))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_BC, line_CA,
            label_A, label_B, label_C
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 使用反证法
        proof_title = Text("证明 (反证法):", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1: 假设AC不大于AB
        proof_1 = Text(
            "假设AC不大于AB",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        proof_2 = Text(
            "即AC=AB或AC<AB",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤2: 情况1 - AC=AB
        self.play(
            line_CA.animate.set_stroke(color=BLUE, width=4),
            line_AB.animate.set_stroke(color=BLUE, width=4)
        )

        proof_3 = Text(
            "情况1: 若AC=AB",
            font_size=32,
            color=BLUE
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        proof_4 = Text(
            "则∠ABC=∠BCA",
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

        proof_6 = Text(
            "与已知∠ABC>∠BCA矛盾",
            font_size=32,
            color=RED
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 恢复颜色并清理，为下一部分腾出空间
        self.play(
            line_CA.animate.set_stroke(color=WHITE, width=3),
            line_AB.animate.set_stroke(color=WHITE, width=3)
        )

        self.play(
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_6)
        )
        self.wait(0.5)

        # 证明步骤3: 情况2 - AC<AB
        self.play(
            line_CA.animate.set_stroke(color=GREEN, width=4),
            line_AB.animate.set_stroke(color=GREEN, width=4)
        )

        proof_7 = Text(
            "情况2: 若AC<AB",
            font_size=32,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_7))
        self.wait(1.5)

        proof_8 = Text(
            "则∠ABC<∠BCA",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        proof_9 = Text(
            "(命题1.18: 大边对大角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_8, DOWN, buff=0.2)
        self.play(Write(proof_9))
        self.wait(1.5)

        proof_10 = Text(
            "与已知∠ABC>∠BCA矛盾",
            font_size=32,
            color=RED
        ).next_to(proof_9, DOWN, buff=0.35)
        self.play(Write(proof_10))
        self.wait(1.5)

        # 恢复颜色
        self.play(
            line_CA.animate.set_stroke(color=WHITE, width=3),
            line_AB.animate.set_stroke(color=WHITE, width=3)
        )

        # 清理并显示结论
        self.play(
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9),
            FadeOut(proof_10)
        )
        self.wait(0.5)

        # 证明步骤4: 结论
        proof_11 = Text(
            "∴ AC既不等于AB，也不小于AB",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_11))
        self.wait(1.5)

        proof_12 = Text(
            "∴ AC>AB",
            font_size=32,
            color=YELLOW
        ).next_to(proof_11, DOWN, buff=0.35)

        # 高亮AC边
        self.play(
            line_CA.animate.set_stroke(color=YELLOW, width=4),
            Write(proof_12)
        )
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        self.play(
            FadeOut(proof_11),
            FadeOut(proof_12)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "在任意三角形中",
            font_size=36,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "较大的角所对的边较大",
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
