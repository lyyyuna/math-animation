"""
Book I, Proposition 27
如果一条直线与两条直线相交，内错角相等，则两直线平行
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition27(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 27)

        title = self.show_title(
            "卷 I, 命题 27",
            ["一条直线与两条直线相交", "若内错角相等，则两直线平行"],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        construction_1 = Text(
            "已知EF与AB、CD相交，且内错角相等",
            font_size=30, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(construction_1))

        E = np.array([-1.4, 1.0, 0.0])
        F = np.array([1.0, -1.0, 0.0])
        slope = 0.45
        A = E + np.array([-2.2, -2.2 * slope, 0.0])
        B = E + np.array([2.2, 2.2 * slope, 0.0])
        C = F + np.array([-2.2, -2.2 * slope, 0.0])
        D = F + np.array([2.2, 2.2 * slope, 0.0])
        bd_mid = (B + D) / 2
        bd_dir = (D - B) / np.linalg.norm(D - B)
        bd_perp = np.array([-bd_dir[1], bd_dir[0], 0.0])
        G = bd_mid + bd_perp * 1.35

        line_AB = Line(A, B, color=WHITE, stroke_width=4)
        line_CD = Line(C, D, color=WHITE, stroke_width=4)
        line_EF = Line(E, F, color=YELLOW, stroke_width=4)
        dots = VGroup(*[Dot(p, color=WHITE, radius=0.06) for p in [A, B, C, D, E, F]])
        labels = VGroup(
            Text("A", font_size=38).next_to(A, LEFT, buff=0.10),
            Text("B", font_size=38).next_to(B, RIGHT, buff=0.10),
            Text("C", font_size=38).next_to(C, LEFT, buff=0.10),
            Text("D", font_size=38).next_to(D, RIGHT, buff=0.10),
            Text("E", font_size=38).next_to(E, UP + LEFT, buff=0.08),
            Text("F", font_size=38).next_to(F, DOWN + RIGHT, buff=0.08),
        )

        ef_angle = np.arctan2(F[1] - E[1], F[0] - E[0])
        fe_angle = np.arctan2(E[1] - F[1], E[0] - F[0])
        ea_angle = np.arctan2(A[1] - E[1], A[0] - E[0])
        fd_angle = np.arctan2(D[1] - F[1], D[0] - F[0])
        angle_AEF = Arc(
            radius=0.38,
            start_angle=ea_angle,
            angle=ef_angle - ea_angle,
            arc_center=E,
            color=BLUE,
            stroke_width=4,
        )
        angle_EFD = Arc(
            radius=0.38,
            start_angle=fd_angle,
            angle=fe_angle - fd_angle,
            arc_center=F,
            color=BLUE,
            stroke_width=4,
        )

        self.play(Create(line_AB), Create(line_CD), Create(line_EF), Create(dots), Write(labels))
        self.play(Create(angle_AEF), Create(angle_EFD))
        self.wait(0.8)
        known = Text("已知: ∠AEF=∠EFD", font_size=30, color=GRAY).next_to(construction_1, DOWN, buff=0.12)
        self.play(Write(known))
        self.wait(1.2)
        self.play(FadeOut(construction_1), FadeOut(known))

        construction_2 = Text(
            "反设AB与CD不平行，在B、D方向相交于G",
            font_size=28, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        definition_note = Text(
            "定义1.23: 同平面内两直线不相交则平行",
            font_size=22, color=GRAY,
        ).next_to(construction_2, DOWN, buff=0.12)
        self.play(Write(construction_2), Write(definition_note))

        line_EG = Line(B, G, color=RED, stroke_width=4)
        line_FG = Line(D, G, color=RED, stroke_width=4)
        dot_G = Dot(G, color=RED, radius=0.07)
        label_G = Text("G", font_size=38, color=RED).next_to(G, UP + RIGHT, buff=0.08)
        self.play(Create(line_EG), Create(line_FG), Create(dot_G), Write(label_G))
        self.wait(1)
        self.play(FadeOut(construction_2), FadeOut(definition_note))

        geometry_group = VGroup(
            line_AB, line_CD, line_EF, dots, labels,
            angle_AEF, angle_EFD, line_EG, line_FG, dot_G, label_G,
        )
        shift_amt = 2.7
        self.play(geometry_group.animate.shift(UP * shift_amt))
        self.wait(0.5)

        E_s = E + UP * shift_amt
        F_s = F + UP * shift_amt
        G_s = G + UP * shift_amt

        proof_title = Text("证明:", font_size=36, color=YELLOW).shift(DOWN * 1.0)
        self.play(Write(proof_title))

        tri_GEF_fill = Polygon(G_s, E_s, F_s, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
        self.play(FadeIn(tri_GEF_fill))
        p1 = Text("若AB与CD在B、D方向交于G", font_size=27).next_to(proof_title, DOWN, buff=0.28)
        p2 = Text("则在△GEF中，∠AEF是外角", font_size=26).next_to(p1, DOWN, buff=0.25)
        p3 = Text("但已知∠AEF=∠EFD", font_size=27).next_to(p2, DOWN, buff=0.25)
        p4 = Text("外角等于内对角，矛盾", font_size=30, color=RED).next_to(p3, DOWN, buff=0.25)
        p4_note = Text("（命题1.16: 外角大于任一内对角）", font_size=22, color=GRAY).next_to(p4, DOWN, buff=0.12)
        self.play(Write(p1)); self.wait(0.8)
        self.play(Write(p2)); self.wait(0.8)
        self.play(Write(p3), angle_AEF.animate.set_stroke(color=RED, width=5), angle_EFD.animate.set_stroke(color=RED, width=5)); self.wait(0.8)
        self.play(Write(p4), Write(p4_note)); self.wait(1.6)

        self.play(FadeOut(tri_GEF_fill), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(p4_note))

        q1 = Text("∴ AB、CD不在B、D方向相交", font_size=27).next_to(proof_title, DOWN, buff=0.3)
        q2 = Text("同理，也不在A、C方向相交", font_size=27).next_to(q1, DOWN, buff=0.25)
        q3 = Text("∴ AB∥CD", font_size=36, color=GREEN).next_to(q2, DOWN, buff=0.3)
        q3_note = Text("（定义1.23: 不相交的同平面直线为平行线）", font_size=22, color=GRAY).next_to(q3, DOWN, buff=0.12)
        self.play(Write(q1)); self.wait(0.8)
        self.play(Write(q2)); self.wait(0.8)
        self.play(Write(q3), Write(q3_note), line_AB.animate.set_stroke(color=GREEN, width=5), line_CD.animate.set_stroke(color=GREEN, width=5)); self.wait(2)

        self.play(FadeOut(proof_title), FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(q3_note))
        conclusion_title = Text("结论:", font_size=38, color=YELLOW).shift(DOWN * 1.0)
        conclusion_1 = Text("一条直线与两条直线相交", font_size=32, color=GREEN).next_to(conclusion_title, DOWN, buff=0.35)
        conclusion_2 = Text("内错角相等，则两直线平行", font_size=32, color=GREEN).next_to(conclusion_1, DOWN, buff=0.2)
        qed = Text("(Q.E.D.)", font_size=28, color=GREEN).next_to(conclusion_2, DOWN, buff=0.25)
        self.play(Write(conclusion_title))
        self.play(Write(conclusion_1))
        self.play(Write(conclusion_2))
        self.play(Write(qed))
        self.wait(2)

        final_group = VGroup(geometry_group, conclusion_title, conclusion_1, conclusion_2, qed)
        self.play(FadeOut(final_group))
        self.wait(1)
