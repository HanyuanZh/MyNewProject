import numpy as np

def create_rotation_matrix(rotate_z, rotate_y, rotate_x):
    # 定义余弦和正弦函数
    c = np.cos
    s = np.sin
    alpha = np.radians(rotate_z)
    beta = np.radians(rotate_y)
    gamma = np.radians(rotate_x)
    # 创建旋转矩阵
    matrix = np.array([
        [c(alpha) * c(beta), c(alpha) * s(beta) * s(gamma) - s(alpha) * c(gamma),
         c(alpha) * s(beta) * c(gamma) + s(alpha) * s(gamma)],
        [s(alpha) * c(beta), s(alpha) * s(beta) * s(gamma) + c(alpha) * c(gamma),
         s(alpha) * s(beta) * c(gamma) - c(alpha) * s(gamma)],
        [-s(beta), c(beta) * s(gamma), c(beta) * c(gamma)]
    ])

    return matrix

