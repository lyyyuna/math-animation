"""
Book I, Proposition 26
两角及一边对应相等，则其余边角对应相等
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition26(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 26)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 26",
            [
                "两三角形中两角对应相等",
                "且一边对应相等，则其余边角也相等",
            ],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 显示共同前提
        setup_title = Text("设:", font_size=42, color=YELLOW).shift(UP * 2.2)
        setup_1 = Text(
            "在△ABC和△DEF中",
            font_size=36,
        ).next_to(setup_title, DOWN, buff=0.35)
        setup_2 = Text(
            "∠ABC=∠DEF，∠BCA=∠EFD",
            font_size=34,
        ).next_to(setup_1, DOWN, buff=0.3)
        setup_3 = Text(
            "且有一条对应边相等",
            font_size=34,
        ).next_to(setup_2, DOWN, buff=0.3)
        setup_4 = Text(
            "分两种情况证明",
            font_size=32, color=GREEN,
        ).next_to(setup_3, DOWN, buff=0.45)
        setup_group = VGroup(setup_title, setup_1, setup_2, setup_3, setup_4)
        self.play(Write(setup_title))
        self.play(Write(setup_1), Write(setup_2), Write(setup_3))
        self.play(Write(setup_4))
        self.wait(2)
        self.play(FadeOut(setup_group))

        # 3. 第一种情况：等角之间的边相等（BC=EF）
        case_1_title = Text(
            "第一种情况: 等角之间的边相等（BC=EF）",
            font_size=30, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(case_1_title))

        B = np.array([-1.8, -0.4, 0.0])
        C = np.array([1.8, -0.4, 0.0])
        A = np.array([-0.5, 2.2, 0.0])

        E = np.array([-1.8, -2.55, 0.0])
        F = np.array([1.8, -2.55, 0.0])
        ba_dir = (A - B) / np.linalg.norm(A - B)
        D = E + ba_dir * 2.0

        G = B + ba_dir * 2.0

        line_AB = Line(A, B, color=WHITE, stroke_width=4)
        line_AC = Line(A, C, color=WHITE, stroke_width=4)
        line_BC = Line(B, C, color=GREEN, stroke_width=4)
        line_DE = Line(D, E, color=WHITE, stroke_width=4)
        line_DF = Line(D, F, color=WHITE, stroke_width=4)
        line_EF = Line(E, F, color=GREEN, stroke_width=4)
        line_BG = Line(B, G, color=YELLOW, stroke_width=5)
        line_GC = Line(G, C, color=YELLOW, stroke_width=4)

        dots_1 = VGroup(*[Dot(p, color=WHITE, radius=0.06) for p in [A, B, C, D, E, F]])
        dot_G = Dot(G, color=YELLOW, radius=0.07)
        labels_1 = VGroup(
            Text("A", font_size=38).next_to(A, UP, buff=0.10),
            Text("B", font_size=38).next_to(B, DOWN + LEFT, buff=0.08),
            Text("C", font_size=38).next_to(C, DOWN + RIGHT, buff=0.08),
            Text("D", font_size=38).next_to(D, LEFT, buff=0.12),
            Text("E", font_size=38).next_to(E, DOWN + LEFT, buff=0.08),
            Text("F", font_size=38).next_to(F, DOWN + RIGHT, buff=0.08),
        )
        label_G = Text("G", font_size=38, color=YELLOW).next_to(G, UP + LEFT, buff=0.12)

        ba_angle = np.arctan2(A[1] - B[1], A[0] - B[0])
        ca_angle = np.arctan2(A[1] - C[1], A[0] - C[0])
        fd_angle = np.arctan2(D[1] - F[1], D[0] - F[0])
        angle_B = Arc(
            radius=0.35,
            start_angle=0,
            angle=ba_angle,
            arc_center=B,
            color=BLUE,
            stroke_width=4,
        )
        angle_C = Arc(
            radius=0.35,
            start_angle=ca_angle,
            angle=PI - ca_angle,
            arc_center=C,
            color=ORANGE,
            stroke_width=4,
        )
        angle_E = Arc(
            radius=0.35,
            start_angle=0,
            angle=ba_angle,
            arc_center=E,
            color=BLUE,
            stroke_width=4,
        )
        angle_F = Arc(
            radius=0.35,
            start_angle=fd_angle,
            angle=PI - fd_angle,
            arc_center=F,
            color=ORANGE,
            stroke_width=4,
        )

        self.play(
            Create(line_AB), Create(line_AC), Create(line_BC),
            Create(line_DE), Create(line_DF), Create(line_EF),
            Create(dots_1), Write(labels_1),
        )
        self.play(Create(angle_B), Create(angle_C), Create(angle_E), Create(angle_F))
        self.wait(0.8)

        case_1_known = Text(
            "已知: ∠ABC=∠DEF，∠BCA=∠EFD，BC=EF",
            font_size=26, color=GRAY,
        ).next_to(case_1_title, DOWN, buff=0.12)
        self.play(Write(case_1_known))
        self.wait(1.2)
        self.play(FadeOut(case_1_title), FadeOut(case_1_known))

        construction_g = Text(
            "若AB>DE，则在AB上取BG=DE（命题1.3）",
            font_size=28, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        construction_g_note = Text(
            "命题1.3: 在较长线段上截取等于较短线段的部分",
            font_size=22, color=GRAY,
        ).next_to(construction_g, DOWN, buff=0.12)
        self.play(Write(construction_g), Write(construction_g_note))
        self.play(Create(line_BG), Create(dot_G), Write(label_G))
        self.wait(0.8)
        self.play(Create(line_GC))
        self.wait(0.8)
        self.play(FadeOut(construction_g), FadeOut(construction_g_note))

        geometry_1 = VGroup(
            line_AB, line_AC, line_BC,
            line_DE, line_DF, line_EF,
            line_BG, line_GC,
            dots_1, dot_G, labels_1, label_G,
            angle_B, angle_C, angle_E, angle_F,
        )
        shift_1 = 2.7
        self.play(geometry_1.animate.shift(UP * shift_1))
        self.wait(0.4)

        A_s = A + UP * shift_1
        B_s = B + UP * shift_1
        C_s = C + UP * shift_1
        D_s = D + UP * shift_1
        E_s = E + UP * shift_1
        F_s = F + UP * shift_1
        G_s = G + UP * shift_1

        proof_title = Text("证明（情况一）:", font_size=34, color=YELLOW)
        proof_title.shift(DOWN * 1.0)
        self.play(Write(proof_title))

        tri_GBC_fill = Polygon(G_s, B_s, C_s, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
        tri_DEF_fill = Polygon(D_s, E_s, F_s, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
        self.play(FadeIn(tri_GBC_fill), FadeIn(tri_DEF_fill))

        p1 = Text("∵ BG=DE，BC=EF，∠GBC=∠DEF", font_size=26).next_to(proof_title, DOWN, buff=0.25)
        p2 = Text("∴ △GBC≌△DEF", font_size=28).next_to(p1, DOWN, buff=0.22)
        p2_note = Text("（命题1.4: 两边及其夹角对应相等，则三角形全等）", font_size=20, color=GRAY).next_to(p2, DOWN, buff=0.12)
        p3 = Text("∴ ∠GCB=∠DFE", font_size=26).next_to(p2_note, DOWN, buff=0.22)
        p4 = Text("又∠DFE=∠BCA，故∠GCB=∠BCA", font_size=24).next_to(p3, DOWN, buff=0.22)
        p5 = Text("小角等于大角，矛盾", font_size=30, color=RED).next_to(p4, DOWN, buff=0.25)

        self.play(Write(p1)); self.wait(0.8)
        self.play(Write(p2), Write(p2_note)); self.wait(0.9)
        self.play(Write(p3)); self.wait(0.8)
        self.play(Write(p4)); self.wait(0.8)
        self.play(Write(p5), line_GC.animate.set_stroke(color=RED, width=5), line_AC.animate.set_stroke(color=RED, width=5))
        self.wait(1.6)

        self.play(
            FadeOut(tri_GBC_fill), FadeOut(tri_DEF_fill),
            FadeOut(p1), FadeOut(p2), FadeOut(p2_note), FadeOut(p3), FadeOut(p4), FadeOut(p5),
        )

        q1 = Text("∴ AB不可能大于DE，同理也不可能小于DE", font_size=25).next_to(proof_title, DOWN, buff=0.3)
        q2 = Text("∴ AB=DE", font_size=32, color=GREEN).next_to(q1, DOWN, buff=0.25)
        q3 = Text("由AB=DE，BC=EF，∠ABC=∠DEF", font_size=25).next_to(q2, DOWN, buff=0.25)
        q4 = Text("∴ AC=DF，∠BAC=∠EDF", font_size=30, color=GREEN).next_to(q3, DOWN, buff=0.25)
        q4_note = Text("（命题1.4）", font_size=22, color=GRAY).next_to(q4, DOWN, buff=0.12)
        self.play(Write(q1)); self.wait(0.8)
        self.play(Write(q2)); self.wait(0.8)
        self.play(Write(q3)); self.wait(0.8)
        self.play(Write(q4), Write(q4_note)); self.wait(1.5)

        self.play(FadeOut(geometry_1), FadeOut(proof_title), FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(q4), FadeOut(q4_note))
        self.wait(0.5)

        # 3. 第二种情况：一条等角所对的边相等（AB=DE）
        case_2_title = Text(
            "第二种情况: 等角所对的边相等（AB=DE）",
            font_size=30, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(case_2_title))

        B2 = np.array([-1.9, -0.35, 0.0])
        C2 = np.array([1.9, -0.35, 0.0])
        A2 = np.array([-0.45, 2.15, 0.0])
        E2 = np.array([-1.9, -3.15, 0.0])
        F2 = np.array([0.95, -3.15, 0.0])
        ba2_dir = (A2 - B2) / np.linalg.norm(A2 - B2)
        D2 = E2 + ba2_dir * np.linalg.norm(A2 - B2)
        H = B2 + (C2 - B2) / np.linalg.norm(C2 - B2) * np.linalg.norm(F2 - E2)

        line_A2B2 = Line(A2, B2, color=GREEN, stroke_width=4)
        line_A2C2 = Line(A2, C2, color=WHITE, stroke_width=4)
        line_B2C2 = Line(B2, C2, color=WHITE, stroke_width=4)
        line_D2E2 = Line(D2, E2, color=GREEN, stroke_width=4)
        line_D2F2 = Line(D2, F2, color=WHITE, stroke_width=4)
        line_E2F2 = Line(E2, F2, color=WHITE, stroke_width=4)
        line_BH = Line(B2, H, color=YELLOW, stroke_width=5)
        line_AH = Line(A2, H, color=YELLOW, stroke_width=4)

        dots_2 = VGroup(*[Dot(p, color=WHITE, radius=0.06) for p in [A2, B2, C2, D2, E2, F2]])
        dot_H = Dot(H, color=YELLOW, radius=0.07)
        labels_2 = VGroup(
            Text("A", font_size=38).next_to(A2, UP, buff=0.10),
            Text("B", font_size=38).next_to(B2, DOWN + LEFT, buff=0.08),
            Text("C", font_size=38).next_to(C2, DOWN + RIGHT, buff=0.08),
            Text("D", font_size=38).next_to(D2, LEFT, buff=0.12),
            Text("E", font_size=38).next_to(E2, DOWN + LEFT, buff=0.08),
            Text("F", font_size=38).next_to(F2, DOWN + RIGHT, buff=0.08),
        )
        label_H = Text("H", font_size=38, color=YELLOW).next_to(H, DOWN, buff=0.08)

        a2b_angle = np.arctan2(A2[1] - B2[1], A2[0] - B2[0])
        a2c_angle = np.arctan2(A2[1] - C2[1], A2[0] - C2[0])
        d2f_angle = np.arctan2(D2[1] - F2[1], D2[0] - F2[0])
        angle_B2 = Arc(
            radius=0.35,
            start_angle=0,
            angle=a2b_angle,
            arc_center=B2,
            color=BLUE,
            stroke_width=4,
        )
        angle_C2 = Arc(
            radius=0.35,
            start_angle=a2c_angle,
            angle=PI - a2c_angle,
            arc_center=C2,
            color=ORANGE,
            stroke_width=4,
        )
        angle_E2 = Arc(
            radius=0.35,
            start_angle=0,
            angle=a2b_angle,
            arc_center=E2,
            color=BLUE,
            stroke_width=4,
        )
        angle_F2 = Arc(
            radius=0.35,
            start_angle=d2f_angle,
            angle=PI - d2f_angle,
            arc_center=F2,
            color=ORANGE,
            stroke_width=4,
        )

        self.play(
            Create(line_A2B2), Create(line_A2C2), Create(line_B2C2),
            Create(line_D2E2), Create(line_D2F2), Create(line_E2F2),
            Create(dots_2), Write(labels_2),
        )
        self.play(Create(angle_B2), Create(angle_C2), Create(angle_E2), Create(angle_F2))
        case_2_known = Text(
            "已知: ∠ABC=∠DEF，∠BCA=∠EFD，AB=DE",
            font_size=26, color=GRAY,
        ).next_to(case_2_title, DOWN, buff=0.12)
        self.play(Write(case_2_known))
        self.wait(1.2)
        self.play(FadeOut(case_2_title), FadeOut(case_2_known))

        construction_h = Text(
            "若BC>EF，则在BC上取BH=EF（命题1.3）",
            font_size=28, color=YELLOW,
        ).to_edge(UP, buff=0.0)
        construction_h_note = Text(
            "命题1.3: 在较长线段上截取等于较短线段的部分",
            font_size=22, color=GRAY,
        ).next_to(construction_h, DOWN, buff=0.12)
        self.play(Write(construction_h), Write(construction_h_note))
        self.play(Create(line_BH), Create(dot_H), Write(label_H))
        self.wait(0.6)
        self.play(Create(line_AH))
        self.wait(0.8)
        self.play(FadeOut(construction_h), FadeOut(construction_h_note))

        geometry_2 = VGroup(
            line_A2B2, line_A2C2, line_B2C2,
            line_D2E2, line_D2F2, line_E2F2,
            line_BH, line_AH,
            dots_2, dot_H, labels_2, label_H,
            angle_B2, angle_C2, angle_E2, angle_F2,
        )
        shift_2 = 2.7
        self.play(geometry_2.animate.shift(UP * shift_2))
        self.wait(0.4)

        A2_s = A2 + UP * shift_2
        B2_s = B2 + UP * shift_2
        H_s = H + UP * shift_2
        D2_s = D2 + UP * shift_2
        E2_s = E2 + UP * shift_2
        F2_s = F2 + UP * shift_2

        proof_2_title = Text("证明（情况二）:", font_size=34, color=YELLOW)
        proof_2_title.shift(DOWN * 1.25)
        self.play(Write(proof_2_title))

        tri_ABH_fill = Polygon(A2_s, B2_s, H_s, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
        tri_DEF_2_fill = Polygon(D2_s, E2_s, F2_s, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
        self.play(FadeIn(tri_ABH_fill), FadeIn(tri_DEF_2_fill))

        r1 = Text("∵ AB=DE，BH=EF，∠ABH=∠DEF", font_size=26).next_to(proof_2_title, DOWN, buff=0.25)
        r2 = Text("∴ △ABH≌△DEF", font_size=28).next_to(r1, DOWN, buff=0.22)
        r2_note = Text("（命题1.4: 两边及其夹角对应相等，则三角形全等）", font_size=20, color=GRAY).next_to(r2, DOWN, buff=0.12)
        r3 = Text("∴ ∠BHA=∠EFD", font_size=26).next_to(r2_note, DOWN, buff=0.22)
        r4 = Text("又∠EFD=∠BCA，故∠BHA=∠BCA", font_size=24).next_to(r3, DOWN, buff=0.22)
        r5 = Text("外角等于内对角，矛盾", font_size=30, color=RED).next_to(r4, DOWN, buff=0.25)
        r5_note = Text("（命题1.16: 外角大于任一内对角）", font_size=22, color=GRAY).next_to(r5, DOWN, buff=0.12)

        self.play(Write(r1)); self.wait(0.8)
        self.play(Write(r2), Write(r2_note)); self.wait(0.9)
        self.play(Write(r3)); self.wait(0.8)
        self.play(Write(r4)); self.wait(0.8)
        self.play(Write(r5), Write(r5_note), line_AH.animate.set_stroke(color=RED, width=5), line_A2C2.animate.set_stroke(color=RED, width=5))
        self.wait(1.6)

        self.play(
            FadeOut(tri_ABH_fill), FadeOut(tri_DEF_2_fill),
            FadeOut(r1), FadeOut(r2), FadeOut(r2_note), FadeOut(r3), FadeOut(r4), FadeOut(r5), FadeOut(r5_note),
        )

        s1 = Text("∴ BC不可能大于EF，同理也不可能小于EF", font_size=25).next_to(proof_2_title, DOWN, buff=0.3)
        s2 = Text("∴ BC=EF", font_size=32, color=GREEN).next_to(s1, DOWN, buff=0.25)
        s3 = Text("由AB=DE，BC=EF，∠ABC=∠DEF", font_size=25).next_to(s2, DOWN, buff=0.25)
        s4 = Text("∴ AC=DF，∠BAC=∠EDF", font_size=30, color=GREEN).next_to(s3, DOWN, buff=0.25)
        s4_note = Text("（命题1.4）", font_size=22, color=GRAY).next_to(s4, DOWN, buff=0.12)
        self.play(Write(s1)); self.wait(0.8)
        self.play(Write(s2)); self.wait(0.8)
        self.play(Write(s3)); self.wait(0.8)
        self.play(Write(s4), Write(s4_note)); self.wait(1.5)
        self.play(FadeOut(proof_2_title), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), FadeOut(s4_note))

        # 4. 总结结论
        conclusion_title = Text("结论:", font_size=38, color=YELLOW).shift(DOWN * 1.0)
        conclusion_1 = Text("两三角形中两角对应相等", font_size=32, color=GREEN).next_to(conclusion_title, DOWN, buff=0.35)
        conclusion_2 = Text("且一边对应相等", font_size=32, color=GREEN).next_to(conclusion_1, DOWN, buff=0.2)
        conclusion_3 = Text("则其余边角也对应相等", font_size=32, color=GREEN).next_to(conclusion_2, DOWN, buff=0.2)
        qed = Text("(Q.E.D.)", font_size=28, color=GREEN).next_to(conclusion_3, DOWN, buff=0.25)
        self.play(Write(conclusion_title))
        self.play(Write(conclusion_1))
        self.play(Write(conclusion_2))
        self.play(Write(conclusion_3))
        self.play(Write(qed))
        self.wait(2)

        final_group = VGroup(geometry_2, conclusion_title, conclusion_1, conclusion_2, conclusion_3, qed)
        self.play(FadeOut(final_group))
        self.wait(1)
