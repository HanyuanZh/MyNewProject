import numpy as np
import pyvista as pv

# 替换为您的VTK文件路径
vtk_file_path = 'C:/Users/hanyu/Desktop/liver.vtk'

# 加载VTK文件
mesh = pv.read(vtk_file_path)

# 创建一个PyVista Plotter实例
plotter = pv.Plotter()
plotter.add_mesh(mesh)

# 获取网格的中心
mesh_center = mesh.center

# 定义球体的半径和步长
radius = 150
# 定义步长
step = 10
theta_min, theta_max = np.pi / 2, np.pi
phi_min1, phi_max1 = 0.65*np.pi, np.pi
phi_min2, phi_max2 = -np.pi,0

x_vals = np.arange(-110, 101, step)
y_vals = np.arange(-80, 81, step)
z_vals = np.arange(-200, -20, step)

# 创建点集，考虑角度限制
points = []
for x in x_vals:
    for y in y_vals:
        for z in z_vals:
            r = np.sqrt(x**2 + y**2 + z**2)
            if r > 0 and r <= radius:
                theta = np.arccos(z / r)  # 方位角，避免除以零
                phi = np.arctan2(y, x)    # 天顶角
                if theta_min <= theta <= theta_max and ((phi_min1 <= phi <= phi_max1) or (phi_min2 <= phi <= phi_max2)):
                    points.append([x, y, z])

# 将点转换为numpy数组并平移到网格中心
points = np.array(points, dtype=np.float32) + mesh_center  # 显式转换为float32以避免警告

# 获取肝脏图像的顶点
liver_points = mesh.points

# 定义一个阈值来判断点是否在肝脏内部
threshold = 10.0

# 初始化一个空列表来存储不重合的点
non_overlapping_points = []

# 循环检查每个点
for point in points:
    # 计算点到所有肝脏顶点的距离
    distances = np.linalg.norm(liver_points - point, axis=1)
    # 如果所有距离都大于阈值，则认为该点不在肝脏内部
    if np.all(distances > threshold):
        non_overlapping_points.append(point)

# 将不重合的点转换为numpy数组
non_overlapping_points = np.array(non_overlapping_points)

# 创建一个PyVista PolyData对象来表示这些不重合的点
non_overlapping_point_polydata = pv.PolyData(non_overlapping_points)

# 将不重合的点添加到绘图工具中
plotter.add_mesh(non_overlapping_point_polydata, color='green', point_size=5)

# 设置视角为XYZ平面正视
plotter.view_xy()
print(len(non_overlapping_points))
# 显示Plotter窗口
plotter.show()
