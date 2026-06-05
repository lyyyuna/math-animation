"""
Book I, Proposition 28
如果一条直线与两条直线相交，同位角相等，或同旁内角之和等于两直角和，
则这两条直线平行
"""
from manim import *
from utils.base_scene import ElementsScene


class Proposition28(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 28)

        title = self.show_title(
            "卷 I, 命题 28",
            [
                "一条直线与两条直线相交",
                "同位角相等，或同旁内角和为两直角",
                "则两直线平行",
            ],
            wait_time=3,
        )
        self.wait(1)
        self.hide_title(title)

        setup_text = Text(
            "已知EF与AB、CD相交于G、H",
            font_size=30,
            color=YELLOW,
        ).to_edge(UP, buff=0.0)
        self.play(Write(setup_text))

        G = np.array([-1.1, 0.8, 0.0])
        H = np.array([1.0, -0.8, 0.0])
        slope = 0.22
        A = G + np.array([-2.15, -2.15 * slope, 0.0])
        B = G + np.array([2.35, 2.35 * slope, 0.0])
        C = H + np.array([-2.15, -2.15 * slope, 0.0])
        D = H + np.array([2.35, 2.35 * slope, 0.0])
        gh_dir = (H - G) / np.linalg.norm(H - G)
        E = G - gh_dir * 1.35
        F = H + gh_dir * 1.35

        line_AB = Line(A, B, color=WHITE, stroke_width=4)
        line_CD = Line(C, D, color=WHITE, stroke_width=4)
        line_EF = Line(E, F, color=YELLOW, stroke_width=4)
        dots = VGroup(*[Dot(p, color=WHITE, radius=0.06) for p in [A, B, C, D, E, F, G, H]])
        labels = VGroup(
            Text("A", font_size=38).next_to(A, LEFT, buff=0.10),
            Text("B", font_size=38).next_to(B, RIGHT, buff=0.10),
            Text("C", font_size=38).next_to(C, LEFT, buff=0.10),
            Text("D", font_size=38).next_to(D, RIGHT, buff=0.10),
            Text("E", font_size=38).next_to(E, UP + LEFT, buff=0.08),
            Text("F", font_size=38).next_to(F, DOWN + RIGHT, buff=0.08),
            Text("G", font_size=38).next_to(G, UP, buff=0.28),
            Text("H", font_size=38).next_to(H, DOWN, buff=0.28),
        )

        def angle_arc(center, start_point, end_point, radius, color):
            start = np.arctan2(start_point[1] - center[1], start_point[0] - center[0])
            end = np.arctan2(end_point[1] - center[1], end_point[0] - center[0])
            sweep = (end - start + PI) % TAU - PI
            return Arc(
                radius=radius,
                start_angle=start,
                angle=sweep,
                arc_center=center,
                color=color,
                stroke_width=4,
            )

        angle_EGB = angle_arc(G, E, B, 0.26, BLUE)
        angle_AGH = angle_arc(G, A, H, 0.36, GREEN)
        angle_BGH = angle_arc(G, B, H, 0.46, ORANGE)
        angle_GHD = angle_arc(H, G, D, 0.26, BLUE)

        self.play(Create(line_AB), Create(line_CD), Create(line_EF))
        self.play(Create(angle_EGB), Create(angle_GHD))
        self.play(Create(dots), Write(labels))
        known_1 = Text("情况一: ∠EGB=∠GHD", font_size=28, color=GRAY)
        known_1.next_to(setup_text, DOWN, buff=0.12)
        known_2 = Text("情况二: ∠BGH+∠GHD=两直角", font_size=28, color=GRAY)
        known_2.next_to(known_1, DOWN, buff=0.12)
        self.play(Write(known_1), Write(known_2))
        self.wait(1.5)
        self.play(FadeOut(setup_text), FadeOut(known_1), FadeOut(known_2))

        self.play(Create(angle_AGH), Create(angle_BGH))
        geometry_group = VGroup(
            line_AB, line_CD, line_EF, dots, labels,
            angle_EGB, angle_AGH, angle_BGH, angle_GHD,
        )
        self.play(geometry_group.animate.shift(UP * 2.75))
        self.wait(0.5)

        proof_title = Text("证明:", font_size=36, color=YELLOW).shift(DOWN * 1.0)
        self.play(Write(proof_title))

        case_1_title = Text("第一种情况: 同位角相等", font_size=30, color=YELLOW)
        case_1_title.next_to(proof_title, DOWN, buff=0.28)
        p1 = Text("∵ ∠EGB=∠GHD（已知）", font_size=26).next_to(case_1_title, DOWN, buff=0.22)
        p2 = Text("且∠EGB=∠AGH", font_size=26).next_to(p1, DOWN, buff=0.22)
        p2_note = Text("（命题1.15: 对顶角相等）", font_size=22, color=GRAY).next_to(p2, DOWN, buff=0.10)
        p3 = Text("∴ ∠AGH=∠GHD", font_size=28, color=GREEN).next_to(p2_note, DOWN, buff=0.22)
        p4 = Text("它们是内错角，∴ AB平行于CD", font_size=28, color=GREEN).next_to(p3, DOWN, buff=0.24)
        p4_note = Text("（命题1.27: 内错角相等，则两直线平行）", font_size=21, color=GRAY)
        p4_note.next_to(p4, DOWN, buff=0.10)

        self.play(Write(case_1_title))
        self.play(
            Write(p1),
            angle_EGB.animate.set_stroke(color=BLUE, width=5),
            angle_GHD.animate.set_stroke(color=BLUE, width=5),
        )
        self.wait(0.8)
        self.play(
            Write(p2),
            Write(p2_note),
            angle_AGH.animate.set_stroke(color=GREEN, width=5),
        )
        self.wait(0.8)
        self.play(Write(p3))
        self.wait(0.8)
        self.play(
            Write(p4),
            Write(p4_note),
            line_AB.animate.set_stroke(color=GREEN, width=5),
            line_CD.animate.set_stroke(color=GREEN, width=5),
        )
        self.wait(1.5)

        case_1_group = VGroup(case_1_title, p1, p2, p2_note, p3, p4, p4_note)
        self.play(
            FadeOut(case_1_group),
            angle_EGB.animate.set_stroke(color=BLUE, width=4),
            angle_AGH.animate.set_stroke(color=GREEN, width=4),
            angle_GHD.animate.set_stroke(color=BLUE, width=4),
            line_AB.animate.set_stroke(color=WHITE, width=4),
            line_CD.animate.set_stroke(color=WHITE, width=4),
        )

        case_2_title = Text("第二种情况: 同旁内角和为两直角", font_size=28, color=YELLOW)
        case_2_title.next_to(proof_title, DOWN, buff=0.26)
        q1 = Text("∵ ∠BGH+∠GHD=两直角（已知）", font_size=24)
        q1.next_to(case_2_title, DOWN, buff=0.20)
        q2 = Text("且∠AGH+∠BGH=两直角", font_size=24).next_to(q1, DOWN, buff=0.20)
        q2_note = Text("（命题1.13: 邻角和为两直角）", font_size=21, color=GRAY).next_to(q2, DOWN, buff=0.10)
        q3 = Text("∴ ∠AGH+∠BGH=∠BGH+∠GHD", font_size=23)
        q3.next_to(q2_note, DOWN, buff=0.20)
        q4 = Text("两边同减∠BGH，得∠AGH=∠GHD", font_size=24, color=GREEN)
        q4.next_to(q3, DOWN, buff=0.20)
        q4_note = Text("（公理3: 等量减等量，其差相等）", font_size=21, color=GRAY).next_to(q4, DOWN, buff=0.10)
        q5 = Text("它们是内错角，∴ AB平行于CD", font_size=28, color=GREEN).next_to(q4_note, DOWN, buff=0.20)
        q5_note = Text("（命题1.27）", font_size=22, color=GRAY).next_to(q5, DOWN, buff=0.10)

        self.play(Write(case_2_title))
        self.play(
            Write(q1),
            angle_BGH.animate.set_stroke(color=ORANGE, width=5),
            angle_GHD.animate.set_stroke(color=ORANGE, width=5),
        )
        self.wait(0.8)
        self.play(
            Write(q2),
            Write(q2_note),
            angle_AGH.animate.set_stroke(color=GREEN, width=5),
        )
        self.wait(0.8)
        self.play(Write(q3))
        self.wait(0.8)
        self.play(Write(q4), Write(q4_note))
        self.wait(0.8)
        self.play(
            Write(q5),
            Write(q5_note),
            line_AB.animate.set_stroke(color=GREEN, width=5),
            line_CD.animate.set_stroke(color=GREEN, width=5),
        )
        self.wait(1.5)

        case_2_group = VGroup(case_2_title, q1, q2, q2_note, q3, q4, q4_note, q5, q5_note)
        self.play(FadeOut(case_2_group), FadeOut(proof_title))

        conclusion_title = Text("结论:", font_size=38, color=YELLOW).shift(DOWN * 1.0)
        conclusion_1 = Text("同位角相等，或同旁内角和为两直角", font_size=30, color=GREEN)
        conclusion_1.next_to(conclusion_title, DOWN, buff=0.35)
        conclusion_2 = Text("则AB平行于CD", font_size=34, color=GREEN).next_to(conclusion_1, DOWN, buff=0.25)
        qed = Text("(Q.E.D.)", font_size=28, color=GREEN).next_to(conclusion_2, DOWN, buff=0.25)

        self.play(Write(conclusion_title))
        self.play(Write(conclusion_1))
        self.play(Write(conclusion_2))
        self.play(Write(qed))
        self.wait(2)

        final_group = VGroup(geometry_group, conclusion_title, conclusion_1, conclusion_2, qed)
        self.play(FadeOut(final_group))
        self.wait(1)
