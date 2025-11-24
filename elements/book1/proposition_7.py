from manim import *
from utils.base_scene import ElementsScene

class Proposition7(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 7)

        # 1. 显示标题
        title = self.show_title(
            "卷一, 命题 7",
            ["过线段两端点引出的两条线段交于一点","则不可能在该线段(从它的两个端点)的同侧","作出相交于另一点的另两条线段","分别等于前两条线段"],
            wait_time=4,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点
        A = np.array([-2, -1, 0])
        B = np.array([2, -1, 0])
        C = np.array([0, 2, 0])
        # D点：与B点x坐标一致，与C点y坐标一致
        D = np.array([2, 2, 0])

        # 作线段AB
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, LEFT, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, RIGHT, buff=0.2)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(0.5)

        # 作第一对线段：AC和BC相交于C
        line_AC = Line(A, C, color=BLUE, stroke_width=3)
        line_BC = Line(B, C, color=BLUE, stroke_width=3)
        label_C = Text("C", font_size=42, color=BLUE).next_to(C, UP, buff=0.2)

        explanation_1 = Text(
            "设AC、BC相交于点C",
            font_size=38,
            color=BLUE
        ).to_edge(UP)

        self.play(Write(explanation_1))
        self.play(Create(line_AC), Create(line_BC))
        self.play(Write(label_C))
        self.wait(1)
        self.play(FadeOut(explanation_1))

        # 假设：作第二对线段AD和BD相交于D（也在同侧，但在CB外侧）
        line_AD = Line(A, D, color=GREEN, stroke_width=3)
        line_BD = Line(B, D, color=GREEN, stroke_width=3)
        label_D = Text("D", font_size=42, color=GREEN).next_to(D, RIGHT, buff=0.2)

        explanation_2 = Text(
            "假设: 存在AD、DB相交于点D(同侧)",
            font_size=38,
            color=GREEN
        ).to_edge(UP)

        self.play(Write(explanation_2))
        self.play(Create(line_AD), Create(line_BD))
        self.play(Write(label_D))
        self.wait(1)
        self.play(FadeOut(explanation_2))

        # 添加相等标记
        explanation_3 = Text(
            "且CA=DA，CB=DB",
            font_size=38,
            color=YELLOW
        ).to_edge(UP)

        self.play(Write(explanation_3))
        self.wait(1.5)
        self.play(FadeOut(explanation_3))

        # 连接CD (公设1)
        line_CD = Line(C, D, color=RED, stroke_width=3)

        explanation_4 = Text(
            "连接CD (公设1)",
            font_size=38,
            color=RED
        ).to_edge(UP)

        self.play(Write(explanation_4))
        self.play(Create(line_CD))
        self.wait(1)
        self.play(FadeOut(explanation_4))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_AC, line_BC, line_AD, line_BD, line_CD,
            label_A, label_B, label_C, label_D
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 反证法
        proof_title = Text("证明(反证法):", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1：AC=AD
        self.play(
            line_AC.animate.set_stroke(color=BLUE, width=5),
            line_AD.animate.set_stroke(color=GREEN, width=5)
        )
        proof_1 = Text(
            "∵ AC=AD (假设)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2：等腰三角形性质
        proof_2 = Text(
            "∴ ∠ACD=∠ADC",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        proof_2_note = Text(
            "(命题1.5: 等边对等角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_2, DOWN, buff=0.2)
        self.play(Write(proof_2))
        self.play(Write(proof_2_note))
        self.wait(1.5)

        # 证明步骤3：角度关系
        self.play(
            line_AC.animate.set_stroke(color=BLUE, width=3),
            line_AD.animate.set_stroke(color=GREEN, width=3),
            line_CD.animate.set_stroke(color=RED, width=5)
        )
        proof_3 = Text(
            "∴ ∠ADC>∠DCB",
            font_size=32
        ).next_to(proof_2_note, DOWN, buff=0.35)
        proof_3_note = Text(
            "(公理5: 整体大于部分)",
            font_size=28,
            color=GRAY
        ).next_to(proof_3, DOWN, buff=0.2)
        self.play(Write(proof_3))
        self.play(Write(proof_3_note))
        self.wait(1.5)

        # 证明步骤4：推出CDB>DCB
        proof_4 = Text(
            "进而 ∠CDB>∠DCB",
            font_size=32
        ).next_to(proof_3_note, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5：CB=DB
        self.play(
            line_CD.animate.set_stroke(color=RED, width=3),
            line_BC.animate.set_stroke(color=BLUE, width=5),
            line_BD.animate.set_stroke(color=GREEN, width=5)
        )
        proof_5 = Text(
            "又∵ CB=DB (假设)",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤6：等腰三角形性质
        proof_6 = Text(
            "∴ ∠CDB=∠DCB",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        proof_6_note = Text(
            "(命题1.5: 等边对等角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_6, DOWN, buff=0.2)
        self.play(Write(proof_6))
        self.play(Write(proof_6_note))
        self.wait(1.5)

        # 证明步骤7：矛盾
        self.play(
            line_BC.animate.set_stroke(color=BLUE, width=3),
            line_BD.animate.set_stroke(color=GREEN, width=3)
        )
        proof_7 = Text(
            "但前面得出∠CDB>∠DCB",
            font_size=32,
            color=RED
        ).next_to(proof_6_note, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        proof_8 = Text(
            "矛盾！假设不成立",
            font_size=32,
            color=RED
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(2)

        # 淡出所有证明文字，准备显示结论
        self.play(
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_2_note),
            FadeOut(proof_3),
            FadeOut(proof_3_note),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_6),
            FadeOut(proof_6_note),
            FadeOut(proof_7),
            FadeOut(proof_8)
        )
        self.wait(0.5)

        # 5. 结论
        conclusion_line1 = Text(
            "过线段两端点引出的两条线段交于一点，",
            font_size=32,
            color=GREEN
        ).shift(DOWN * 1.8)

        conclusion_line2 = Text(
            "则不可能在该线段同侧作出相交于另一点的",
            font_size=32,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.3)

        conclusion_line3 = Text(
            "另两条线段，分别等于前两条线段",
            font_size=32,
            color=GREEN
        ).next_to(conclusion_line2, DOWN, buff=0.3)

        conclusion_line4 = Text(
            "(Q.E.D.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line3, DOWN, buff=0.3)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.play(Write(conclusion_line3))
        self.play(Write(conclusion_line4))
        self.wait(2)

        # 6. 结束
        self.play(
            FadeOut(geometry_group),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2),
            FadeOut(conclusion_line3),
            FadeOut(conclusion_line4)
        )
        self.wait(1)
