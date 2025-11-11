from manim import *
from utils.base_scene import ElementsScene

class Proposition5(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 5)

        # 1. 显示标题
        title = self.show_title(
            "卷一, 命题5",
            ["在等腰三角形中，两底角彼此相等",
            "若向下延长两腰，则在底边下面的两个角也彼此相等"],
            wait_time=3
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）- 绘制等腰三角形
        A = np.array([0, 3.5, 0])
        B = np.array([-2, 0.5, 0])
        C = np.array([2, 0.5, 0])

        # 绘制等腰三角形ABC
        line_AB = Line(A, B, color=WHITE, stroke_width=2)
        line_AC = Line(A, C, color=WHITE, stroke_width=2)
        line_BC = Line(B, C, color=BLUE, stroke_width=2)

        self.play(Create(line_AB))
        self.wait(0.3)
        self.play(Create(line_AC))
        self.wait(0.3)
        self.play(Create(line_BC))
        self.wait(0.5)

        # 标注三角形ABC的点
        label_A = Text("A", font_size=42, color=YELLOW).next_to(A, UP, buff=0.2)
        label_B = Text("B", font_size=42, color=YELLOW).next_to(B, LEFT, buff=0.2)
        label_C = Text("C", font_size=42, color=YELLOW).next_to(C, RIGHT, buff=0.2)

        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(0.5)

        # 标记相等的边（等腰）
        mark_AB = Text("a", font_size=32, color=GREEN).move_to((A + B) / 2).shift(LEFT * 0.3)
        mark_AC = Text("a", font_size=32, color=GREEN).move_to((A + C) / 2).shift(RIGHT * 0.3)

        self.play(Write(mark_AB), Write(mark_AC))
        self.wait(1)

        # 延长AB到D，AC到E
        D = B + 1.5 * (B - A) / np.linalg.norm(B - A) * 2
        E = C + 1.5 * (C - A) / np.linalg.norm(C - A) * 2

        line_BD = Line(B, D, color=WHITE, stroke_width=2)
        line_CE = Line(C, E, color=WHITE, stroke_width=2)

        explanation_1 = Text("延长AB、AC成直线BD、CE（公设2）", font_size=38, color=YELLOW)
        explanation_1.to_edge(DOWN)
        self.play(Write(explanation_1))

        self.play(Create(line_BD), Create(line_CE))
        self.wait(0.5)

        label_D = Text("D", font_size=42, color=YELLOW).next_to(D, DOWN + LEFT, buff=0.2)
        label_E = Text("E", font_size=42, color=YELLOW).next_to(E, DOWN + RIGHT, buff=0.2)
        self.play(Write(label_D), Write(label_E))
        self.wait(1)
        self.play(FadeOut(explanation_1))

        # 在BD上取点F，在CE上取点G，使AF = AG
        F = B + 0.6 * (D - B)
        G = C + 0.6 * (E - C)

        point_F = Dot(F, color=RED)
        point_G = Dot(G, color=RED)
        label_F = Text("F", font_size=42, color=YELLOW).next_to(F, LEFT, buff=0.2)
        label_G = Text("G", font_size=42, color=YELLOW).next_to(G, RIGHT, buff=0.2)

        explanation_2 = Text("在BD上取点F，在CE上取点G，使AF=AG（命题1.3）", font_size=38, color=YELLOW)
        explanation_2.to_edge(DOWN)
        self.play(Write(explanation_2))

        self.play(Create(point_F), Create(point_G))
        self.play(Write(label_F), Write(label_G))
        self.wait(1)
        self.play(FadeOut(explanation_2))

        # 连接FC和GB
        line_FC = Line(F, C, color=ORANGE, stroke_width=2)
        line_GB = Line(G, B, color=ORANGE, stroke_width=2)

        explanation_3 = Text("连接FC和GB（公设1）", font_size=38, color=YELLOW)
        explanation_3.to_edge(DOWN)
        self.play(Write(explanation_3))

        self.play(Create(line_FC), Create(line_GB))
        self.wait(1)
        self.play(FadeOut(explanation_3))

        # 3. 准备证明 - 移到上半部分
        geometry_group = VGroup(
            line_AB, line_AC, line_BC,
            line_BD, line_CE,
            line_FC, line_GB,
            label_A, label_B, label_C, label_D, label_E, label_F, label_G,
            mark_AB, mark_AC,
            point_F, point_G
        )

        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 文字显示在下半部分
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.3)

        # 证明步骤1 - △AFC ≌ △AGB
        proof_1 = Text(
            "∵ AF=AG，AB=AC，∠FAG公共",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2 - 强调第一对全等三角形
        proof_2 = Text(
            "∴ △AFC≌△AGB（命题1.4，SAS）",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(0.5)

        # 强调△AFC和△AGB（需要使用移动后的坐标）
        A_shifted = A + UP * 3.2
        B_shifted = B + UP * 3.2
        C_shifted = C + UP * 3.2
        F_shifted = F + UP * 3.2
        G_shifted = G + UP * 3.2

        triangle_AFC_highlight = Polygon(A_shifted, F_shifted, C_shifted, color=GREEN, fill_opacity=0.3, stroke_width=0)
        triangle_AGB_highlight = Polygon(A_shifted, G_shifted, B_shifted, color=GREEN, fill_opacity=0.3, stroke_width=0)

        self.play(
            FadeIn(triangle_AFC_highlight),
            FadeIn(triangle_AGB_highlight)
        )
        self.wait(1)
        self.play(
            FadeOut(triangle_AFC_highlight),
            FadeOut(triangle_AGB_highlight)
        )
        self.wait(0.5)

        # 证明步骤3
        self.play(
            line_FC.animate.set_stroke(color=YELLOW, width=4),
            line_GB.animate.set_stroke(color=YELLOW, width=4)
        )
        proof_3 = Text(
            "∴ FC=GB，∠ACF=∠ABG，∠AFC=∠AGB",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4 - 淡出前面的步骤1-2，并将步骤3上移
        self.play(
            line_FC.animate.set_stroke(color=ORANGE, width=2),
            line_GB.animate.set_stroke(color=ORANGE, width=2),
            FadeOut(proof_1),
            FadeOut(proof_2),
            proof_3.animate.next_to(proof_title, DOWN, buff=0.4)
        )

        proof_4 = Text(
            "∵ AF=AG，AB=AC，∴ BF=CG（公理3）",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5 - △BFC ≌ △CGB
        proof_5 = Text(
            "∵ BF=CG，FC=GB，∠BFC=∠CGB",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤6 - 强调第二对全等三角形
        proof_6 = Text(
            "∴ △BFC≌△CGB（命题1.4，SAS）",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(0.5)

        # 强调△BFC和△CGB（需要使用移动后的坐标）
        triangle_BFC_highlight = Polygon(B_shifted, F_shifted, C_shifted, color=BLUE, fill_opacity=0.3, stroke_width=0)
        triangle_CGB_highlight = Polygon(C_shifted, G_shifted, B_shifted, color=BLUE, fill_opacity=0.3, stroke_width=0)

        self.play(
            FadeIn(triangle_BFC_highlight),
            FadeIn(triangle_CGB_highlight)
        )
        self.wait(1)
        self.play(
            FadeOut(triangle_BFC_highlight),
            FadeOut(triangle_CGB_highlight)
        )
        self.wait(0.5)

        # 证明步骤7 - 强调底边下方的两个角相等
        proof_7_part1 = Text("∴ ∠FBC=∠GCB", font_size=32, color=PURPLE)
        proof_7_part2 = Text("，∠BCF=∠CBG", font_size=32)
        proof_7 = VGroup(proof_7_part1, proof_7_part2).arrange(RIGHT, buff=0)
        proof_7.next_to(proof_6, DOWN, buff=0.35)

        self.play(Write(proof_7))
        self.wait(0.5)

        # 高亮显示∠FBC和∠GCB（底边下方的内角）
        # ∠FBC: 从BC逆时针到BF的角（顶点在B）
        vec_BC = C_shifted - B_shifted
        vec_BF = F_shifted - B_shifted
        angle_BC = np.arctan2(vec_BC[1], vec_BC[0])
        angle_BF = np.arctan2(vec_BF[1], vec_BF[0])

        # ∠GCB: 从CG顺时针到CB的角（顶点在C）
        vec_CG = G_shifted - C_shifted
        vec_CB = B_shifted - C_shifted
        angle_CG = np.arctan2(vec_CG[1], vec_CG[0])
        angle_CB = np.arctan2(vec_CB[1], vec_CB[0])

        # 计算角度差，确保正确方向
        angle_diff_FBC = angle_BF - angle_BC
        if angle_diff_FBC > np.pi:
            angle_diff_FBC -= 2 * np.pi
        elif angle_diff_FBC < -np.pi:
            angle_diff_FBC += 2 * np.pi

        angle_diff_GCB = angle_CB - angle_CG
        if angle_diff_GCB > np.pi:
            angle_diff_GCB -= 2 * np.pi
        elif angle_diff_GCB < -np.pi:
            angle_diff_GCB += 2 * np.pi

        angle_FBC = Arc(radius=0.4, start_angle=angle_BC, angle=angle_diff_FBC,
                       color=PURPLE, stroke_width=4).shift(B_shifted)
        angle_GCB = Arc(radius=0.4, start_angle=angle_CG, angle=angle_diff_GCB,
                       color=PURPLE, stroke_width=4).shift(C_shifted)

        # 强调角度
        self.play(
            Create(angle_FBC),
            Create(angle_GCB)
        )
        self.wait(1)
        self.play(
            FadeOut(angle_FBC),
            FadeOut(angle_GCB)
        )

        # 恢复文字颜色
        self.play(proof_7_part1.animate.set_color(WHITE))
        self.wait(0.5)

        # 证明步骤8 - 淡出步骤3-5，并将步骤6-7上移
        self.play(
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            proof_6.animate.next_to(proof_title, DOWN, buff=0.4),
            proof_7.animate.next_to(proof_title, DOWN, buff=0.4 + 0.35 + 0.8)  # 需要考虑proof_6的高度
        )

        proof_8 = Text(
            "∵ ∠ABG=∠ACF，∠CBG=∠BCF",
            font_size=32
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(1.5)

        # 证明步骤9 - 可视化公理3的相减过程
        # 显示角度相减的示意
        subtract_explanation = Text(
            "∠ABG - ∠CBG = ∠ACF - ∠BCF",
            font_size=30,
            color=BLUE_C
        ).next_to(proof_8, DOWN, buff=0.3)
        self.play(Write(subtract_explanation))
        self.wait(1)

        proof_9 = Text(
            "∴ ∠ABC=∠ACB（公理3：等量减等量）",
            font_size=32
        ).next_to(subtract_explanation, DOWN, buff=0.35)
        self.play(Write(proof_9))
        self.wait(0.5)

        # 高亮显示结果的两个角（使用移动后的坐标）
        angle_ABC = Arc(radius=0.4, start_angle=np.arctan2((A_shifted-B_shifted)[1], (A_shifted-B_shifted)[0]),
                       angle=np.arctan2((C_shifted-B_shifted)[1], (C_shifted-B_shifted)[0])-np.arctan2((A_shifted-B_shifted)[1], (A_shifted-B_shifted)[0]),
                       color=RED, stroke_width=4).shift(B_shifted)
        angle_ACB = Arc(radius=0.4, start_angle=np.arctan2((A_shifted-C_shifted)[1], (A_shifted-C_shifted)[0]),
                       angle=np.arctan2((B_shifted-C_shifted)[1], (B_shifted-C_shifted)[0])-np.arctan2((A_shifted-C_shifted)[1], (A_shifted-C_shifted)[0]),
                       color=RED, stroke_width=4).shift(C_shifted)

        self.play(Create(angle_ABC), Create(angle_ACB))
        self.wait(1.5)
        self.play(FadeOut(angle_ABC), FadeOut(angle_ACB), FadeOut(subtract_explanation))
        self.wait(0.5)

        # 5. 结论 - 分两行显示
        conclusion_line1 = Text(
            "∴ 等腰三角形两底角相等，延长线与底边所成角相等",
            font_size=36,
            color=GREEN
        ).next_to(proof_9, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "(Q.E.D.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.wait(2)

        # 6. 结束（注意：proof_1-5已经在证明过程中淡出）
        self.play(
            FadeOut(geometry_group),
            FadeOut(proof_title),
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(proof_9),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
