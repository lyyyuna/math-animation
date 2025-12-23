"""
Book I, Proposition 21
由三角形一边的两端点向内作两条相交线段，
则交点到端点的线段和小于另两边之和，但所成角大于对应角
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition21(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 21)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 21",
            ["由三角形一边两端点向内作两条相交线段", "线段和小于另两边和，所成角大于对应角"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点 - 三角形ABC
        A = np.array([0, 2.2, 0])
        B = np.array([-2.0, -1.0, 0])
        C = np.array([2.2, -1.0, 0])

        # D点在三角形内部
        D = np.array([0.3, 0.3, 0])

        # 步骤1: 显示三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        line_BC = Line(B, C, color=WHITE, stroke_width=3)
        line_CA = Line(C, A, color=WHITE, stroke_width=3)

        label_A = Text("A", font_size=42, color=WHITE).next_to(A, UP, buff=0.2)
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

        # 步骤2: 在三角形内取点D，从B、C分别连到D
        construction_2 = Text(
            "在三角形内取点D，连接BD、DC",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_2))
        self.wait(0.5)

        dot_D = Dot(D, color=WHITE, radius=0.06)
        label_D = Text("D", font_size=42, color=WHITE).next_to(D, UP + LEFT, buff=0.15)

        line_BD = Line(B, D, color=BLUE, stroke_width=3)
        line_DC = Line(D, C, color=BLUE, stroke_width=3)

        self.play(Create(dot_D), Write(label_D))
        self.play(Create(line_BD), Create(line_DC))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 步骤3: 延长BD与AC交于E
        construction_3 = Text(
            "延长BD与AC交于E",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        self.play(Write(construction_3))
        self.wait(0.5)

        # 计算E点：BD延长线与AC的交点
        # BD方向向量
        BD_dir = (D - B) / np.linalg.norm(D - B)
        # AC的参数方程: P = A + t*(C - A)
        # BD的参数方程: P = B + s*BD_dir
        # 解交点
        AC_vec = C - A
        # B + s*BD_dir = A + t*AC_vec
        # s*BD_dir - t*AC_vec = A - B
        # 用矩阵求解
        mat = np.array([[BD_dir[0], -AC_vec[0]], [BD_dir[1], -AC_vec[1]]])
        rhs = np.array([A[0] - B[0], A[1] - B[1]])
        params = np.linalg.solve(mat, rhs)
        s = params[0]
        E = B + s * BD_dir
        E = np.array([E[0], E[1], 0])

        # 创建 line_AE 和 line_EC 替换 line_CA（用于后续分别高亮）
        line_AE = Line(A, E, color=WHITE, stroke_width=3)
        line_EC = Line(E, C, color=WHITE, stroke_width=3)
        self.add(line_AE, line_EC)
        self.remove(line_CA)

        line_DE = Line(D, E, color=GREEN, stroke_width=3)
        label_E = Text("E", font_size=42, color=WHITE).next_to(E, UP + RIGHT, buff=0.15)

        self.play(Create(line_DE))
        self.play(Write(label_E))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 显示已知和求证
        given_text = Text(
            "已知: △ABC，D在三角形内",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.05)
        prove_text = Text(
            "求证: BD+DC<AB+AC，∠BDC>∠BAC",
            font_size=34,
            color=YELLOW
        ).next_to(given_text, DOWN, buff=0.15)

        self.play(Write(given_text))
        self.play(Write(prove_text))
        self.wait(2)
        self.play(FadeOut(given_text), FadeOut(prove_text))

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            line_AB, line_BC, line_AE, line_EC,
            line_BD, line_DC, line_DE,
            label_A, label_B, label_C, label_D, label_E,
            dot_D
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 第一部分：证明BD+DC<AB+AC
        proof_title = Text("证明 (第一部分):", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤1: 在△ABE中，AB+AE>BE
        # 用半透明填充高亮 △ABE，同时边也加粗
        # 更新后的点位置（已经shift了UP * 3.2）
        A_shifted = A + UP * 3.2
        B_shifted = B + UP * 3.2
        E_shifted = E + UP * 3.2

        triangle_ABE = Polygon(
            A_shifted, B_shifted, E_shifted,
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        )
        self.play(
            FadeIn(triangle_ABE),
            line_AB.animate.set_stroke(color=BLUE, width=4),
            line_AE.animate.set_stroke(color=BLUE, width=4),
            line_BD.animate.set_stroke(color=BLUE, width=4),
            line_DE.animate.set_stroke(color=BLUE, width=4),
        )

        proof_1 = Text(
            "在△ABE中，AB+AE>BE",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        proof_1b = Text(
            "(命题1.20: 两边之和大于第三边)",
            font_size=28,
            color=GRAY
        ).next_to(proof_1, DOWN, buff=0.2)
        self.play(Write(proof_1b))
        self.wait(1.5)

        # 恢复颜色，淡出三角形填充
        self.play(
            FadeOut(triangle_ABE),
            line_AB.animate.set_stroke(color=WHITE, width=3),
            line_AE.animate.set_stroke(color=WHITE, width=3),
            line_BD.animate.set_stroke(color=BLUE, width=3),
            line_DE.animate.set_stroke(color=GREEN, width=3),
        )

        # 清理
        self.play(FadeOut(proof_1), FadeOut(proof_1b))
        self.wait(0.5)

        # 证明步骤2: 两边加EC，得AB+AC>BE+EC
        proof_2 = Text(
            "两边同加EC:",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_2))
        self.wait(1)

        proof_3 = Text(
            "AB+(AE+EC)>BE+EC",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        proof_4 = Text(
            "即 AB+AC>BE+EC",
            font_size=32,
            color=YELLOW
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 清理
        self.play(FadeOut(proof_2), FadeOut(proof_3), FadeOut(proof_4))
        self.wait(0.5)

        # 证明步骤3: 在△CED中，CE+ED>CD
        # 用半透明填充高亮 △CED，同时边也加粗
        C_shifted = C + UP * 3.2
        D_shifted = D + UP * 3.2

        triangle_CED = Polygon(
            C_shifted, E_shifted, D_shifted,
            fill_color=GREEN,
            fill_opacity=0.3,
            stroke_width=0
        )
        self.play(
            FadeIn(triangle_CED),
            line_EC.animate.set_stroke(color=GREEN, width=4),
            line_DE.animate.set_stroke(color=GREEN, width=4),
            line_DC.animate.set_stroke(color=GREEN, width=4),
        )

        proof_5 = Text(
            "在△CED中，CE+ED>CD",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_5))
        self.wait(1.5)

        proof_5b = Text(
            "(命题1.20)",
            font_size=28,
            color=GRAY
        ).next_to(proof_5, DOWN, buff=0.2)
        self.play(Write(proof_5b))
        self.wait(1.5)

        # 恢复颜色，淡出三角形填充
        self.play(
            FadeOut(triangle_CED),
            line_EC.animate.set_stroke(color=WHITE, width=3),
            line_DE.animate.set_stroke(color=GREEN, width=3),
            line_DC.animate.set_stroke(color=BLUE, width=3),
        )

        # 清理
        self.play(FadeOut(proof_5), FadeOut(proof_5b))
        self.wait(0.5)

        # 证明步骤4: 两边加DB，得CE+EB>CD+BD
        proof_6 = Text(
            "两边同加DB:",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_6))
        self.wait(1)

        proof_7 = Text(
            "CE+(ED+DB)>CD+DB",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        proof_8 = Text(
            "即 CE+EB>CD+BD",
            font_size=32,
            color=YELLOW
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 清理
        self.play(FadeOut(proof_6), FadeOut(proof_7), FadeOut(proof_8))
        self.wait(0.5)

        # 证明步骤5: 综合得AB+AC>BD+DC
        proof_9 = Text(
            "∵ AB+AC>BE+EC",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_9))
        self.wait(1)

        proof_10 = Text(
            "且 BE+EC>BD+DC",
            font_size=32
        ).next_to(proof_9, DOWN, buff=0.35)
        self.play(Write(proof_10))
        self.wait(1)

        proof_11 = Text(
            "∴ AB+AC>BD+DC",
            font_size=32,
            color=YELLOW
        ).next_to(proof_10, DOWN, buff=0.35)
        self.play(Write(proof_11))
        self.wait(1.5)

        # 清理第一部分
        self.play(
            FadeOut(proof_9),
            FadeOut(proof_10),
            FadeOut(proof_11),
            FadeOut(proof_title)
        )
        self.wait(0.5)

        # 5. 证明第二部分：证明∠BDC>∠BAC
        proof_title2 = Text("证明 (第二部分):", font_size=38, color=YELLOW)
        proof_title2.shift(DOWN * 2.0)
        self.play(Write(proof_title2))
        self.wait(0.5)

        # 证明步骤6: 在△CDE中，外角∠BDC>∠CED
        # 高亮 △CDE
        self.play(
            FadeIn(triangle_CED),
            line_EC.animate.set_stroke(color=GREEN, width=4),
            line_DE.animate.set_stroke(color=GREEN, width=4),
            line_DC.animate.set_stroke(color=GREEN, width=4),
        )

        # 标注外角 ∠BDC（用红色表示外角）
        angle_BDC = Angle(
            Line(D_shifted, B_shifted), Line(D_shifted, C_shifted),
            radius=0.35, color=RED, stroke_width=3
        )
        self.play(Create(angle_BDC))

        proof_12 = Text(
            "在△CDE中，∠BDC是外角",
            font_size=32
        ).next_to(proof_title2, DOWN, buff=0.4)
        self.play(Write(proof_12))
        self.wait(1.5)

        # 标注内角 ∠CED（用黄色表示内角）
        angle_CED = Angle(
            Line(E_shifted, D_shifted), Line(E_shifted, C_shifted),
            radius=0.3, color=YELLOW, stroke_width=3
        )
        self.play(Create(angle_CED))

        proof_13 = Text(
            "∴ ∠BDC>∠CED",
            font_size=32
        ).next_to(proof_12, DOWN, buff=0.35)
        self.play(Write(proof_13))
        self.wait(1.5)

        proof_13b = Text(
            "(命题1.16: 外角大于内对角)",
            font_size=28,
            color=GRAY
        ).next_to(proof_13, DOWN, buff=0.2)
        self.play(Write(proof_13b))
        self.wait(1.5)

        # 恢复颜色，淡出填充和角度标注
        self.play(
            FadeOut(triangle_CED),
            FadeOut(angle_BDC),
            FadeOut(angle_CED),
            line_EC.animate.set_stroke(color=WHITE, width=3),
            line_DE.animate.set_stroke(color=GREEN, width=3),
            line_DC.animate.set_stroke(color=BLUE, width=3),
        )

        # 清理
        self.play(FadeOut(proof_12), FadeOut(proof_13), FadeOut(proof_13b))
        self.wait(0.5)

        # 证明步骤7: 在△ABE中，外角∠CEB>∠BAC
        # 高亮 △ABE
        self.play(
            FadeIn(triangle_ABE),
            line_AB.animate.set_stroke(color=BLUE, width=4),
            line_AE.animate.set_stroke(color=BLUE, width=4),
            line_BD.animate.set_stroke(color=BLUE, width=4),
            line_DE.animate.set_stroke(color=BLUE, width=4),
        )

        # 标注外角 ∠CEB（用红色表示外角）
        angle_CEB = Angle(
            Line(E_shifted, B_shifted), Line(E_shifted, C_shifted),
            radius=0.3, color=RED, stroke_width=3
        )
        self.play(Create(angle_CEB))

        proof_14 = Text(
            "在△ABE中，∠CEB是外角",
            font_size=32
        ).next_to(proof_title2, DOWN, buff=0.4)
        self.play(Write(proof_14))
        self.wait(1.5)

        # 标注内角 ∠BAC（用黄色表示内角）
        angle_BAC = Angle(
            Line(A_shifted, B_shifted), Line(A_shifted, C_shifted),
            radius=0.3, color=YELLOW, stroke_width=3
        )
        self.play(Create(angle_BAC))

        proof_15 = Text(
            "∴ ∠CEB>∠BAC",
            font_size=32
        ).next_to(proof_14, DOWN, buff=0.35)
        self.play(Write(proof_15))
        self.wait(1.5)

        proof_15b = Text(
            "(命题1.16)",
            font_size=28,
            color=GRAY
        ).next_to(proof_15, DOWN, buff=0.2)
        self.play(Write(proof_15b))
        self.wait(1.5)

        # 恢复颜色，淡出填充和角度标注
        self.play(
            FadeOut(triangle_ABE),
            FadeOut(angle_CEB),
            FadeOut(angle_BAC),
            line_AB.animate.set_stroke(color=WHITE, width=3),
            line_AE.animate.set_stroke(color=WHITE, width=3),
            line_BD.animate.set_stroke(color=BLUE, width=3),
            line_DE.animate.set_stroke(color=GREEN, width=3),
        )

        # 清理
        self.play(FadeOut(proof_14), FadeOut(proof_15), FadeOut(proof_15b))
        self.wait(0.5)

        # 证明步骤8: 综合得∠BDC>∠BAC
        proof_16 = Text(
            "∵ ∠BDC>∠CED",
            font_size=32
        ).next_to(proof_title2, DOWN, buff=0.4)
        self.play(Write(proof_16))
        self.wait(1)

        proof_17 = Text(
            "且 ∠CED=∠CEB>∠BAC",
            font_size=32
        ).next_to(proof_16, DOWN, buff=0.35)
        self.play(Write(proof_17))
        self.wait(1)

        proof_18 = Text(
            "∴ ∠BDC>∠BAC",
            font_size=32,
            color=YELLOW
        ).next_to(proof_17, DOWN, buff=0.35)
        self.play(Write(proof_18))
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(proof_16),
            FadeOut(proof_17),
            FadeOut(proof_18),
            FadeOut(proof_title2)
        )
        self.wait(0.5)

        # 6. 结论 - 淡出辅助线
        self.play(
            FadeOut(line_DE),
            FadeOut(label_E)
        )
        # 更新geometry_group
        geometry_group = VGroup(
            line_AB, line_BC, line_AE, line_EC,
            line_BD, line_DC,
            label_A, label_B, label_C, label_D,
            dot_D
        )
        self.wait(0.5)

        conclusion_title = Text("结论:", font_size=38, color=YELLOW)
        conclusion_title.shift(DOWN * 2.0)
        self.play(Write(conclusion_title))

        conclusion_line1 = Text(
            "BD+DC<AB+AC",
            font_size=36,
            color=GREEN
        ).next_to(conclusion_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "∠BDC>∠BAC",
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

        # 7. 结束
        self.play(
            FadeOut(geometry_group),
            FadeOut(conclusion_title),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2),
            FadeOut(conclusion_line3)
        )
        self.wait(1)
