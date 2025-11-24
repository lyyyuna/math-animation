from manim import *
from utils.base_scene import ElementsScene

class Proposition8(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 8)

        # 1. 显示标题
        title = self.show_title(
            "卷一, 命题8",
            ["如果两个三角形的三条边分别相等",
             "那么等边所夹的角也相等"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）- 构造两个三角形ABC和DEF

        # 三角形ABC（左侧）- 放大1.5倍，位置更靠近中心
        A = np.array([-3, 1.5, 0])
        B = np.array([-5, -2, 0])
        C = np.array([-1, -2, 0])

        # 三角形DEF（右侧）- 与ABC完全全等（三边相等）
        D = np.array([3, 1.5, 0])   # D与A对称，使两个三角形全等
        E = np.array([1, -2, 0])
        F = np.array([5, -2, 0])

        # 构造三角形ABC
        line_AB = Line(A, B, color=WHITE)
        line_BC = Line(B, C, color=WHITE)
        line_CA = Line(C, A, color=WHITE)
        triangle_ABC = VGroup(line_AB, line_BC, line_CA)

        self.play(Create(triangle_ABC))
        self.wait(0.5)

        # 标注三角形ABC的点
        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP)
        label_B = Text("B", font_size=42, color=WHITE).next_to(B, LEFT)
        label_C = Text("C", font_size=42, color=WHITE).next_to(C, RIGHT)

        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(0.5)

        # 构造三角形DEF
        line_DE = Line(D, E, color=WHITE)
        line_EF = Line(E, F, color=WHITE)
        line_FD = Line(F, D, color=WHITE)
        triangle_DEF = VGroup(line_DE, line_EF, line_FD)

        self.play(Create(triangle_DEF))
        self.wait(0.5)

        # 标注三角形DEF的点
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, UP)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, LEFT)
        label_F = Text("F", font_size=42, color=WHITE).next_to(F, RIGHT)

        self.play(Write(label_D), Write(label_E), Write(label_F))
        self.wait(0.5)

        # 添加说明：三边相等
        condition_text = Text(
            "已知: AB=DE, AC=DF, BC=EF",
            font_size=38,
            color=YELLOW
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(condition_text))
        self.wait(1)

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            triangle_ABC, triangle_DEF,
            label_A, label_B, label_C,
            label_D, label_E, label_F
        )

        self.play(
            FadeOut(condition_text),
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 文字显示在下半部分
        proof_title_main = Text("证明:", font_size=38, color=YELLOW)
        proof_title_method = Text("(反证法)", font_size=32, color=RED)

        proof_title = VGroup(proof_title_main, proof_title_method).arrange(RIGHT, buff=0.3)
        proof_title.shift(DOWN * 2.0)

        self.play(Write(proof_title_main))
        self.wait(0.3)
        self.play(Write(proof_title_method))
        self.wait(0.5)

        # 证明步骤1: 将三角形ABC移至三角形DEF上（动画演示）
        proof_1 = Text(
            "将△ABC移至△DEF上，使BC与EF重合",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(0.5)

        # 创建移动的三角形ABC副本（从已经移动到上方的位置复制）
        triangle_ABC_copy = triangle_ABC.copy()
        label_A_copy = label_A.copy()
        label_B_copy = label_B.copy()
        label_C_copy = label_C.copy()
        moving_group = VGroup(triangle_ABC_copy, label_A_copy, label_B_copy, label_C_copy)

        # 高亮BC和EF
        self.play(
            line_BC.animate.set_stroke(color=BLUE, width=4),
            line_EF.animate.set_stroke(color=BLUE, width=4)
        )

        # 计算移动向量：让BC与EF完全重合
        # 现在triangle_ABC已经在UP * 3.2的位置，所以B的当前位置是B + UP * 3.2
        # E的当前位置是E + UP * 3.2
        # 移动向量让B移到E，C移到F
        shift_vector = E - B

        # 移动三角形：BC与EF完全重合（B到E，C到F）
        self.add(moving_group)
        self.play(
            moving_group.animate.shift(shift_vector),
            run_time=2
        )
        self.wait(1)

        # 恢复BC和EF的正常样式
        self.play(
            line_BC.animate.set_stroke(color=WHITE, width=2),
            line_EF.animate.set_stroke(color=WHITE, width=2)
        )

        # 移除移动后的标签A、B、C
        # 移动后B与E重合，C与F重合，A与D重合（因为三角形全等）
        # 所以都不显示新标签
        self.play(
            FadeOut(label_A_copy),
            FadeOut(label_B_copy),
            FadeOut(label_C_copy)
        )
        self.wait(0.5)

        # 证明步骤2: BC与EF相等，所以C与F重合
        proof_2 = Text(
            "∵ BC=EF，∴ C与F重合",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3: 假设BA、CA不与ED、DF重合
        proof_3 = Text(
            "假设BA、CA不与ED、DF重合，A点落在G点",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1)

        # 为了展示反证法，创建G点在D点旁边（假设A不与D重合）
        # G点位置：在D点旁边稍微偏移
        G_position = D + UP * 3.2 + np.array([0.6, 0.3, 0])

        # 创建并显示G标签
        label_G = Text("G", font_size=42, color=YELLOW).next_to(G_position, UP, buff=0.1)
        self.play(Write(label_G))
        self.wait(0.5)

        # 构造假想的线段EG、GF
        line_EG = Line(E + UP * 3.2, G_position, color=RED, stroke_width=3)
        line_GF = Line(G_position, F + UP * 3.2, color=RED, stroke_width=3)

        self.play(
            Create(line_EG),
            Create(line_GF)
        )
        self.wait(1)

        # 证明步骤4: 引用命题7，这是矛盾的
        proof_4 = Text(
            "则GE=DE, GF=DF",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1)

        proof_5 = Text(
            "这与命题1.7矛盾",
            font_size=32,
            color=RED
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1)

        proof_6 = Text(
            "(从同侧端点作出两组等长线段不可能相交于不同点)",
            font_size=28,
            color=GRAY
        ).next_to(proof_5, DOWN, buff=0.2)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 移除假想的线段EG、GF和标签G
        self.play(
            FadeOut(line_EG),
            FadeOut(line_GF),
            FadeOut(label_G)
        )
        self.wait(0.5)

        # 证明步骤5: 因此BA、CA与ED、DF重合
        proof_7 = Text(
            "∴ BA、CA分别与ED、DF重合",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))

        # 高亮所有边
        self.play(
            line_AB.animate.set_stroke(color=GREEN, width=4),
            line_CA.animate.set_stroke(color=GREEN, width=4),
            line_DE.animate.set_stroke(color=GREEN, width=4),
            line_FD.animate.set_stroke(color=GREEN, width=4)
        )
        self.wait(1.5)

        # 证明步骤6: 角BAC与角EDF重合
        proof_8 = Text(
            "∴ ∠BAC与∠EDF重合",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        proof_9 = Text(
            "即∠BAC=∠EDF (公理4: 重合的物体全等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_8, DOWN, buff=0.2)
        self.play(Write(proof_9))
        self.wait(2)

        # 5. 结论 - 分两行显示
        # 淡出所有证明步骤，为结论腾出空间
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

        conclusion_line1 = Text(
            "三角形三边分别相等，则等边所夹角相等",
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
            FadeOut(moving_group),
            FadeOut(proof_title),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
