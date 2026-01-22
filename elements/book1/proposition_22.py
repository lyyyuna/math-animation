"""
Book I, Proposition 22
以分别与三条已知线段相等的线段为三边作三角形
要求：任意两条线段之和大于第三条线段
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition22(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 22)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 22",
            ["以三条已知线段为三边作三角形", "要求任意两边之和大于第三边"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 显示三条已知线段 A、B、C（在左侧）
        # 定义三条线段的位置（显示在左上角）
        seg_A_start = np.array([-5.5, 3.5, 0])
        seg_A_end = np.array([-3.5, 3.5, 0])  # 长度2
        seg_B_start = np.array([-5.5, 2.5, 0])
        seg_B_end = np.array([-3.0, 2.5, 0])  # 长度2.5
        seg_C_start = np.array([-5.5, 1.5, 0])
        seg_C_end = np.array([-4.0, 1.5, 0])  # 长度1.5

        # 线段长度
        len_A = 2.0
        len_B = 2.5
        len_C = 1.5

        line_seg_A = Line(seg_A_start, seg_A_end, color=RED, stroke_width=4)
        line_seg_B = Line(seg_B_start, seg_B_end, color=GREEN, stroke_width=4)
        line_seg_C = Line(seg_C_start, seg_C_end, color=BLUE, stroke_width=4)

        label_seg_A = Text("A", font_size=38, color=RED).next_to(line_seg_A, LEFT, buff=0.2)
        label_seg_B = Text("B", font_size=38, color=GREEN).next_to(line_seg_B, LEFT, buff=0.2)
        label_seg_C = Text("C", font_size=38, color=BLUE).next_to(line_seg_C, LEFT, buff=0.2)

        construction_1 = Text(
            "已知线段A、B、C",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_1))
        self.wait(0.5)

        self.play(
            Create(line_seg_A), Write(label_seg_A),
            Create(line_seg_B), Write(label_seg_B),
            Create(line_seg_C), Write(label_seg_C),
        )
        self.wait(1)

        # 显示条件说明
        condition_text = Text(
            "任意两边之和大于第三边",
            font_size=32,
            color=GRAY
        ).next_to(line_seg_C, DOWN, buff=0.3).align_to(line_seg_C, LEFT)
        self.play(Write(condition_text))
        self.wait(1.5)
        self.play(FadeOut(construction_1), FadeOut(condition_text))

        # 3. 作图：直线DE，截取DF=A, FG=B, GH=C
        construction_2 = Text(
            "作直线DE，截取DF=A，FG=B，GH=C",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        # 定义点D、F、G、H在一条水平线上
        D = np.array([-3.0, -0.5, 0])
        F = D + np.array([len_A, 0, 0])  # DF = A
        G = F + np.array([len_B, 0, 0])  # FG = B
        H = G + np.array([len_C, 0, 0])  # GH = C

        # 作直线DE（向右延伸）
        line_DE = Line(D, H + np.array([0.5, 0, 0]), color=WHITE, stroke_width=3)
        self.play(Create(line_DE))

        # 标注点D
        dot_D = Dot(D, color=WHITE, radius=0.06)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, DOWN, buff=0.2)
        self.play(Create(dot_D), Write(label_D))
        self.wait(0.5)

        # 截取DF = A（用红色标注）
        line_DF = Line(D, F, color=RED, stroke_width=4)
        dot_F = Dot(F, color=WHITE, radius=0.06)
        label_F = Text("F", font_size=42, color=WHITE).next_to(F, DOWN, buff=0.2)
        self.play(Create(line_DF))
        self.play(Create(dot_F), Write(label_F))
        self.wait(0.5)

        # 截取FG = B（用绿色标注）
        line_FG = Line(F, G, color=GREEN, stroke_width=4)
        dot_G = Dot(G, color=WHITE, radius=0.06)
        label_G = Text("G", font_size=42, color=WHITE).next_to(G, DOWN, buff=0.2)
        self.play(Create(line_FG))
        self.play(Create(dot_G), Write(label_G))
        self.wait(0.5)

        # 截取GH = C（用蓝色标注）
        line_GH = Line(G, H, color=BLUE, stroke_width=4)
        dot_H = Dot(H, color=WHITE, radius=0.06)
        label_H = Text("H", font_size=42, color=WHITE).next_to(H, DOWN, buff=0.2)
        self.play(Create(line_GH))
        self.play(Create(dot_H), Write(label_H))
        self.wait(1)

        self.play(FadeOut(construction_2))

        # 4. 以F为圆心，FD为半径作圆DKL
        construction_3 = Text(
            "以F为圆心，FD为半径作圆",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        circle_F = Circle(radius=len_A, color=RED, stroke_width=2)
        circle_F.move_to(F)
        self.play(Create(circle_F))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 5. 以G为圆心，GH为半径作圆KLH
        construction_4 = Text(
            "以G为圆心，GH为半径作圆",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_4))
        self.wait(0.5)

        circle_G = Circle(radius=len_C, color=BLUE, stroke_width=2)
        circle_G.move_to(G)
        self.play(Create(circle_G))
        self.wait(1)
        self.play(FadeOut(construction_4))

        # 6. 计算两圆交点K（取上方的交点）
        # 两圆交点计算
        # 圆F: (x-F[0])^2 + (y-F[1])^2 = len_A^2
        # 圆G: (x-G[0])^2 + (y-G[1])^2 = len_C^2
        # F和G之间的距离是len_B
        d = len_B  # F和G之间的距离
        a = len_A  # 圆F的半径
        c = len_C  # 圆G的半径

        # 使用两圆交点公式
        # x = (d^2 - c^2 + a^2) / (2d) （从F点算起）
        x = (d**2 - c**2 + a**2) / (2 * d)
        y = np.sqrt(a**2 - x**2)  # 取正值（上方交点）

        K = F + np.array([x, y, 0])

        # 连接KF和KG
        construction_5 = Text(
            "连接KF和KG",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_5))
        self.wait(0.5)

        dot_K = Dot(K, color=YELLOW, radius=0.08)
        label_K = Text("K", font_size=42, color=YELLOW).next_to(K, UP, buff=0.2)
        self.play(Create(dot_K), Write(label_K))

        line_KF = Line(K, F, color=RED, stroke_width=3)
        line_KG = Line(K, G, color=BLUE, stroke_width=3)
        self.play(Create(line_KF), Create(line_KG))
        self.wait(1)
        self.play(FadeOut(construction_5))

        # 高亮三角形KFG
        construction_6 = Text(
            "三角形KFG",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_6))

        # 高亮三角形
        triangle_KFG = Polygon(
            K, F, G,
            fill_color=YELLOW,
            fill_opacity=0.2,
            stroke_width=0
        )
        self.play(
            FadeIn(triangle_KFG),
            line_KF.animate.set_stroke(width=4),
            line_FG.animate.set_stroke(width=5),
            line_KG.animate.set_stroke(width=4),
        )
        self.wait(1.5)
        self.play(FadeOut(construction_6))

        # 7. 准备证明 - 移到上半部分
        geometry_group = VGroup(
            line_seg_A, line_seg_B, line_seg_C,
            label_seg_A, label_seg_B, label_seg_C,
            line_DE, line_DF, line_FG, line_GH,
            dot_D, dot_F, dot_G, dot_H, dot_K,
            label_D, label_F, label_G, label_H, label_K,
            circle_F, circle_G,
            line_KF, line_KG,
            triangle_KFG
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 更新点位置（用于后续高亮）
        K_shifted = K + UP * 3.2
        F_shifted = F + UP * 3.2
        G_shifted = G + UP * 3.2

        # 8. 证明过程
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明KF = A
        self.play(
            line_KF.animate.set_stroke(color=RED, width=5),
            line_DF.animate.set_stroke(color=RED, width=5),
        )

        proof_1 = Text(
            "∵ F是圆心，FD、FK都是半径",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        proof_2 = Text(
            "∴ FK=FD=A",
            font_size=32,
            color=RED
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 恢复并清理
        self.play(
            line_KF.animate.set_stroke(color=RED, width=3),
            line_DF.animate.set_stroke(color=RED, width=4),
        )
        self.play(FadeOut(proof_1), FadeOut(proof_2))
        self.wait(0.3)

        # 证明KG = C
        self.play(
            line_KG.animate.set_stroke(color=BLUE, width=5),
            line_GH.animate.set_stroke(color=BLUE, width=5),
        )

        proof_3 = Text(
            "∵ G是圆心，GH、GK都是半径",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_3))
        self.wait(1.5)

        proof_4 = Text(
            "∴ GK=GH=C",
            font_size=32,
            color=BLUE
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 恢复并清理
        self.play(
            line_KG.animate.set_stroke(color=BLUE, width=3),
            line_GH.animate.set_stroke(color=BLUE, width=4),
        )
        self.play(FadeOut(proof_3), FadeOut(proof_4))
        self.wait(0.3)

        # 证明FG = B
        self.play(
            line_FG.animate.set_stroke(color=GREEN, width=6),
        )

        proof_5 = Text(
            "又 FG=B（作图）",
            font_size=32,
            color=GREEN
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 恢复
        self.play(
            line_FG.animate.set_stroke(color=GREEN, width=5),
        )
        self.play(FadeOut(proof_5))
        self.wait(0.3)

        # 综合结论
        proof_6 = Text(
            "∴ KF、FG、GK分别等于A、B、C",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 清理证明步骤
        self.play(FadeOut(proof_6), FadeOut(proof_title))
        self.wait(0.5)

        # 9. 淡出辅助圆，突出最终三角形
        self.play(
            FadeOut(circle_F),
            FadeOut(circle_G),
            FadeOut(line_DE),
            FadeOut(line_DF),
            FadeOut(line_GH),
            FadeOut(dot_D),
            FadeOut(dot_H),
            FadeOut(label_D),
            FadeOut(label_H),
        )
        self.wait(0.5)

        # 10. 显示结论
        conclusion_title = Text("结论:", font_size=38, color=YELLOW)
        conclusion_title.shift(DOWN * 2.0)
        self.play(Write(conclusion_title))

        conclusion_line1 = Text(
            "△KFG的三边KF、FG、GK",
            font_size=36,
            color=GREEN
        ).next_to(conclusion_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "分别等于已知线段A、B、C",
            font_size=36,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.25)

        conclusion_line3 = Text(
            "(Q.E.F.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line2, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.play(Write(conclusion_line3))
        self.wait(2)

        # 11. 结束
        final_group = VGroup(
            line_seg_A, line_seg_B, line_seg_C,
            label_seg_A, label_seg_B, label_seg_C,
            line_FG, line_KF, line_KG,
            dot_F, dot_G, dot_K,
            label_F, label_G, label_K,
            triangle_KFG,
            conclusion_title,
            conclusion_line1, conclusion_line2, conclusion_line3
        )
        self.play(FadeOut(final_group))
        self.wait(1)
