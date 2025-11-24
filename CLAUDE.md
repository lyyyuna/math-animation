# 欧几里得《几何原本》动画制作规范

## 设备适配说明

本项目主要针对**手机竖屏**观看优化（9:16 比例）。布局采用**上下结构**：
- **上半部分**：缩小的几何图形
- **下半部分**：证明过程文字

## 标准动画流程

每个命题的动画应遵循以下标准结构：

### 1. 显示标题和问题陈述
- 显示命题标题（卷数和命题编号，字体56）
- 显示问题的完整陈述（字体42）
- 等待一段时间后隐藏标题

### 2. 作图过程（全屏）
- **在全屏范围内展示作图步骤**
- 按照欧几里得的作图顺序逐步构造图形
- 清楚标注所有关键点和线段
- 使用不同颜色区分不同的几何元素
- 每个作图步骤之间适当等待，让观众理解

### 3. 准备证明（布局调整 - 手机竖屏）
- **将完整的几何图形组合成一个 `VGroup`**
- 包括所有图形元素：线段、圆、三角形、点、标签等
- **不缩小图形，保持原始大小**
- **将图形向上移动 (`shift(UP * 3.2)`)**
- 图形和证明文字以水平中心线完全分隔

### 4. 展示证明过程
- **证明文字显示在下半部分**
- 证明标题居中，使用 `.shift(DOWN * 2.0)` 定位
- 字体较大，便于手机阅读
- 按照逻辑顺序逐步展示证明步骤
- 配合图形高亮来说明每一步推理
  - 使用 `set_stroke(color=COLOR, width=4)` 高亮相关元素
  - 证明完该步骤后恢复正常粗细
- 每个证明步骤之间适当等待

### 5. 显示结论
- 淡出辅助图形（如辅助圆）
- 突出显示最终结果
- 添加 Q.E.D. 或 Q.E.F. 标记
  - Q.E.D. (Quod Erat Demonstrandum) - "这就是所要证明的" - 用于证明题
  - Q.E.F. (Quod Erat Faciendum) - "这就是所要作的" - 用于作图题

### 6. 结束动画
- 淡出所有元素
- 适当等待后结束

## 代码结构示例

```python
from manim import *
from utils.base_scene import ElementsScene

class PropositionN(ElementsScene):
    def construct(self):
        self.setup_proposition(book_number, prop_number)

        # 1. 显示标题
        title = self.show_title("卷 X, 命题 N", "命题的完整陈述")
        self.wait(1)
        self.hide_title(title)

        # 2. 作图过程（全屏）
        # 定义关键点
        A = np.array([...])
        B = np.array([...])

        # 逐步作图
        line_AB = Line(A, B, color=WHITE)
        self.play(Create(line_AB))

        # ... 更多作图步骤 ...

        # 3. 准备证明 - 移到上半部分（手机竖屏）
        geometry_group = VGroup(
            # 包含所有几何元素
            line_AB, circle_A, triangle,
            label_A, label_B, point_C, ...
        )
        self.play(
            geometry_group.animate.shift(UP * 3.2)
        )
        self.wait(0.5)

        # 4. 证明过程 - 文字显示在下半部分
        proof_title = Text("证明:", font_size=38, color=YELLOW)
        proof_title.shift(DOWN * 2.0)
        self.play(Write(proof_title))

        # 证明步骤1 - 配合高亮
        self.play(
            element1.animate.set_stroke(color=BLUE, width=4)
        )
        proof_1 = Text(
            "第一步推理...",
            font_size=32
        ).next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(proof_1))
        self.wait(1.5)

        # 证明步骤2
        self.play(
            element1.animate.set_stroke(color=ORIGINAL_COLOR, width=2),
            element2.animate.set_stroke(color=GREEN, width=4)
        )
        proof_2 = Text(
            "第二步推理...",
            font_size=32
        ).next_to(proof_1, DOWN, buff=0.35)
        self.play(Write(proof_2))
        self.wait(1.5)

        # ... 更多证明步骤 ...

        # 5. 结论 - 分两行显示
        conclusion_line1 = Text(
            "结论陈述",
            font_size=36,
            color=GREEN
        ).next_to(proof_N, DOWN, buff=0.4)

        conclusion_line2 = Text(
            "(Q.E.D./Q.E.F.)",
            font_size=30,
            color=GREEN
        ).next_to(conclusion_line1, DOWN, buff=0.2)

        self.play(Write(conclusion_line1))
        self.play(Write(conclusion_line2))
        self.wait(2)

        # 6. 结束
        self.play(
            FadeOut(geometry_group),
            FadeOut(proof_title),
            FadeOut(proof_1),
            FadeOut(proof_2),
            # ... 淡出所有证明文字 ...
            FadeOut(conclusion_line1),
            FadeOut(conclusion_line2)
        )
        self.wait(1)
```

