"""
Book I, Proposition 20
在任意三角形中，任意两边之和大于第三边
In any triangle the sum of any two sides is greater than the remaining one
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition20(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 20)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 20",
            ["在任意三角形中", "任意两边之和大于第三边"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 三角形ABC
        A = np.array([0, 2.0, 0])
        B = np.array([-1.8, -1.2, 0])
        C = np.array([2.2, -1.2, 0])

        # 步骤1: 显示三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)
        line_CA = Line(C, A, color=WHITE, stroke_width=3)

        label_A = Text("A", font_size=42, color=WHITE).next_to(A, LEFT, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, LEFT, buff=0.2)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, RIGHT, buff=0.2)

        construction_1 = Text(
            "三角形ABC",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_AB), Create(line_BC), Create(line_CA))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤2: 延长BA至D，使AD=CA
        # D点在BA延长线上，距离A等于CA的长度
        BA_direction = (A - B) / np.linalg.norm(A - B)
        CA_length = np.linalg.norm(A - C)
        D = A + BA_direction * CA_length

        construction_2 = Text(
            "延长BA至D，使AD=CA",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        # 延长线AD
        line_AD = Line(A, D, color=BLUE, stroke_width=3)
        # D点较高，标签放在右侧
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, RIGHT, buff=0.2)

        self.play(Create(line_AD))
        self.play(Write(label_D))
        self.wait(0.5)

        # D点出现后，文字整体向上移动，保持水平居中
        # 计算D点的y坐标，文字移到其上方（留出足够空间给第二行文字）
        text_y_pos = D[1] + 1.2
        self.play(construction_2.animate.move_to([0, text_y_pos, 0]))

        # 显示AD=CA
        construction_2b = Text(
            "(命题1.3: 截取等长线段)",
            font_size=28,
            color=GRAY
        ).next_to(construction_2, DOWN, buff=0.15)
        self.play(Write(construction_2b))
        self.wait(1)
        self.play(FadeOut(construction_2), FadeOut(construction_2b))

        # 步骤3: 连接DC - 使用更高的位置
        construction_3 = Text(
            "连接DC",
            font_size=38,
            color=YELLOW
        ).move_to([0, text_y_pos, 0])
        self.play(Write(construction_3))
        self.wait(0.5)

        line_DC = Line(D, C, color=GREEN, stroke_width=3)
        self.play(Create(line_DC))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 显示已知和求证 - 使用更高的位置
        given_text = Text(
            "已知: △ABC",
            font_size=38,
            color=YELLOW
        ).move_to([0, text_y_pos, 0])
        prove_text = Text(
            "求证: BA+AC>BC",
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
            line_AD, line_DC,
            label_A, label_B, label_C, label_D
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1: DA=AC，所以∠ADC=∠ACD
        self.play(
            line_AD.animate.set_stroke(color=BLUE, width=4),
            line_CA.animate.set_stroke(color=BLUE, width=4)
        )

        proof_1 = Text(
            "∵ DA=AC (作图)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        proof_2 = Text(
            "∴ ∠ADC=∠ACD",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        proof_2b = Text(
            "(命题1.5: 等腰三角形底角相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_2, DOWN, buff=0.2)
        self.play(Write(proof_2b))
        self.wait(1.5)

        # 恢复颜色
        self.play(
            line_AD.animate.set_stroke(color=BLUE, width=3),
            line_CA.animate.set_stroke(color=WHITE, width=3)
        )

        # 清理部分证明文字
        self.play(
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_2b)
        )
        self.wait(0.5)

        # 证明步骤2: ∠BCD>∠ADC
        proof_3 = Text(
            "∵ ∠BCD=∠BCA+∠ACD",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_3))
        self.wait(1.5)

        proof_4 = Text(
            "∴ ∠BCD>∠ACD=∠ADC",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        proof_4b = Text(
            "(公理5: 整体大于部分)",
            font_size=28,
            color=GRAY
        ).next_to(proof_4, DOWN, buff=0.2)
        self.play(Write(proof_4b))
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_4b)
        )
        self.wait(0.5)

        # 证明步骤3: 在△DCB中，大角对大边
        self.play(
            line_DC.animate.set_stroke(color=GREEN, width=4),
            line_BC.animate.set_stroke(color=YELLOW, width=4)
        )

        proof_5 = Text(
            "在△DCB中，∠BCD>∠BDC",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_5))
        self.wait(1.5)

        proof_6 = Text(
            "∴ DB>BC",
            font_size=32,
            color=YELLOW
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        proof_6b = Text(
            "(命题1.19: 大角对大边)",
            font_size=28,
            color=GRAY
        ).next_to(proof_6, DOWN, buff=0.2)
        self.play(Write(proof_6b))
        self.wait(1.5)

        # 恢复颜色
        self.play(
            line_DC.animate.set_stroke(color=GREEN, width=3),
            line_BC.animate.set_stroke(color=WHITE, width=3)
        )

        # 清理
        self.play(
            FadeOut(proof_5),
            FadeOut(proof_6),
            FadeOut(proof_6b)
        )
        self.wait(0.5)

        # 证明步骤4: DB=BA+AD=BA+AC
        self.play(
            line_AB.animate.set_stroke(color=BLUE, width=4),
            line_AD.animate.set_stroke(color=BLUE, width=4)
        )

        proof_7 = Text(
            "∵ DB=BA+AD",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_7))
        self.wait(1.5)

        proof_8 = Text(
            "又AD=AC",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        proof_9 = Text(
            "∴ BA+AC=DB>BC",
            font_size=32,
            color=YELLOW
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 恢复颜色
        self.play(
            line_AB.animate.set_stroke(color=WHITE, width=3),
            line_AD.animate.set_stroke(color=BLUE, width=3)
        )

        # 清理
        self.play(
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9)
        )
        self.wait(0.5)

        # 证明步骤5: 同理其他两边
        proof_10 = Text(
            "同理可证:",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_10))
        self.wait(1)

        proof_11 = Text(
            "AB+BC>CA",
            font_size=32
        ).next_to(proof_10, DOWN, buff=0.35)
        self.play(Write(proof_11))
        self.wait(1)

        proof_12 = Text(
            "BC+CA>AB",
            font_size=32
        ).next_to(proof_11, DOWN, buff=0.35)
        self.play(Write(proof_12))
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(proof_10),
            FadeOut(proof_11),
            FadeOut(proof_12)
        )
        self.wait(0.5)

        # 5. 结论 - 分两行显示
        # 淡出辅助线
        self.play(
            FadeOut(line_AD),
            FadeOut(line_DC),
            FadeOut(label_D)
        )
        # 更新geometry_group（移除已淡出的元素）
        geometry_group = VGroup(
            line_AB, line_BC, line_CA,
            label_A, label_B, label_C
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "在任意三角形中",
            font_size=36,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "任意两边之和大于第三边",
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
