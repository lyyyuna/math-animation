"""
Book I, Proposition 16
在任意三角形中，延长一边，所形成的外角大于任何一个内对角
In any triangle, if one of the sides is produced, then the exterior angle is greater than either of the interior and opposite angles
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition16(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 16)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 16",
            ["在任意三角形中，延长一边", "所形成的外角大于任何一个内对角"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 三角形ABC
        A = np.array([-1.5, 2.0, 0])
        B = np.array([-3.0, -1.0, 0])
        C = np.array([1.5, -1.0, 0])

        # 步骤1: 显示三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)
        line_CA = Line(C, A, color=WHITE, stroke_width=3)

        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, LEFT, buff=0.2)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, DOWN, buff=0.2)

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

        # 步骤2: 延长BC至D
        D = np.array([4.5, -1.0, 0])
        line_CD = Line(C, D, color=BLUE, stroke_width=3)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, RIGHT, buff=0.2)

        construction_2 = Text(
            "延长BC至点D",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        self.play(Create(line_CD))
        self.play(Write(label_D))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 步骤3: 取AC的中点E（命题1.10）
        E = (A + C) / 2
        point_E = Dot(E, color=YELLOW, radius=0.08)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, UP, buff=0.15)

        construction_3 = Text(
            "取AC的中点E (命题1.10 二等分线段)",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        self.play(FadeIn(point_E), Write(label_E))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 步骤4: 连接BE并延长至F，使EF=BE（命题1.3）
        BE_vec = E - B
        F = E + BE_vec
        line_BE = Line(B, E, color=GREEN, stroke_width=3)
        line_EF = Line(E, F, color=GREEN, stroke_width=3)
        label_F = Text("F", font_size=42, color=WHITE).next_to(F, DOWN + RIGHT, buff=0.2)

        construction_4a = Text(
            "连接BE并延长至F，使EF=BE",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        construction_4b = Text(
            "(命题1.3: 从较长线段截取等于较短线段的一段)",
            font_size=32,
            color=GRAY
        ).next_to(construction_4a, DOWN, buff=0.15)
        self.play(Write(construction_4a))
        self.play(Write(construction_4b))
        self.wait(0.5)

        self.play(Create(line_BE), Create(line_EF))
        self.play(Write(label_F))
        self.wait(1)
        self.play(FadeOut(construction_4a), FadeOut(construction_4b))

        # 步骤5: 连接FC
        line_FC = Line(F, C, color=ORANGE, stroke_width=3)

        construction_5 = Text(
            "连接FC",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_5))
        self.wait(0.5)

        self.play(Create(line_FC))
        self.wait(1)
        self.play(FadeOut(construction_5))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_BC, line_CA, line_CD,
            line_BE, line_EF, line_FC,
            point_E,
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

        # 证明步骤1: AE=EC, BE=EF
        proof_1 = Text(
            "∵ AE=EC (E是AC中点), BE=EF (作图)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: 对顶角相等
        proof_2 = Text(
            "且∠AEB=∠FEC (对顶角)",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        proof_3 = Text(
            "(命题1.15: 两直线相交所成对顶角相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_2, DOWN, buff=0.2)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤3: 三角形全等
        proof_4 = Text(
            "∴ △ABE≌△CFE",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        proof_5 = Text(
            "(命题1.4: 两边及其夹角对应相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_4, DOWN, buff=0.2)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤4: 角相等
        proof_6 = Text(
            "∴ ∠BAE=∠ECF",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤5: 角度大小关系
        proof_7 = Text(
            "∵ ∠ACD>∠ECF",
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

        # 证明步骤6: 结论1
        proof_9 = Text(
            "∴ ∠ACD>∠BAE",
            font_size=32
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 先隐去部分证明过程，为同理部分腾出空间
        self.play(
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9)
        )
        self.wait(0.5)

        # 证明步骤7: 同理
        proof_10 = Text(
            "同理，二等分BC",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_10))
        self.wait(1.5)

        proof_11 = Text(
            "可证∠ACD>∠ABC",
            font_size=32
        ).next_to(proof_10, DOWN, buff=0.35)
        self.play(Write(proof_11))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        self.play(
            FadeOut(proof_10),
            FadeOut(proof_11)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "三角形的外角大于任何一个内对角",
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