## 布局参数调整指南（手机竖屏）

### 图形缩放和位移
- **不缩放图形**：保持原始大小，方便手机观看
- **上移距离**：`shift(UP * 3.2)` - 移到上半部分
  - 标准：UP * 3.2
  - 图形较小可用：UP * 3.0
  - 图形较大可用：UP * 3.5

### 文字布局
- **证明标题**：`.shift(DOWN * 2.0)` - 显示在下半部分顶部，居中
- **证明步骤**：`.next_to(上一个元素, DOWN, buff=0.35-0.4)` - 居中对齐
- **行间距**：0.35 - 0.4（适合手机阅读）
- **结论显示**：分两行显示
  - 第一行：结论陈述（字体36）
  - 第二行：(Q.E.D./Q.E.F.)（字体30）
  - 行间距：0.2
- **字体大小**（专为手机优化，大字体便于阅读）：
  - 命题标题：56
  - 命题说明：42
  - 点标签（A, B, C）：42
  - 证明标题：38
  - 证明步骤：32
  - 结论第一行：36
  - 结论第二行：30

### 颜色使用建议
- 基本线段：WHITE
- 辅助圆：BLUE, GREEN
- 高亮元素：增加 stroke width 到 4
- 结果三角形/多边形：YELLOW (fill_opacity=0.2)
- 证明标题：YELLOW
- 结论：GREEN

### 等待时间
- 显示标题后：1秒
- 每个作图步骤后：0.5 - 1秒
- 布局调整后：0.5秒
- 每个证明步骤后：1.5秒
- 显示结论后：2秒
- 结束前：1秒

## 注意事项

1. **模块导入**：确保正确导入 `utils.base_scene` 和 `utils.geometry`
2. **VGroup 组合**：证明前必须将所有几何元素组合到一个 VGroup 中
3. **高亮恢复**：每次高亮后记得恢复原始样式，避免影响下一步
4. **文字对齐**：使用 `aligned_edge=LEFT` 保持证明步骤左对齐
5. **淡出清理**：结束时统一淡出 geometry_group，简化代码

## 文件组织

```
math-animation/
├── elements/
│   ├── book1/
│   │   ├── __init__.py
│   │   ├── proposition_1.py
│   │   ├── proposition_2.py
│   │   └── ...
│   ├── book2/
│   └── ...
├── utils/
│   ├── __init__.py
│   ├── base_scene.py
│   └── geometry.py
├── render.sh
└── CLAUDE.md (本文件)
```

## 运行动画

```bash
./render.sh <book> <proposition> [quality]

# 手机竖屏渲染（默认）
./render.sh 1 1        # 默认：1080x1920 高质量竖屏
./render.sh 1 1 -qlp   # 480x854 低质量预览
./render.sh 1 1 -qmp   # 720x1280 中等质量
./render.sh 1 1 -qhp   # 1080x1920 高质量竖屏（同默认）
./render.sh 1 1 -qkp   # 2160x3840 4K竖屏

# 传统横屏渲染（需明确指定）
./render.sh 1 1 -qh    # 1920x1080 高质量横屏
./render.sh 1 1 -ql    # 低质量预览
./render.sh 1 1 -qk    # 4K质量横屏
```

## 常用公理和公设

