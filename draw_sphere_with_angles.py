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



# 创建点集，考虑角度限制
points = []
for x in np.arange(-radius, radius + 1, step):
    for y in np.arange(-radius, radius + 1, step):
        for z in np.arange(-radius, radius + 1, step):
            r = np.sqrt(x**2 + y**2 + z**2)
            if r > 0 and r <= radius:
                theta = np.arccos(z / r)  # 方位角，避免除以零
                phi = np.arctan2(y, x)    # 天顶角
                if theta_min <= theta <= theta_max and ((phi_min1 <= phi <= phi_max1) or (phi_min2 <= phi <= phi_max2)):
                    points.append([x, y, z])

# 将点转换为numpy数组并平移到网格中心
points = np.array(points, dtype=np.float32) + mesh_center  # 显式转换为float32以避免警告

# 创建PyVista PolyData对象，指定force_float=False
point_polydata = pv.PolyData(points, force_float=False)

plotter.add_mesh(point_polydata, color='green', point_size=5)

# 设置视角为XYZ平面正视 (您可以根据需要选择view_xy(), view_xz(), 或 view_yz())
plotter.view_xy()
#print(point_polydata.points-mesh_center)
# 显示Plotter窗口
plotter.show()
