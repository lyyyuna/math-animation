from manim import *
from utils.base_scene import ElementsScene

class Proposition6(ElementsScene):
    """
    命题 6: 如果一个三角形有两个角彼此相等，那么这两个角所对的边也彼此相等。

    已知：三角形 ABC，角 ABC = 角 ACB
    求证：边 AB = 边 AC

    证明方法：反证法
    """

    def construct(self):
        self.setup_proposition(1, 6)

        # 1. 显示标题和问题陈述
        title = self.show_title(
            "卷 I, 命题 6",
            ["在一个三角形里，如果有两个角彼此相等","那么这两个角所对的边也彼此相等"]
        )
        self.wait(1)
        self.hide_title(title)

        # 显示已知和求证
        given_text = Text(
            "已知: △ABC，∠ABC = ∠ACB",
            font_size=38,
            color=BLUE
        ).shift(UP * 2)

        prove_text = Text(
            "求证: AB = AC",
            font_size=38,
            color=YELLOW
        ).next_to(given_text, DOWN, buff=0.4)

        self.play(Write(given_text))
        self.wait(1)
        self.play(Write(prove_text))
        self.wait(2)
        self.play(FadeOut(given_text), FadeOut(prove_text))
        self.wait(0.5)

        # 2. 作图过程 - 构造三角形ABC（看起来 AB 稍长于 AC）
        A = np.array([0, 2, 0])
        B = np.array([-2.5, -1, 0])  # 让 AB 明显比 AC 长
        C = np.array([1.6, -1, 0])  # AC 稍短

        # 创建三角形ABC
        line_AB = Line(A, B, color=WHITE)
        line_AC = Line(A, C, color=WHITE)
        line_BC = Line(B, C, color=WHITE)

        self.play(Create(line_AB))
        self.wait(0.3)
        self.play(Create(line_AC))
        self.wait(0.3)
        self.play(Create(line_BC))
        self.wait(0.5)

        # 标注点
        label_A = Text("A", font_size=42).next_to(A, UP, buff=0.2)
        label_B = Text("B", font_size=42).next_to(B, DOWN + LEFT, buff=0.2)
        label_C = Text("C", font_size=42).next_to(C, DOWN + RIGHT, buff=0.2)

        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C)
        )
        self.wait(0.5)

        # 标注角 ABC 和角 ACB（用小弧线表示等角）
        angle_ABC = Arc(
            radius=0.4,
            start_angle=Line(B, C).get_angle(),
            angle=Line(B, A).get_angle() - Line(B, C).get_angle(),
            color=YELLOW,
            arc_center=B
        )

        angle_ACB = Arc(
            radius=0.4,
            start_angle=Line(C, B).get_angle(),
            angle=Line(C, A).get_angle() - Line(C, B).get_angle(),
            color=YELLOW,
            arc_center=C
        )

        self.play(Create(angle_ABC), Create(angle_ACB))
        self.wait(0.3)

        # 添加角的标记（双弧线表示相等）
        angle_ABC_2 = Arc(
            radius=0.5,
            start_angle=Line(B, C).get_angle(),
            angle=Line(B, A).get_angle() - Line(B, C).get_angle(),
            color=YELLOW,
            arc_center=B
        )

        angle_ACB_2 = Arc(
            radius=0.5,
            start_angle=Line(C, B).get_angle(),
            angle=Line(C, A).get_angle() - Line(C, B).get_angle(),
            color=YELLOW,
            arc_center=C
        )

        self.play(Create(angle_ABC_2), Create(angle_ACB_2))
        self.wait(1)

        # 3. 反证法作图 - 在 AB 上截取 DB = AC
        # 计算 D 点位置（假设 AB 稍长于 AC）
        # 为了演示，我们稍微调整使 AB 看起来比 AC 长一点点
        AB_vec = B - A
        AC_length = np.linalg.norm(C - A)
        AB_length = np.linalg.norm(AB_vec)

        # D 点在 AB 上，使得 DB = AC
        # AD = AB - DB = AB - AC
        D = A + AB_vec * (AB_length - AC_length) / AB_length

        # 显示说明：在 AB 上截取 DB = AC
        construction_text = Text(
            "在AB上截取DB=AC (命题1.3: 截取相等线段)",
            font_size=32,
            color=BLUE
        ).to_edge(UP)
        self.play(Write(construction_text))
        self.wait(1)

        # 标注点 D
        point_D = Dot(D, color=RED)
        label_D = Text("D", font_size=42, color=RED).next_to(D, UP + LEFT, buff=0.2)

        self.play(
            FadeIn(point_D),
            Write(label_D)
        )
        self.wait(0.5)

        # 连接 DC
        connection_text = Text(
            "连接DC (公设1: 两点确定一条直线)",
            font_size=32,
            color=GREEN
        ).to_edge(UP)
        self.play(
            FadeOut(construction_text),
            Write(connection_text)
        )
        self.wait(1)

        line_DC = Line(D, C, color=GREEN)
        self.play(Create(line_DC))
        self.wait(1)

        self.play(FadeOut(connection_text))
        self.wait(0.5)

        # 4. 移动图形到上半部分，准备证明
        geometry_group = VGroup(
            line_AB, line_AC, line_BC, line_DC,
            label_A, label_B, label_C, label_D,
            point_D,
            angle_ABC, angle_ACB, angle_ABC_2, angle_ACB_2
        )

        self.play(geometry_group.animate.shift(UP * 3.2))
        self.wait(0.5)

        # 5. 展示证明过程 - 使用反证法
        proof_title = Text("证明 (反证法):", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))
        self.wait(0.5)

        # 证明步骤 1: 假设 AB ≠ AC
        proof_1 = Text(
            "假设 AB ≠ AC，且 AB > AC",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤 2: DB = AC, BC 是公共边
        self.play(
            line_DC.animate.set_stroke(color=BLUE, width=4),
            line_AC.animate.set_stroke(color=BLUE, width=4)
        )
        proof_2 = Text(
            "∵ DB=AC，BC是公共边",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # 证明步骤 3: 两边相等
        self.play(
            line_DC.animate.set_stroke(color=WHITE, width=2),
            line_AC.animate.set_stroke(color=WHITE, width=2),
            line_BC.animate.set_stroke(color=BLUE, width=4)
        )
        proof_3 = Text(
            "两边DB、BC分别与边AC、CB相等",
            font_size=32
        ).next_to(proof_2, DOWN, buff=0.35)
        self.play(Write(proof_3))
        self.wait(1.5)

        # 证明步骤 4: 角相等
        self.play(
            line_BC.animate.set_stroke(color=WHITE, width=2),
            angle_ABC.animate.set_stroke(color=BLUE, width=4),
            angle_ABC_2.animate.set_stroke(color=BLUE, width=4)
        )
        proof_4 = Text(
            "且∠DBC=∠ACB (已知)",
            font_size=32
        ).next_to(proof_3, DOWN, buff=0.35)
        self.play(Write(proof_4))
        self.wait(1.5)

        # 证明步骤 5: 应用命题 1.4
        self.play(
            angle_ABC.animate.set_stroke(color=YELLOW, width=2),
            angle_ABC_2.animate.set_stroke(color=YELLOW, width=2)
        )
        proof_5 = Text(
            "∴ △DBC≌△ACB",
            font_size=32
        ).next_to(proof_4, DOWN, buff=0.35)
        self.play(Write(proof_5))
        self.wait(1.0)

        # 说明命题 1.4
        proof_5b = Text(
            "(命题1.4: 两边及其夹角对应相等)",
            font_size=28,
            color=GRAY
        ).next_to(proof_5, DOWN, buff=0.2)
        self.play(Write(proof_5b))
        self.wait(1.5)

        # 证明步骤 6: 矛盾
        proof_6 = Text(
            "即小的(△DBC)=大的(△ACB)",
            font_size=32,
            color=RED
        ).next_to(proof_5b, DOWN, buff=0.35)
        self.play(Write(proof_6))
        self.wait(1.5)

        # 证明步骤 7: 违反公理 5
        proof_7 = Text(
            "这违反了公理5(整体大于部分)",
            font_size=32,
            color=RED
        ).next_to(proof_6, DOWN, buff=0.35)
        self.play(Write(proof_7))
        self.wait(1.5)

        # 证明步骤 8: 结论
        proof_8 = Text(
            "∴ 假设不成立，AB=AC",
            font_size=32,
            color=GREEN
        ).next_to(proof_7, DOWN, buff=0.35)
        self.play(Write(proof_8))
        self.wait(2)

        # 6. 显示结论
        # 淡出辅助线（保留红色矛盾文字）
        self.play(
            FadeOut(line_DC),
            FadeOut(point_D),
            FadeOut(label_D)
        )

        # 让三角形变形为真正的等腰三角形（AB = AC）
        # 计算新的 B 点位置，使 AB = AC
        A_shifted = A + UP * 3.2
        C_shifted = C + UP * 3.2
        AC_length_current = np.linalg.norm(C - A)

        # 新的 B 点：使 AB = AC，保持角度，只调整长度
        AB_direction = (B - A) / np.linalg.norm(B - A)
        B_new = A + AB_direction * AC_length_current + UP * 3.2

        # 创建新的线段
        line_AB_new = Line(A_shifted, B_new, color=GREEN, stroke_width=4)
        line_AC_new = Line(A_shifted, C_shifted, color=GREEN, stroke_width=4)
        line_BC_new = Line(B_new, C_shifted, color=WHITE, stroke_width=2)

        label_B_new = Text("B", font_size=42).next_to(B_new, DOWN + LEFT, buff=0.2)

        # 计算新的角B的弧线
        angle_ABC_new = Arc(
            radius=0.4,
            start_angle=Line(B_new, C_shifted).get_angle(),
            angle=Line(B_new, A_shifted).get_angle() - Line(B_new, C_shifted).get_angle(),
            color=YELLOW,
            arc_center=B_new
        )

        angle_ABC_2_new = Arc(
            radius=0.5,
            start_angle=Line(B_new, C_shifted).get_angle(),
            angle=Line(B_new, A_shifted).get_angle() - Line(B_new, C_shifted).get_angle(),
            color=YELLOW,
            arc_center=B_new
        )

        # 动画：三角形变形
        self.play(
            Transform(line_AB, line_AB_new),
            Transform(line_AC, line_AC_new),
            Transform(line_BC, line_BC_new),
            Transform(label_B, label_B_new),
            Transform(angle_ABC, angle_ABC_new),
            Transform(angle_ABC_2, angle_ABC_2_new),
            run_time=2
        )
        self.wait(1)

        conclusion_line1 = Text(
            "如果三角形有两个角相等",
            font_size=36,
            color=GREEN
        ).next_to(proof_8, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "那么这两个角所对的边也相等",
            font_size=36,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        qed = Text(
            "(Q.E.D.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line2, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.play(Write(qed))
        self.wait(2)

        # 7. 结束动画
        self.play(
            FadeOut(line_AB),
            FadeOut(line_AC),
            FadeOut(line_BC),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            FadeOut(angle_ABC),
            FadeOut(angle_ACB),
            FadeOut(angle_ABC_2),
            FadeOut(angle_ACB_2),
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            FadeOut(proof_3),
            FadeOut(proof_4),
            FadeOut(proof_5),
            FadeOut(proof_5b),
            FadeOut(proof_6),
            FadeOut(proof_7),
            FadeOut(proof_8),
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2),
            FadeOut(qed)
        )
        self.wait(1)
