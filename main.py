from manim import *

class KochSnowflake(Scene):
    def construct(self):
        # 初始三角形
        points = [
            np.array([-2, -np.sqrt(3)/2, 0]),
            np.array([2, -np.sqrt(3)/2, 0]),
            np.array([0, np.sqrt(3), 0]),
            np.array([-2, -np.sqrt(3)/2, 0])
        ]
        triangle = VMobject()
        triangle.set_points_as_corners(points)
        
        # 迭代次数
        iterations = 4
        
        # 科赫曲线生成函数
        def koch_curve(p1, p2, level):
            if level == 0:
                return [p1, p2]
            else:
                # 分割线段为三等分
                pA = p1 + (p2 - p1) / 3
                pB = p1 + 2 * (p2 - p1) / 3
                
                # 计算凸起点的位置
                angle = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
                pC = p1 + (p2 - p1) / 2
                length = np.linalg.norm(p2 - p1) / 3
                pC += np.array([-np.sin(angle), np.cos(angle), 0]) * length * np.sqrt(3)
                
                # 递归调用
                return (
                    koch_curve(p1, pA, level - 1)[:-1] +
                    koch_curve(pA, pC, level - 1)[:-1] +
                    koch_curve(pC, pB, level - 1)[:-1] +
                    koch_curve(pB, p2, level - 1)
                )
        
        # 创建科赫雪花
        snowflake_points = []
        for i in range(3):
            p1 = points[i]
            p2 = points[i+1]
            snowflake_points += koch_curve(p1, p2, iterations)[:-1]
        
        snowflake = VMobject()
        snowflake.set_points_as_corners(snowflake_points + [snowflake_points[0]])
        snowflake.set_color(BLUE)
        
        self.play(Create(triangle))
        self.wait(0.5)
        self.play(Transform(triangle, snowflake))
        self.wait(2)