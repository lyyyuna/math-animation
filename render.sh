#!/bin/bash

# Euclid's Elements Animation Renderer
# Usage: ./render.sh <book> <proposition> [quality]
# Example: ./render.sh 1 1 -ql (render Book 1, Proposition 1 in low quality)

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 显示使用说明
show_usage() {
    echo "Usage: $0 <book> <proposition> [quality]"
    echo ""
    echo "Arguments:"
    echo "  book          Book number (1-13)"
    echo "  proposition   Proposition number"
    echo "  quality       Quality flag (optional, default: -qhp):"
    echo ""
    echo "                Mobile Portrait (9:16) - 推荐用于手机观看:"
    echo "                -qlp  Low quality portrait (480x854)"
    echo "                -qmp  Medium quality portrait (720x1280)"
    echo "                -qhp  High quality portrait (1080x1920) [DEFAULT]"
    echo "                -qkp  4K portrait (2160x3840)"
    echo ""
    echo "                Desktop Landscape (16:9):"
    echo "                -ql   Low quality landscape"
    echo "                -qm   Medium quality landscape"
    echo "                -qh   High quality landscape"
    echo "                -qk   4K quality landscape"
    echo ""
    echo "Examples:"
    echo "  $0 1 1          # 默认：手机竖屏高质量 (1080x1920)"
    echo "  $0 1 1 -qlp     # 手机竖屏低质量预览 (480x854)"
    echo "  $0 1 1 -qkp     # 手机竖屏4K (2160x3840)"
    echo "  $0 1 1 -qh      # 电脑横屏高质量 (1920x1080)"
    exit 1
}

# 检查参数
if [ $# -lt 2 ]; then
    echo -e "${RED}Error: Missing required arguments${NC}"
    show_usage
fi

BOOK=$1
PROP=$2
QUALITY=${3:--qhp}  # 默认使用手机竖屏高质量渲染

# 验证 book 和 proposition
if ! [[ "$BOOK" =~ ^[0-9]+$ ]] || [ "$BOOK" -lt 1 ] || [ "$BOOK" -gt 13 ]; then
    echo -e "${RED}Error: Book number must be between 1 and 13${NC}"
    exit 1
fi

if ! [[ "$PROP" =~ ^[0-9]+$ ]] || [ "$PROP" -lt 1 ]; then
    echo -e "${RED}Error: Proposition number must be a positive integer${NC}"
    exit 1
fi

# 构建文件路径
SCENE_FILE="elements/book${BOOK}/proposition_${PROP}.py"

# 检查文件是否存在
if [ ! -f "$SCENE_FILE" ]; then
    echo -e "${RED}Error: Scene file not found: $SCENE_FILE${NC}"
    echo -e "${YELLOW}Tip: Create the file with the following structure:${NC}"
    echo ""
    echo "from manim import *"
    echo "from utils.base_scene import ElementsScene"
    echo ""
    echo "class Proposition${PROP}(ElementsScene):"
    echo "    def construct(self):"
    echo "        self.setup_proposition($BOOK, $PROP)"
    echo "        # Your animation code here"
    exit 1
fi

# 提取场景类名
SCENE_CLASS="Proposition${PROP}"

# 输出目录
OUTPUT_DIR="output/book${BOOK}"
mkdir -p "$OUTPUT_DIR"

echo -e "${GREEN}==================================${NC}"
echo -e "${GREEN}Rendering Elements Animation${NC}"
echo -e "${GREEN}==================================${NC}"
echo -e "Book:        ${YELLOW}$BOOK${NC}"
echo -e "Proposition: ${YELLOW}$PROP${NC}"
echo -e "Quality:     ${YELLOW}$QUALITY${NC}"
echo -e "Scene File:  ${YELLOW}$SCENE_FILE${NC}"
echo -e "${GREEN}==================================${NC}"
echo ""

# 运行 manim
echo -e "${GREEN}Starting render...${NC}"
# 设置 PYTHONPATH 以便找到项目模块
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)"

# 检查是否为竖屏模式
RESOLUTION_FLAG=""
case $QUALITY in
    -qlp)
        RESOLUTION_FLAG="-ql --resolution 480,854"
        ;;
    -qmp)
        RESOLUTION_FLAG="-qm --resolution 720,1280"
        ;;
    -qhp)
        RESOLUTION_FLAG="-qh --resolution 1080,1920"
        ;;
    -qkp)
        RESOLUTION_FLAG="-qk --resolution 2160,3840"
        ;;
    *)
        RESOLUTION_FLAG="$QUALITY"
        ;;
esac

manim $RESOLUTION_FLAG "$SCENE_FILE" "$SCENE_CLASS" -o "book${BOOK}_prop${PROP}.mp4"

# 检查渲染结果
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}==================================${NC}"
    echo -e "${GREEN}Render completed successfully!${NC}"
    echo -e "${GREEN}==================================${NC}"

    # 查找生成的视频文件
    VIDEO_FILE=$(find media -name "book${BOOK}_prop${PROP}.mp4" -type f -printf '%T@ %p\n' | sort -rn | head -1 | cut -d' ' -f2-)

    if [ -n "$VIDEO_FILE" ]; then
        echo -e "Output: ${YELLOW}$VIDEO_FILE${NC}"

        # 获取文件大小
        SIZE=$(du -h "$VIDEO_FILE" | cut -f1)
        echo -e "Size:   ${YELLOW}$SIZE${NC}"
    fi
else
    echo ""
    echo -e "${RED}==================================${NC}"
    echo -e "${RED}Render failed!${NC}"
    echo -e "${RED}==================================${NC}"
    exit 1
fi
