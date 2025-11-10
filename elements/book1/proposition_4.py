from manim import *
from utils.base_scene import ElementsScene

class Proposition4(ElementsScene):
    def construct(self):
        self.setup_proposition(1, 4)

        # 1. 显示标题
        title = self.show_title(
            "卷一, 命题4",
            ["如果两个三角形，一个的两边分别等于另一个的两边",
            "且相等线段所夹的角相等，那么它们的底边相等",
            "两个三角形全等，且其余的角也分别相等"],
            wait_time=4.5
        )
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）- 绘制两个三角形

        # 三角形ABC - 左侧
        A = np.array([-4, 0.5, 0])
        B = np.array([-5.5, -1.5, 0])
        C = np.array([-2, -1.5, 0])

        # 三角形DEF - 右侧
        D = np.array([2, 0.5, 0])
        E = np.array([0.5, -1.5, 0])
        F = np.array([4, -1.5, 0])

        # 绘制三角形ABC
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

        # 绘制三角形DEF
        line_DE = Line(D, E, color=WHITE, stroke_width=2)
        line_DF = Line(D, F, color=WHITE, stroke_width=2)
        line_EF = Line(E, F, color=BLUE, stroke_width=2)

        self.play(Create(line_DE))
        self.wait(0.3)
        self.play(Create(line_DF))
        self.wait(0.3)
        self.play(Create(line_EF))
        self.wait(0.5)

        # 标注三角形DEF的点
        label_D = Text("D", font_size=42, color=YELLOW).next_to(D, UP, buff=0.2)
        label_E = Text("E", font_size=42, color=YELLOW).next_to(E, LEFT, buff=0.2)
        label_F = Text("F", font_size=42, color=YELLOW).next_to(F, RIGHT, buff=0.2)

        self.play(Write(label_D), Write(label_E), Write(label_F))
        self.wait(1)

        # 标记相等的边
        mark_AB = Text("a", font_size=32, color=GREEN).move_to((A + B) / 2).shift(LEFT * 0.3)
        mark_AC = Text("b", font_size=32, color=GREEN).move_to((A + C) / 2).shift(RIGHT * 0.3)
        mark_DE = Text("a", font_size=32, color=GREEN).move_to((D + E) / 2).shift(LEFT * 0.3)
        mark_DF = Text("b", font_size=32, color=GREEN).move_to((D + F) / 2).shift(RIGHT * 0.3)

        self.play(
            Write(mark_AB), Write(mark_AC),
            Write(mark_DE), Write(mark_DF)
        )
        self.wait(0.5)

        # 标记相等的角
        # 计算角BAC的起始角度和角度范围
        vec_AB = B - A
        vec_AC = C - A
        angle_AB = np.arctan2(vec_AB[1], vec_AB[0])
        angle_AC = np.arctan2(vec_AC[1], vec_AC[0])

        # 计算角DEF的起始角度和角度范围
        vec_DE = E - D
        vec_DF = F - D
        angle_DE = np.arctan2(vec_DE[1], vec_DE[0])
        angle_DF = np.arctan2(vec_DF[1], vec_DF[0])

        angle_A = Arc(radius=0.4, start_angle=angle_AB, angle=angle_AC-angle_AB, color=RED, stroke_width=2).shift(A)
        angle_D = Arc(radius=0.4, start_angle=angle_DE, angle=angle_DF-angle_DE, color=RED, stroke_width=2).shift(D)

        self.play(Create(angle_A), Create(angle_D))
        self.wait(1)

        # 3. 准备证明 - 保持原大小，移到上半部分
        geometry_group = VGroup(
            line_AB, line_AC, line_BC,
            line_DE, line_DF, line_EF,
            label_A, label_B, label_C,
            label_D, label_E, label_F,
            mark_AB, mark_AC, mark_DE, mark_DF,
            angle_A, angle_D
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

        # 证明步骤1 - 移动三角形ABC使其与DEF重合
        proof_1 = Text(
            "把△ABC移到△DEF上，使A落在D上",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(0.5)

        # 创建三角形ABC的副本用于移动
        triangle_ABC = VGroup(
            line_AB.copy(),
            line_AC.copy(),
            line_BC.copy()
        )
        labels_ABC = VGroup(
            label_A.copy(),
            label_B.copy(),
            label_C.copy()
        )
        marks_ABC = VGroup(
            mark_AB.copy(),
            mark_AC.copy()
        )
        angle_ABC = angle_A.copy()

        # 计算移动向量：从A移动到D
        shift_vector = D - A

        # 移动三角形ABC到DEF位置
        self.play(
            triangle_ABC.animate.shift(shift_vector),
            labels_ABC.animate.shift(shift_vector),
            marks_ABC.animate.shift(shift_vector),
            angle_ABC.animate.shift(shift_vector),
            run_time=2
        )
        self.wait(0.5)

        # 调整标签位置避免重叠
        # A和D的标签：A在左上，D在右上
        new_label_A = labels_ABC[0]
        self.play(
            new_label_A.animate.shift(LEFT * 0.3 + UP * 0.1),
            label_D.animate.shift(RIGHT * 0.3 + UP * 0.1)
        )

        # B和E的标签：B在左下偏左，E在左下偏右
        new_label_B = labels_ABC[1]
        self.play(
            new_label_B.animate.shift(LEFT * 0.3),
            label_E.animate.shift(RIGHT * 0.3)
        )

        # C和F的标签：C在右下偏左，F在右下偏右
        new_label_C = labels_ABC[2]
        self.play(
            new_label_C.animate.shift(LEFT * 0.3),
            label_F.animate.shift(RIGHT * 0.3)
        )
        self.wait(1)

        # 证明步骤2
        self.play(
            line_AB.animate.set_stroke(color=GREEN, width=4),
            line_DE.animate.set_stroke(color=GREEN, width=4)
        )
        proof_2 = Text(
            "∵ AB=DE，直线AB与DE重合，B与E重合",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤3
        self.play(
            line_AB.animate.set_stroke(color=WHITE, width=2),
            line_DE.animate.set_stroke(color=WHITE, width=2),
            angle_A.animate.set_stroke(color=YELLOW, width=4),
            angle_D.animate.set_stroke(color=YELLOW, width=4)
        )
        proof_3 = Text(
            "∵ ∠BAC=∠EDF，∴ AC与DF重合",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤4
        self.play(
            angle_A.animate.set_stroke(color=RED, width=2),
            angle_D.animate.set_stroke(color=RED, width=2),
            line_AC.animate.set_stroke(color=GREEN, width=4),
            line_DF.animate.set_stroke(color=GREEN, width=4)
        )
        proof_4 = Text(
            "∵ AC=DF，∴ 点C与点F重合",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤5
        self.play(
            line_AC.animate.set_stroke(color=WHITE, width=2),
            line_DF.animate.set_stroke(color=WHITE, width=2),
            line_BC.animate.set_stroke(color=YELLOW, width=4),
            line_EF.animate.set_stroke(color=YELLOW, width=4)
        )
        proof_5 = Text(
            "∵ B与E重合，C与F重合，∴ BC与EF重合",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.5)

        # 证明步骤6
        proof_6 = Text(
            "∴ BC=EF，△ABC≌△DEF（公理4）",
            font_size=32
        ).next_to(proof_5, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤7
        self.play(
            line_BC.animate.set_stroke(color=BLUE, width=2),
            line_EF.animate.set_stroke(color=BLUE, width=2)
        )
        proof_7 = Text(
            "∴ 其余的角也重合且相等（公理4）",
            font_size=32
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 5. 结论 - 分两行显示
        conclusion_line1 = Text(
            "∴ 两边及夹角相等的三角形全等",
            font_size=36,
            color=GREEN
        ).next_to(proof_7, DOWN, buff=0.4)

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
            FadeOut(triangle_ABC),
            FadeOut(labels_ABC),
            FadeOut(marks_ABC),
            FadeOut(angle_ABC),
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
