"""
Book I, Proposition 24
两三角形中两边对应相等，夹角大者所对的边也较大
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition24(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 24)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 24",
            [
                "两三角形中两边对应相等",
                "夹角大者所对的边也较大",
            ],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        side_len = 2.8
        bac_deg = 110   # ∠BAC
        edf_deg = 60    # ∠EDF（明显小于 ∠BAC）

        # ---- 2a. △ABC（∠BAC 较大）----
        construction_1 = Text(
            "作△ABC（∠BAC较大）",
            font_size=34, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_1))
        self.wait(0.3)

        A = np.array([0.0, 2.05, 0.0])
        ab_rad = np.deg2rad(270 - bac_deg / 2)   # 215°
        ac_rad = np.deg2rad(270 + bac_deg / 2)   # 325°
        B = A + side_len * np.array([np.cos(ab_rad), np.sin(ab_rad), 0])
        C = A + side_len * np.array([np.cos(ac_rad), np.sin(ac_rad), 0])

        dot_A = Dot(A, color=WHITE, radius=0.06)
        dot_B = Dot(B, color=WHITE, radius=0.06)
        dot_C = Dot(C, color=WHITE, radius=0.06)
        line_AB = Line(A, B, color=WHITE, stroke_width=4)
        line_AC = Line(A, C, color=WHITE, stroke_width=4)
        line_BC = Line(B, C, color=WHITE, stroke_width=4)
        label_A = Text("A", font_size=38).next_to(A, UP, buff=0.10)
        label_B = Text("B", font_size=38).next_to(B, DOWN + LEFT, buff=0.08)
        label_C = Text("C", font_size=38).next_to(C, DOWN + RIGHT, buff=0.08)

        # ∠BAC 角弧（蓝色）
        bac_arc = Arc(
            radius=0.35,
            start_angle=ab_rad,
            angle=ac_rad - ab_rad,
            arc_center=A,
            color=BLUE,
            stroke_width=4,
        )

        self.play(
            Create(line_AB), Create(line_AC), Create(line_BC),
            Create(dot_A), Create(dot_B), Create(dot_C),
            Write(label_A), Write(label_B), Write(label_C),
        )
        self.play(Create(bac_arc))
        self.wait(1)
        self.play(FadeOut(construction_1))

        # ---- 2b. △DEF（AB=DE, AC=DF, ∠EDF 较小）----
        construction_2 = Text(
            "作△DEF，使AB=DE，AC=DF，∠EDF较小",
            font_size=28, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_2))
        self.wait(0.3)

        D = np.array([0.0, -0.45, 0.0])
        de_rad = np.deg2rad(270 - edf_deg / 2)   # 240°
        df_rad = np.deg2rad(270 + edf_deg / 2)   # 300°
        E = D + side_len * np.array([np.cos(de_rad), np.sin(de_rad), 0])
        F = D + side_len * np.array([np.cos(df_rad), np.sin(df_rad), 0])

        dot_D = Dot(D, color=WHITE, radius=0.06)
        dot_E = Dot(E, color=WHITE, radius=0.06)
        dot_F = Dot(F, color=WHITE, radius=0.06)
        line_DE = Line(D, E, color=WHITE, stroke_width=4)
        line_DF = Line(D, F, color=WHITE, stroke_width=4)
        line_EF = Line(E, F, color=WHITE, stroke_width=4)
        label_D = Text("D", font_size=38).next_to(D, UP, buff=0.10)
        label_E = Text("E", font_size=38).next_to(E, DOWN + LEFT, buff=0.08)
        label_F = Text("F", font_size=38).next_to(F, DOWN + RIGHT, buff=0.08)

        edf_arc = Arc(
            radius=0.32,
            start_angle=de_rad,
            angle=df_rad - de_rad,
            arc_center=D,
            color=GREEN,
            stroke_width=4,
        )

        self.play(
            Create(line_DE), Create(line_DF), Create(line_EF),
            Create(dot_D), Create(dot_E), Create(dot_F),
            Write(label_D), Write(label_E), Write(label_F),
        )
        self.play(Create(edf_arc))
        self.wait(1)
        self.play(FadeOut(construction_2))

        # ---- 2c. 作 ∠EDG=∠BAC（命题1.23）----
        construction_3 = Text(
            "作∠EDG=∠BAC（命题1.23）",
            font_size=32, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        construction_3_note = Text(
            "命题1.23: 在已知直线上作等于已知角的角",
            font_size=24, color=GRAY,
        ).next_to(construction_3, DOWN, buff=0.12)
        self.play(Write(construction_3), Write(construction_3_note))
        self.wait(0.3)

        # 从 DE 方向逆时针旋转 ∠BAC 得到 DG 方向
        dg_rad = de_rad + np.deg2rad(bac_deg)    # 350°
        G = D + side_len * np.array([np.cos(dg_rad), np.sin(dg_rad), 0])

        dot_G = Dot(G, color=YELLOW, radius=0.07)
        line_DG = Line(D, G, color=YELLOW, stroke_width=4)
        label_G = Text("G", font_size=38, color=YELLOW).next_to(G, RIGHT, buff=0.08)

        edg_arc = Arc(
            radius=0.52,
            start_angle=de_rad,
            angle=np.deg2rad(bac_deg),
            arc_center=D,
            color=BLUE,
            stroke_width=4,
        )

        self.play(
            Create(line_DG),
            Create(dot_G), Write(label_G),
        )
        self.play(Create(edg_arc))
        self.wait(1)
        self.play(FadeOut(construction_3), FadeOut(construction_3_note))

        # ---- 2d. 使 DG=DF（命题1.3）----
        construction_4 = Text(
            "使DG=DF（命题1.3）",
            font_size=32, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        construction_4_note = Text(
            "命题1.3: 在较长线段上截取等于较短线段的部分",
            font_size=24, color=GRAY,
        ).next_to(construction_4, DOWN, buff=0.12)
        self.play(Write(construction_4), Write(construction_4_note))
        self.wait(0.3)

        self.play(
            line_DG.animate.set_stroke(color=ORANGE, width=5),
            line_DF.animate.set_stroke(color=ORANGE, width=5),
        )
        self.wait(1)
        self.play(
            line_DG.animate.set_stroke(color=YELLOW, width=4),
            line_DF.animate.set_stroke(color=WHITE, width=4),
        )
        self.play(FadeOut(construction_4), FadeOut(construction_4_note))

        # ---- 2e. 连接 EG 和 FG ----
        construction_5 = Text(
            "连接EG，FG",
            font_size=34, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_5))
        self.wait(0.3)

        line_EG = Line(E, G, color=YELLOW, stroke_width=4)
        line_FG = Line(F, G, color=YELLOW, stroke_width=4)

        self.play(Create(line_EG), Create(line_FG))
        self.wait(1)
        self.play(FadeOut(construction_5))

        # 3. 准备证明 - 整体上移
        geometry_group = VGroup(
            line_AB, line_AC, line_BC,
            dot_A, dot_B, dot_C,
            label_A, label_B, label_C,
            bac_arc,
            line_DE, line_DF, line_EF,
            dot_D, dot_E, dot_F,
            label_D, label_E, label_F,
            edf_arc,
            line_DG, dot_G, label_G, edg_arc,
            line_EG, line_FG,
        )
        shift_amt = 2.7
        self.play(geometry_group.animate.shift(UP * shift_amt))
        self.wait(0.5)

        # 更新点位置（用于证明阶段的三角形填充）
        A_s = A + UP * shift_amt
        B_s = B + UP * shift_amt
        C_s = C + UP * shift_amt
        D_s = D + UP * shift_amt
        E_s = E + UP * shift_amt
        F_s = F + UP * shift_amt
        G_s = G + UP * shift_amt

        # 4. 证明
        proof_title = Text("证明:", font_size=36, color=YELLOW)
        proof_title.shift(DOWN * 1.0)
        self.play(Write(proof_title))
        self.wait(0.3)

        # ---- Group 1: SAS → BC=EG ----
        triangle_ABC_fill = Polygon(
            A_s, B_s, C_s,
            fill_color=BLUE, fill_opacity=0.2, stroke_width=0,
        )
        triangle_DEG_fill = Polygon(
            D_s, E_s, G_s,
            fill_color=BLUE, fill_opacity=0.2, stroke_width=0,
        )
        self.play(FadeIn(triangle_ABC_fill), FadeIn(triangle_DEG_fill))

        proof_1a = Text(
            "∵ AB=DE，AC=DG，∠BAC=∠EDG",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        self.play(Write(proof_1a))
        self.wait(1.2)

        proof_1b = Text(
            "∴ △ABC≌△DEG（命题1.4: SAS）",
            font_size=26,
        ).next_to(proof_1a, DOWN, buff=0.25)
        self.play(Write(proof_1b))
        self.wait(1.2)

        proof_1c = Text(
            "∴ BC=EG",
            font_size=30, color=BLUE,
        ).next_to(proof_1b, DOWN, buff=0.3)
        self.play(
            Write(proof_1c),
            line_BC.animate.set_stroke(color=BLUE, width=5),
            line_EG.animate.set_stroke(color=BLUE, width=5),
        )
        self.wait(1.8)

        self.play(
            line_BC.animate.set_stroke(color=WHITE, width=3),
            line_EG.animate.set_stroke(color=YELLOW, width=3),
            FadeOut(triangle_ABC_fill), FadeOut(triangle_DEG_fill),
            FadeOut(proof_1a), FadeOut(proof_1b), FadeOut(proof_1c),
        )

        # ---- Group 2: 等腰三角形 → ∠EFG>∠EGF ----
        triangle_DFG_fill = Polygon(
            D_s, F_s, G_s,
            fill_color=YELLOW, fill_opacity=0.22, stroke_width=0,
        )
        self.play(FadeIn(triangle_DFG_fill))

        proof_2a = Text(
            "∵ DG=DF，△DFG为等腰三角形",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        self.play(Write(proof_2a))
        self.wait(1.0)

        proof_2b = Text(
            "∴ ∠DFG=∠DGF",
            font_size=26,
        ).next_to(proof_2a, DOWN, buff=0.25)
        self.play(Write(proof_2b))

        proof_2b_note = Text(
            "（命题1.5: 等腰三角形底角相等）",
            font_size=22, color=GRAY,
        ).next_to(proof_2b, DOWN, buff=0.15)
        self.play(Write(proof_2b_note))
        self.wait(1.2)

        self.play(FadeOut(triangle_DFG_fill))

        proof_2c = Text(
            "又 ∠EFG>∠DFG，∠DGF>∠EGF",
            font_size=26,
        ).next_to(proof_2b_note, DOWN, buff=0.3)
        self.play(Write(proof_2c))

        proof_2d = Text(
            "（公理5：整体大于部分）",
            font_size=22, color=GRAY,
        ).next_to(proof_2c, DOWN, buff=0.15)
        self.play(Write(proof_2d))
        self.wait(1.3)

        proof_2e = Text(
            "∴ ∠EFG>∠EGF",
            font_size=30, color=BLUE,
        ).next_to(proof_2d, DOWN, buff=0.25)
        self.play(Write(proof_2e))
        self.wait(1.8)

        self.play(
            FadeOut(proof_2a), FadeOut(proof_2b),
            FadeOut(proof_2b_note), FadeOut(proof_2c),
            FadeOut(proof_2d), FadeOut(proof_2e),
        )

        # ---- Group 3: 命题1.19 → BC>EF ----
        triangle_EFG_fill = Polygon(
            E_s, F_s, G_s,
            fill_color=BLUE, fill_opacity=0.25, stroke_width=0,
        )
        self.play(FadeIn(triangle_EFG_fill))

        proof_3a = Text(
            "在△EFG中，∠EFG>∠EGF",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        self.play(Write(proof_3a))
        self.wait(1.0)

        proof_3b = Text(
            "∴ EG>EF（命题1.19：大角对大边）",
            font_size=24,
        ).next_to(proof_3a, DOWN, buff=0.25)
        self.play(Write(proof_3b))
        self.wait(1.3)

        proof_3c = Text(
            "又 BC=EG",
            font_size=28,
        ).next_to(proof_3b, DOWN, buff=0.3)
        self.play(Write(proof_3c))
        self.wait(0.8)

        proof_3d = Text(
            "∴ BC>EF",
            font_size=34, color=GREEN,
        ).next_to(proof_3c, DOWN, buff=0.3)
        self.play(
            Write(proof_3d),
            line_BC.animate.set_stroke(color=GREEN, width=5),
            line_EF.animate.set_stroke(color=RED, width=5),
        )
        self.wait(2)

        self.play(
            FadeOut(triangle_EFG_fill),
            FadeOut(proof_3a), FadeOut(proof_3b),
            FadeOut(proof_3c), FadeOut(proof_3d),
            FadeOut(proof_title),
            line_BC.animate.set_stroke(color=WHITE, width=3),
            line_EF.animate.set_stroke(color=WHITE, width=3),
        )
        self.wait(0.3)

        # 5. 结论
        conclusion_title = Text("结论:", font_size=38, color=YELLOW)
        conclusion_title.shift(DOWN * 1.0)
        self.play(Write(conclusion_title))

        conclusion_line1 = Text(
            "两三角形中两边对应相等",
            font_size=32, color=GREEN,
        ).next_to(conclusion_title, DOWN, buff=0.35)

        conclusion_line2 = Text(
            "夹角大者所对的边也较大",
            font_size=32, color=GREEN,
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        conclusion_line3 = Text(
            "(Q.E.D.)",
            font_size=28, color=GREEN,
        ).next_to(conclusion_line2, DOWN, buff=0.25)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.play(Write(conclusion_line3))
        self.wait(2)

        # 6. 结束
        final_group = VGroup(
            geometry_group,
            conclusion_title,
            conclusion_line1, conclusion_line2, conclusion_line3,
        )
        self.play(FadeOut(final_group))
        self.wait(1)
