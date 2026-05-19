"""
Book I, Proposition 25
如果两个三角形有两条对应边相等，则第三边越长，其所对应的角越大
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition25(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 25)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 25",
            [
                "两三角形中两边对应相等",
                "第三边较大者所对的角也较大",
            ],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        side_len = 2.6
        bac_deg = 105   # ∠BAC 较大，因此 BC 较长
        edf_deg = 62    # ∠EDF 较小，因此 EF 较短

        # ---- 2a. 作 △ABC ----
        construction_1 = Text(
            "作△ABC（第三边BC较长）",
            font_size=34, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_1))
        self.wait(0.3)

        A = np.array([0.0, 2.0, 0.0])
        ab_rad = np.deg2rad(270 - bac_deg / 2)
        ac_rad = np.deg2rad(270 + bac_deg / 2)
        B = A + side_len * np.array([np.cos(ab_rad), np.sin(ab_rad), 0])
        C = A + side_len * np.array([np.cos(ac_rad), np.sin(ac_rad), 0])

        dot_A = Dot(A, color=WHITE, radius=0.06)
        dot_B = Dot(B, color=WHITE, radius=0.06)
        dot_C = Dot(C, color=WHITE, radius=0.06)
        line_AB = Line(A, B, color=WHITE, stroke_width=4)
        line_AC = Line(A, C, color=WHITE, stroke_width=4)
        line_BC = Line(B, C, color=GREEN, stroke_width=4)
        label_A = Text("A", font_size=38).next_to(A, UP, buff=0.10)
        label_B = Text("B", font_size=38).next_to(B, DOWN + LEFT, buff=0.08)
        label_C = Text("C", font_size=38).next_to(C, DOWN + RIGHT, buff=0.08)
        bac_arc = Arc(
            radius=0.38,
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

        # ---- 2b. 作 △DEF，使两边对应相等但 EF 较短 ----
        construction_2 = Text(
            "作△DEF，使AB=DE，AC=DF，且BC>EF",
            font_size=28, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_2))
        self.wait(0.3)

        D = np.array([0.0, -0.55, 0.0])
        de_rad = np.deg2rad(270 - edf_deg / 2)
        df_rad = np.deg2rad(270 + edf_deg / 2)
        E = D + side_len * np.array([np.cos(de_rad), np.sin(de_rad), 0])
        F = D + side_len * np.array([np.cos(df_rad), np.sin(df_rad), 0])

        dot_D = Dot(D, color=WHITE, radius=0.06)
        dot_E = Dot(E, color=WHITE, radius=0.06)
        dot_F = Dot(F, color=WHITE, radius=0.06)
        line_DE = Line(D, E, color=WHITE, stroke_width=4)
        line_DF = Line(D, F, color=WHITE, stroke_width=4)
        line_EF = Line(E, F, color=RED, stroke_width=4)
        label_D = Text("D", font_size=38).next_to(D, UP, buff=0.10)
        label_E = Text("E", font_size=38).next_to(E, DOWN + LEFT, buff=0.08)
        label_F = Text("F", font_size=38).next_to(F, DOWN + RIGHT, buff=0.08)
        edf_arc = Arc(
            radius=0.34,
            start_angle=de_rad,
            angle=df_rad - de_rad,
            arc_center=D,
            color=ORANGE,
            stroke_width=4,
        )

        self.play(
            Create(line_DE), Create(line_DF), Create(line_EF),
            Create(dot_D), Create(dot_E), Create(dot_F),
            Write(label_D), Write(label_E), Write(label_F),
        )
        self.play(Create(edf_arc))
        self.wait(1)

        known_text = Text(
            "已知: AB=DE，AC=DF，BC>EF",
            font_size=30, color=GRAY,
        ).to_edge(UP, buff=0.0)
        self.play(FadeOut(construction_2), Write(known_text))
        self.wait(1.2)
        self.play(FadeOut(known_text))

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
        )
        shift_amt = 2.6
        self.play(geometry_group.animate.shift(UP * shift_amt))
        self.wait(0.5)

        A_s = A + UP * shift_amt
        B_s = B + UP * shift_amt
        C_s = C + UP * shift_amt
        D_s = D + UP * shift_amt
        E_s = E + UP * shift_amt
        F_s = F + UP * shift_amt

        # 4. 证明过程
        proof_title = Text("证明:", font_size=36, color=YELLOW)
        proof_title.shift(DOWN * 1.0)
        self.play(Write(proof_title))
        self.wait(0.3)

        proof_given = Text(
            "已知: AB=DE，AC=DF，BC>EF",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        proof_goal = Text(
            "求证: ∠BAC>∠EDF",
            font_size=30, color=GREEN,
        ).next_to(proof_given, DOWN, buff=0.25)
        self.play(Write(proof_given), Write(proof_goal))
        self.wait(1.5)
        self.play(FadeOut(proof_given), FadeOut(proof_goal))

        # ---- 4a. 排除两角相等 ----
        triangle_ABC_fill = Polygon(
            A_s, B_s, C_s,
            fill_color=BLUE, fill_opacity=0.18, stroke_width=0,
        )
        triangle_DEF_fill = Polygon(
            D_s, E_s, F_s,
            fill_color=BLUE, fill_opacity=0.18, stroke_width=0,
        )
        self.play(FadeIn(triangle_ABC_fill), FadeIn(triangle_DEF_fill))

        proof_1a = Text(
            "假设∠BAC=∠EDF",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        self.play(Write(proof_1a))
        self.wait(0.8)

        proof_1b = Text(
            "∵ AB=DE，AC=DF，夹角相等",
            font_size=26,
        ).next_to(proof_1a, DOWN, buff=0.25)
        self.play(Write(proof_1b))
        self.wait(0.8)

        proof_1c = Text(
            "∴ △ABC≌△DEF",
            font_size=28,
        ).next_to(proof_1b, DOWN, buff=0.25)
        proof_1c_note = Text(
            "（命题1.4: 两边及其夹角对应相等，则三角形全等）",
            font_size=22, color=GRAY,
        ).next_to(proof_1c, DOWN, buff=0.15)
        self.play(Write(proof_1c), Write(proof_1c_note))
        self.wait(1.0)

        proof_1d = Text(
            "∴ BC=EF，与BC>EF矛盾",
            font_size=30, color=RED,
        ).next_to(proof_1c_note, DOWN, buff=0.25)
        self.play(
            Write(proof_1d),
            line_BC.animate.set_stroke(color=GREEN, width=5),
            line_EF.animate.set_stroke(color=RED, width=5),
        )
        self.wait(1.8)

        self.play(
            FadeOut(triangle_ABC_fill), FadeOut(triangle_DEF_fill),
            FadeOut(proof_1a), FadeOut(proof_1b),
            FadeOut(proof_1c), FadeOut(proof_1c_note), FadeOut(proof_1d),
            line_BC.animate.set_stroke(color=GREEN, width=4),
            line_EF.animate.set_stroke(color=RED, width=4),
        )

        # ---- 4b. 排除 ∠BAC 较小 ----
        self.play(
            bac_arc.animate.set_stroke(color=BLUE, width=5),
            edf_arc.animate.set_stroke(color=ORANGE, width=5),
        )

        proof_2a = Text(
            "假设∠BAC<∠EDF",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        self.play(Write(proof_2a))
        self.wait(0.8)

        proof_2b = Text(
            "则较小角所对的边也较小",
            font_size=26,
        ).next_to(proof_2a, DOWN, buff=0.25)
        proof_2b_note = Text(
            "（命题1.24: 夹角大者所对的边较大）",
            font_size=22, color=GRAY,
        ).next_to(proof_2b, DOWN, buff=0.15)
        self.play(Write(proof_2b), Write(proof_2b_note))
        self.wait(1.0)

        proof_2c = Text(
            "∴ BC<EF，与BC>EF矛盾",
            font_size=30, color=RED,
        ).next_to(proof_2b_note, DOWN, buff=0.25)
        self.play(
            Write(proof_2c),
            line_BC.animate.set_stroke(color=GREEN, width=5),
            line_EF.animate.set_stroke(color=RED, width=5),
        )
        self.wait(1.8)

        self.play(
            FadeOut(proof_2a), FadeOut(proof_2b),
            FadeOut(proof_2b_note), FadeOut(proof_2c),
            bac_arc.animate.set_stroke(color=BLUE, width=4),
            edf_arc.animate.set_stroke(color=ORANGE, width=4),
            line_BC.animate.set_stroke(color=GREEN, width=4),
            line_EF.animate.set_stroke(color=RED, width=4),
        )

        # ---- 4c. 结论 ----
        proof_3a = Text(
            "∴ ∠BAC既不等于也不小于∠EDF",
            font_size=28,
        ).next_to(proof_title, DOWN, buff=0.3)
        proof_3b = Text(
            "∴ ∠BAC>∠EDF",
            font_size=34, color=GREEN,
        ).next_to(proof_3a, DOWN, buff=0.3)
        self.play(Write(proof_3a))
        self.wait(1.0)
        self.play(
            Write(proof_3b),
            bac_arc.animate.set_stroke(color=GREEN, width=6),
            edf_arc.animate.set_stroke(color=RED, width=5),
        )
        self.wait(2)

        self.play(FadeOut(proof_title), FadeOut(proof_3a), FadeOut(proof_3b))
        self.wait(0.3)

        # 5. 显示结论
        conclusion_title = Text("结论:", font_size=38, color=YELLOW)
        conclusion_title.shift(DOWN * 1.0)
        self.play(Write(conclusion_title))

        conclusion_line1 = Text(
            "两三角形中两边对应相等",
            font_size=32, color=GREEN,
        ).next_to(conclusion_title, DOWN, buff=0.35)
        conclusion_line2 = Text(
            "第三边较大者所对的角也较大",
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
