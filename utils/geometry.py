"""
Common geometry helper functions for Elements
"""
from manim import *
import numpy as np


def construct_equilateral_triangle(p1: np.ndarray, p2: np.ndarray) -> np.ndarray:
    """
    根据两点构造等边三角形的第三个顶点
    """
    # 计算边长
    side_length = np.linalg.norm(p2 - p1)

    # 计算中点
    midpoint = (p1 + p2) / 2

    # 计算垂直方向
    direction = p2 - p1
    perpendicular = np.array([-direction[1], direction[0], 0])
    perpendicular = perpendicular / np.linalg.norm(perpendicular)

    # 第三个顶点
    height = side_length * np.sqrt(3) / 2
    p3 = midpoint + perpendicular * height

    return p3


def angle_between_points(p1: np.ndarray, vertex: np.ndarray, p2: np.ndarray) -> float:
    """
    计算三点形成的角度（弧度）
    """
    v1 = p1 - vertex
    v2 = p2 - vertex

    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(np.clip(cos_angle, -1, 1))

    return angle


def distance_between_points(p1: np.ndarray, p2: np.ndarray) -> float:
    """
    计算两点间距离
    """
    return np.linalg.norm(p2 - p1)