### 公设 (Postulates)
1. **公设1**: 从任意一点到另一点可以作直线
2. **公设2**: 一条有限直线可以继续延长
3. **公设3**: 以任意点为圆心，任意长度为半径画圆
4. **公设4**: 所有直角都彼此相等
5. **公设5**: 若一条直线与两条直线相交，在同侧的内角和小于两直角，则这两条直线在不断延长后必在内角和小于两直角的一侧相交

### 公理 (Common Notions)
1. **公理1**: 与同量相等的量彼此相等
2. **公理2**: 等量加等量，其和相等
3. **公理3**: 等量减等量，其差相等
4. **公理4**: 彼此重合的物体是全等的
5. **公理5**: 整体大于部分

### 使用规范
- 当引用公理或公设时，在证明步骤中明确标注（例如：`公理1: 与同量相等的量彼此相等`）
- 作图过程中使用公设时，使用较大的字体（font_size=38）显示说明文字
- 证明过程中引用公理或公设时，字体大小与证明步骤一致（font_size=32）

## 数学符号和用语规范

为保持整个项目的一致性，所有命题必须使用以下标准化的数学符号和用语：

### 几何符号
- **角**: 使用 `∠` 符号
  - ✅ 正确：`∠ABC`、`∠ACB`
  - ❌ 错误：`角ABC`、`角 ABC`

- **三角形**: 使用 `△` 符号
  - ✅ 正确：`△ABC`、`△DBC`
  - ❌ 错误：`三角形ABC`、`三角形 ABC`

- **全等**: 使用 `≌` 符号
  - ✅ 正确：`△ABC≌△DEF`
  - ❌ 错误：`△ABC 全等 △DEF`

### 逻辑符号
- **因为**: 使用 `∵` 符号
  - ✅ 正确：`∵ AB=AC，BC是公共边`
  - ❌ 错误：`因为 AB=AC，BC是公共边`

- **所以**: 使用 `∴` 符号
  - ✅ 正确：`∴ △ABC≌△DEF`
  - ❌ 错误：`所以 △ABC≌△DEF`

### 文字间距规范
- **等式**: 等号两侧无空格
  - ✅ 正确：`AB=AC`、`∠ABC=∠ACB`
  - ❌ 错误：`AB = AC`、`∠ABC = ∠ACB`

- **逗号分隔**: 中文逗号后无空格
  - ✅ 正确：`AB=AC，BC是公共边`
  - ❌ 错误：`AB=AC, BC是公共边` 或 `AB=AC， BC是公共边`

- **线段点名**: 点名之间无空格
  - ✅ 正确：`线段AB`、`连接DC`
  - ❌ 错误：`线段 AB`、`连接 DC`

### 证明过程用语
- **已知**: 使用格式 `已知: △ABC，∠ABC=∠ACB`
- **求证**: 使用格式 `求证: AB=AC`
- **引用命题**: 使用括号说明，例如 `(命题1.4: 两边及其夹角对应相等)`
- **引用公理**: 使用括号说明，例如 `(公理5: 整体大于部分)`
- **引用公设**: 使用括号说明，例如 `(公设1: 两点确定一条直线)`

### 示例对照

**标准格式示例**（命题6）：
```python
# 已知和求证
given_text = Text("已知: △ABC，∠ABC=∠ACB", font_size=38)
prove_text = Text("求证: AB=AC", font_size=38)

# 证明步骤
proof_1 = Text("∵ DB=AC，BC是公共边", font_size=32)
proof_2 = Text("两边DB、BC分别与边AC、CB相等", font_size=32)
proof_3 = Text("且∠DBC=∠ACB (已知)", font_size=32)
proof_4 = Text("∴ △DBC≌△ACB", font_size=32)
proof_5 = Text("(命题1.4: 两边及其夹角对应相等)", font_size=28, color=GRAY)
```

### 注意事项
1. 所有新命题必须遵循此规范
2. 修改旧命题时，应同时更新符号使用
3. 符号的使用应当自然流畅，不影响阅读
4. 在引用公理、公设、命题时，可在括号内用中文简要说明其内容

## 参考实现

详见 `elements/book1/proposition_1.py` - 命题1的完整实现展示了所有标准流程。
