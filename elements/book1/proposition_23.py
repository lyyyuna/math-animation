"""
Book I, Proposition 23
在已知直线和它上面的一点，作一个直线角等于已知直线角
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition23(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 23)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 23",
            ["在已知直线和它上面的一点", "作一个直线角等于已知直线角"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）

        # 2a. 显示已知角DCE（右上方）
        construction_1 = Text(
            "已知角DCE",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_1))
        self.wait(0.5)

        # 定义角DCE的顶点和两边（水平居中，用锐角演示）
        C = np.array([0.0, 0.5, 0])
        D = C + np.array([-0.8, 2.0, 0])   # CD方向：左上
        E = C + np.array([1.5, 1.8, 0])    # CE方向：右上

        dot_C = Dot(C, color=WHITE, radius=0.06)
        dot_D = Dot(D, color=WHITE, radius=0.06)
        dot_E = Dot(E, color=WHITE, radius=0.06)

        line_CD = Line(C, D, color=ORANGE, stroke_width=3)
        line_CE = Line(C, E, color=ORANGE, stroke_width=3)

        label_C = Text("C", font_size=42).next_to(C, DOWN, buff=0.2)
        label_D = Text("D", font_size=42).next_to(D, UP + LEFT, buff=0.15)
        label_E = Text("E", font_size=42).next_to(E, RIGHT, buff=0.15)

        # 角度弧：显式从 CE 方向逆时针扫到 CD 方向（绘制顶角内的锐角）
        cd_angle = np.arctan2(D[1] - C[1], D[0] - C[0])
        ce_angle = np.arctan2(E[1] - C[1], E[0] - C[0])
        angle_DCE = Arc(
            radius=0.6,
            start_angle=ce_angle,
            angle=cd_angle - ce_angle,
            arc_center=C,
            color=ORANGE,
            stroke_width=3,
        )

        self.play(
            Create(line_CD), Create(line_CE),
            Create(dot_C), Create(dot_D), Create(dot_E),
            Write(label_C), Write(label_D), Write(label_E),
        )
        self.play(Create(angle_DCE))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # 2b. 显示已知直线AB和点A（左下方）
        construction_2 = Text(
            "已知直线AB和点A",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_2))
        self.wait(0.5)

        # AB 水平居中
        A = np.array([-2.5, -1.5, 0])
        B = A + np.array([5.0, 0, 0])

        line_AB = Line(A, B, color=WHITE, stroke_width=3)
        dot_A = Dot(A, color=WHITE, radius=0.06)
        dot_B = Dot(B, color=WHITE, radius=0.06)

        label_A = Text("A", font_size=42).next_to(A, DOWN, buff=0.2)
        label_B = Text("B", font_size=42).next_to(B, DOWN, buff=0.2)

        self.play(
            Create(line_AB),
            Create(dot_A), Create(dot_B),
            Write(label_A), Write(label_B),
        )
        self.wait(1)
        self.play(FadeOut(construction_2))

        # 2c. 在CD和CE上取点D、E，连接DE
        construction_3 = Text(
            "连接DE",
            font_size=38,
            color=YELLOW
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_3))
        self.wait(0.5)

        line_DE = Line(D, E, color=ORANGE, stroke_width=3)
        self.play(Create(line_DE))
        self.wait(1)
        self.play(FadeOut(construction_3))

        # 2d. 用命题1.22作三角形AFG，使AF=CD, AG=CE, FG=DE
        construction_4 = Text(
            "由命题1.22：以三线段为边作三角形",
            font_size=34,
            color=YELLOW
        ).to_edge(UP, buff=0.0)
        construction_4b = Text(
            "作△AFG，使AF=CD，AG=CE，FG=DE",
            font_size=30,
            color=YELLOW
        ).next_to(construction_4, DOWN, buff=0.15)
        self.play(Write(construction_4), Write(construction_4b))
        self.wait(0.5)

        # 计算三边长度
        len_CD = np.linalg.norm(D - C)
        len_CE = np.linalg.norm(E - C)
        len_DE = np.linalg.norm(E - D)

        # 用两圆交点法求F的位置
        # 以A为端点，在AB方向上，AF=CD，AG=CE
        # F在A的上方，构成三角形AFG
        # AF=CD, AG=CE, FG=DE
        # 先确定G在AB上的方向（取AB方向上的某点作为参考）
        # 实际上F和G不必在AB上，只需从A出发

        # 用解析方法：A是原点，设F在某方向上距离A为len_CD
        # G在另一方向上距离A为len_CE，FG=len_DE
        # 通过两圆交点求解

        # 以A为中心建立坐标：
        # 设G在AB方向上（即右方），距离A为len_CE
        AB_dir = (B - A) / np.linalg.norm(B - A)
        G = A + AB_dir * len_CE

        # F的位置：AF=len_CD, GF=len_DE
        # 两圆交点：圆1以A为心半径len_CD，圆2以G为心半径len_DE
        d_AG = len_CE  # A到G的距离
        # x是从A到G方向上的投影
        x_F = (d_AG**2 - len_DE**2 + len_CD**2) / (2 * d_AG)
        y_F = np.sqrt(max(len_CD**2 - x_F**2, 0))  # 取上方交点

        # F的实际坐标
        AB_perp = np.array([-AB_dir[1], AB_dir[0], 0])  # AB的垂直方向（向上）
        F = A + AB_dir * x_F + AB_perp * y_F

        dot_F = Dot(F, color=YELLOW, radius=0.08)
        dot_G = Dot(G, color=YELLOW, radius=0.08)

        label_F = Text("F", font_size=42, color=YELLOW).next_to(F, UP + LEFT, buff=0.15)
        label_G = Text("G", font_size=42, color=YELLOW).next_to(G, DOWN, buff=0.2)

        line_AF = Line(A, F, color=YELLOW, stroke_width=3)
        line_AG = Line(A, G, color=YELLOW, stroke_width=3)
        line_FG = Line(F, G, color=YELLOW, stroke_width=3)

        # 角度弧FAG：显式从 AG 方向逆时针扫到 AF 方向
        af_angle = np.arctan2(F[1] - A[1], F[0] - A[0])
        ag_angle = np.arctan2(G[1] - A[1], G[0] - A[0])
        angle_FAG = Arc(
            radius=0.6,
            start_angle=ag_angle,
            angle=af_angle - ag_angle,
            arc_center=A,
            color=YELLOW,
            stroke_width=3,
        )

        self.play(
            Create(dot_F), Write(label_F),
            Create(dot_G), Write(label_G),
        )
        self.play(
            Create(line_AF), Create(line_AG), Create(line_FG),
        )
        self.play(Create(angle_FAG))
        self.wait(1)

        # 高亮三角形AFG
        triangle_AFG = Polygon(
            A, F, G,
            fill_color=YELLOW,
            fill_opacity=0.15,
            stroke_width=0
        )
        self.play(FadeIn(triangle_AFG))
        self.wait(1)
        self.play(FadeOut(construction_4), FadeOut(construction_4b))

        # 3. 准备证明 - 移到上半部分
        geometry_group = VGroup(
            line_CD, line_CE, line_DE,
            dot_C, dot_D, dot_E,
            label_C, label_D, label_E,
            angle_DCE,
            line_AB, dot_A, dot_B, label_A, label_B,
            line_AF, line_AG, line_FG,
            dot_F, dot_G, label_F, label_G,
            angle_FAG, triangle_AFG,
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 更新点位置
        A_s = A + UP * 3.2
        F_s = F + UP * 3.2
        G_s = G + UP * 3.2
        C_s = C + UP * 3.2
        D_s = D + UP * 3.2
        E_s = E + UP * 3.2

        # 4. 证明过程
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 步骤1：DC=FA, CE=AG
        self.play(
            line_CD.animate.set_stroke(color=RED, width=5),
            line_AF.animate.set_stroke(color=RED, width=5),
        )

        proof_1 = Text(
            "∵ DC=FA，CE=AG (作图)",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        self.play(
            line_CD.animate.set_stroke(color=ORANGE, width=3),
            line_AF.animate.set_stroke(color=YELLOW, width=3),
            line_CE.animate.set_stroke(color=BLUE, width=5),
            line_AG.animate.set_stroke(color=BLUE, width=5),
        )
        self.wait(1)
        self.play(
            line_CE.animate.set_stroke(color=ORANGE, width=3),
            line_AG.animate.set_stroke(color=YELLOW, width=3),
        )

        # 步骤2：DE=FG
        self.play(
            line_DE.animate.set_stroke(color=GREEN, width=5),
            line_FG.animate.set_stroke(color=GREEN, width=5),
        )

        proof_2 = Text(
            "且DE=FG (作图)",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        self.play(
            line_DE.animate.set_stroke(color=ORANGE, width=3),
            line_FG.animate.set_stroke(color=YELLOW, width=3),
        )

        # 步骤3：由命题1.8得角相等
        # 高亮两个三角形
        triangle_DCE = Polygon(
            D_s, C_s, E_s,
            fill_color=ORANGE,
            fill_opacity=0.2,
            stroke_width=0
        )
        triangle_AFG_proof = Polygon(
            A_s, F_s, G_s,
            fill_color=YELLOW,
            fill_opacity=0.2,
            stroke_width=0
        )
        self.play(
            FadeIn(triangle_DCE),
            FadeIn(triangle_AFG_proof),
        )

        proof_3 = Text(
            "∴ △DCE≌△FAG",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        proof_4 = Text(
            "(命题1.8: 三边对应相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_3, DOWN, buff=0.25)
        self.play(Write(proof_4))
        self.wait(1.5)

        self.play(FadeOut(triangle_DCE), FadeOut(triangle_AFG_proof))

        # 步骤4：角相等
        self.play(
            angle_DCE.animate.set_stroke(color=RED, width=4),
            angle_FAG.animate.set_stroke(color=RED, width=4),
        )

        proof_5 = Text(
            "∴ ∠DCE=∠FAG",
            font_size=32,
            color=RED
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        self.play(
            angle_DCE.animate.set_stroke(color=ORANGE, width=2),
            angle_FAG.animate.set_stroke(color=YELLOW, width=2),
        )

        # 清理证明步骤
        self.play(
            FadeOut(proof_1), FadeOut(proof_2),
            FadeOut(proof_3), FadeOut(proof_4), FadeOut(proof_5),
            FadeOut(proof_title),
        )
        self.wait(0.5)

        # 5. 淡出辅助元素（保留 △DCE 和 ∠FAG 作为对照）
        self.play(
            FadeOut(line_DE),
            FadeOut(triangle_AFG),
        )
        # 高亮最终作出的 ∠FAG
        self.play(angle_FAG.animate.set_stroke(color=GREEN, width=5))
        self.wait(0.5)

        # 6. 显示结论
        conclusion_title = Text("结论:", font_size=38, color=YELLOW)
        conclusion_title.shift(DOWN * 2.0)
        self.play(Write(conclusion_title))

        conclusion_line1 = Text(
            "在直线AB上的点A作出∠FAG",
            font_size=36,
            color=GREEN
        ).next_to(conclusion_title, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "等于已知角DCE",
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

        # 7. 结束
        final_group = VGroup(
            line_CD, line_CE,
            dot_C, dot_D, dot_E,
            label_C, label_D, label_E,
            angle_DCE,
            line_AB, dot_A, dot_B, label_A, label_B,
            line_AF, line_AG, line_FG,
            dot_F, dot_G, label_F, label_G,
            angle_FAG,
            conclusion_title,
            conclusion_line1, conclusion_line2, conclusion_line3,
        )
        self.play(FadeOut(final_group))
        self.wait(1)
