"""
Book I, Proposition 15
如果两直线相交，则它们所成的对顶角相等
If two straight lines intersect, then they make the vertical angles equal to one another
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition15(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 15)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 15",
            ["如果两直线相交", "则它们所成的对顶角相等"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 两条相交的直线AB和CD，交于点E
        A = np.array([-2.8, 2.0, 0])
        B = np.array([2.8, -2.0, 0])
        C = np.array([-2.5, -1.8, 0])
        D = np.array([2.5, 1.8, 0])
        E = np.array([0, 0, 0])  # 交点

        # 步骤1: 显示直线AB
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP + LEFT, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, DOWN + RIGHT, buff=0.2)

        construction_1 = Text(
            "直线AB",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_AB))
        self.play(Write(label_A), Write(label_B))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤2: 显示直线CD，与AB相交于E
        line_CD = Line(C, D, color=GREEN, stroke_width=3)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, DOWN + LEFT, buff=0.2)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, UP + RIGHT, buff=0.2)

        construction_2 = Text(
            "直线CD与AB相交于点E",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        self.play(Create(line_CD))
        self.play(Write(label_C), Write(label_D))
        self.wait(0.5)

        # 标记交点E
        point_E = Dot(E, color=YELLOW, radius=0.08)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, DOWN, buff=0.25)

        self.play(FadeIn(point_E), Write(label_E))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_CD,
            point_E,
            label_A, label_B, label_C, label_D, label_E
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

        # 证明步骤1: AE在CD上侧
        proof_1 = Text(
            "∵ 直线AE在直线CD的上侧",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: 引用命题1.13（第一次）
        proof_2 = Text(
            "∴ ∠CEA+∠AED=两直角",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        proof_3 = Text(
            "(命题1.13: 直线相交形成的邻角和等于两直角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_2, DOWN, buff=0.2)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤3: DE与AB相交
        proof_4 = Text(
            "又∵ 直线DE与AB相交",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤4: 引用命题1.13（第二次）
        proof_5 = Text(
            "∴ ∠AED+∠DEB=两直角",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤5: 公理1 - 两式相等
        proof_6 = Text(
            "∴ ∠CEA+∠AED=∠AED+∠DEB",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        proof_7 = Text(
            "(公理1: 与同量相等的量彼此相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_6, DOWN, buff=0.2)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤6: 公理3 - 同减∠AED
        proof_8 = Text(
            "同减∠AED，得∠CEA=∠BED",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        proof_9 = Text(
            "(公理3: 等量减等量，其差相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_8, DOWN, buff=0.2)
        self.play(Write(proof_9))
        self.wait(1.5)

        # 证明步骤7: 同理
        proof_10 = Text(
            "同理，∠CEB=∠DEA",
            font_size=32
        ).next_to(proof_9, DOWN, buff=0.35)
        self.play(Write(proof_10))
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
            FadeOut(proof_10)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "两直线相交所成的对顶角相等",
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
