"""
Book I, Proposition 14
如果过某一直线上任意一点且在该直线的两边有两条直线，且这两条直线与该直线所形成的两邻角之和等于两直角和，那么这两条直线在同一直线上
If two straight lines, not lying on the same side, make adjacent angles with a straight line at a point on it, equal to two right angles, then the two straight lines are in a straight line with one another
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition14(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 14)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 14",
            ["如果过某一直线上任意一点", "且在该直线的两边有两条直线", "且这两条直线与该直线所形成的两邻角之和", "等于两直角和", "那么这两条直线在同一直线上"],
            wait_time=4,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点（CBD在水平直线上，A在上方）
        C = np.array([-2.9, 0, 0])    # 水平线左端
        B = np.array([0, 0, 0])       # 水平线中点
        D = np.array([2.9, 0, 0])     # 水平线右端
        A = np.array([-2.2, 2.5, 0])  # 上方

        # 计算射线AB（从A开始，通过B延伸）
        # 方向向量：从A到B
        direction = B - A
        # 归一化
        direction_norm = direction / np.linalg.norm(direction)
        # 从B继续延长
        right_end = B + direction_norm * 4.0

        # 步骤1: 显示直线AB（画成射线），点B和A一起出现
        line_AB = Line(A, right_end, color=WHITE, stroke_width=3)
        point_B = Dot(B, color=YELLOW, radius=0.08)
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, LEFT, buff=0.2)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, DOWN, buff=0.3)

        construction_1 = Text(
            "直线AB",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(Create(line_AB), FadeIn(point_B))
        self.play(Write(label_A), Write(label_B))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 步骤2: 从B引出直线BC（AB下方）
        line_BC = Line(B, C, color=GREEN, stroke_width=3)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, DOWN, buff=0.2)

        construction_2 = Text(
            "从B引出直线BC",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        self.play(Create(line_BC))
        self.play(Write(label_C))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 步骤3: 从B引出直线BD（CD下方）
        line_BD = Line(B, D, color=BLUE, stroke_width=3)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, DOWN, buff=0.2)

        construction_3 = Text(
            "从B引出直线BD",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        self.play(Create(line_BD))
        self.play(Write(label_D))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 步骤4: 说明已知条件
        construction_4 = Text(
            "已知∠ABC+∠ABD=两直角，则BC与BD共线",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_4))
        self.wait(2)
        self.play(FadeOut(construction_4))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_BC, line_BD,
            point_B,
            label_A, label_B, label_C, label_D
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 文字显示在下半部分
        proof_title = Text("证明 (反证法):", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1: 假设BD和BC不共线
        proof_1 = Text(
            "假设BD和BC不在同一直线上",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2: 引入辅助点E和辅助线BE
        # 定义E点（需要考虑图形已经上移）
        E_base = np.array([2.0, 2.0, 0])  # E在右上方（基础位置）
        E = E_base + np.array([0, 3.2, 0])  # 加上上移的偏移
        B_shifted = B + np.array([0, 3.2, 0])  # B的新位置

        line_BE = Line(B_shifted, E, color=RED, stroke_width=3)
        line_BE.set_opacity(0.6)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, UP, buff=0.2)

        proof_2_intro = Text(
            "设BE与CB在同一直线上",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2_intro))
        self.wait(1.0)

        self.play(Create(line_BE), Write(label_E))
        self.wait(1.0)
        self.play(FadeOut(proof_2_intro))
        self.wait(0.5)

        # 证明步骤3: 设BE与CB共线（高亮）
        self.play(
            line_BE.animate.set_stroke(color=RED, width=5),
            line_BE.animate.set_opacity(1),
            line_BC.animate.set_stroke(color=GREEN, width=5)
        )
        # 继续证明（不再重复"设BE与CB在同一直线上"）

        # 证明步骤3: 由命题1.13
        self.play(
            line_BE.animate.set_stroke(color=RED, width=3),
            line_BC.animate.set_stroke(color=GREEN, width=3),
            line_AB.animate.set_stroke(color=WHITE, width=5)
        )
        proof_3 = Text(
            "∵ 直线AB在直线CBE的上方",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        proof_4 = Text(
            "∴ ∠ABC+∠ABE=两直角",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        proof_5 = Text(
            "(命题1.13 直线相交形成的邻角和等于两直角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_4, DOWN, buff=0.2)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤4: 但已知∠ABC+∠ABD=两直角
        self.play(
            line_AB.animate.set_stroke(color=WHITE, width=3),
            line_BD.animate.set_stroke(color=BLUE, width=5)
        )
        proof_6 = Text(
            "但已知∠ABC+∠ABD=两直角",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤5: 公理1
        self.play(
            line_BD.animate.set_stroke(color=BLUE, width=3)
        )
        proof_7 = Text(
            "∴ ∠ABC+∠ABE=∠ABC+∠ABD",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        proof_8 = Text(
            "(公理1: 与同量相等的量彼此相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_7, DOWN, buff=0.2)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 证明步骤6: 同减∠ABC
        proof_9 = Text(
            "同减∠ABC，得∠ABE=∠ABD",
            font_size=32
        ).next_to(proof_8, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(1.5)

        proof_10 = Text(
            "(公理3: 等量减等量，其差相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_9, DOWN, buff=0.2)
        self.play(Write(proof_10))
        self.wait(1.5)

        # 证明步骤7: 矛盾
        self.play(
            line_BE.animate.set_stroke(color=RED, width=5),
            line_BD.animate.set_stroke(color=BLUE, width=5)
        )
        proof_11 = Text(
            "但∠ABE≠∠ABD (BE和BD不重合)",
            font_size=32,
            color=RED
        ).next_to(proof_10, DOWN, buff=0.35)
        self.play(Write(proof_11))
        self.wait(1.5)

        # 证明步骤8: 矛盾，假设不成立
        proof_12 = Text(
            "矛盾! 故假设不成立",
            font_size=32,
            color=RED
        ).next_to(proof_11, DOWN, buff=0.35)
        self.play(Write(proof_12))
        self.wait(2)

        # 隐去辅助线BE和所有证明步骤
        self.play(
            line_BE.animate.set_opacity(0.3),
            line_BD.animate.set_stroke(color=BLUE, width=3),
            FadeOut(proof_1),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9),
            FadeOut(proof_10),
            FadeOut(proof_11),
            FadeOut(proof_12)
        )
        self.wait(0.5)

        # 证明步骤9: 同理可证其他直线都不满足
        proof_13 = Text(
            "同理，除BD外的其他直线",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_13))
        self.wait(1.5)

        proof_14 = Text(
            "都不满足与CB在同一直线上",
            font_size=32
        ).next_to(proof_13, DOWN, buff=0.35)
        self.play(Write(proof_14))
        self.wait(1.5)

        # 证明步骤10: 结论
        self.play(
            line_BC.animate.set_stroke(color=GREEN, width=5),
            line_BD.animate.set_stroke(color=BLUE, width=5)
        )
        proof_15 = Text(
            "∴ CB与BD在同一直线上",
            font_size=32,
            color=GREEN
        ).next_to(proof_14, DOWN, buff=0.35)
        self.play(Write(proof_15))
        self.wait(2)

        # 淡出辅助线BE
        self.play(
            FadeOut(line_BE),
            FadeOut(label_E)
        )
        self.wait(0.5)

        # 5. 结论 - 分两行显示
        # 先隐去前面的证明过程
        self.play(
            line_BC.animate.set_stroke(color=GREEN, width=3),
            line_BD.animate.set_stroke(color=BLUE, width=3),
            FadeOut(proof_13),
            FadeOut(proof_14),
            FadeOut(proof_15)
        )
        self.wait(0.5)

        conclusion_line1 = Text(
            "邻角之和等于两直角的两直线必共线",
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
        # 更新geometry_group，移除已淡出的元素
        geometry_group_final = VGroup(
            line_AB, line_BC, line_BD,
            point_B,
            label_A, label_B, label_C, label_D
        )
        self.play(
            FadeOut(geometry_group_final),
            FadeOut(proof_title),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
