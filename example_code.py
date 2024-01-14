# 导入必要的模块
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgeryvtk.camera.vtk_camera_model import compute_projection_matrix, set_camera_intrinsics, set_camera_pose
import vtk
import numpy as np
from add_point import add_point
from generate_rotation_matrix import create_rotation_matrix as crm
from combine_single_matrix import combine_single_matrix as csm
from sksurgeryvtk.widgets.vtk_overlay_window import VTKOverlayWindow

# 创建肝脏模型实例
liver_model = VTKSurfaceModel("C:\\Users\\hanyu\\Desktop\\liver.vtk", colour=[1.0, 0.0, 0.0], visibility=True, opacity=1.0, pickable=False)

# 创建一个渲染器、渲染窗口和交互器
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# 创建并配置摄像机
camera = vtk.vtkCamera()

# 计算肝脏模型的质心
bounds = liver_model.actor.GetBounds()
centroid = [(bounds[1] + bounds[0]) / 2, (bounds[3] + bounds[2]) / 2, (bounds[5] + bounds[4]) / 2]

# 移动肝脏模型使质心位于原点
transform = vtk.vtkTransform()
transform.Translate(-centroid[0], -centroid[1], -centroid[2])
liver_model.actor.SetUserTransform(transform)

# 创建坐标轴
axes = vtk.vtkAxesActor()
axes.SetTotalLength(100, 100, 100)
axes.SetPosition(-centroid[0], -centroid[1], -centroid[2])

# 将坐标轴和肝脏模型添加到渲染器
renderer.AddActor(liver_model.actor)
renderer.AddActor(axes)

# 设置摄像机参数
width, height = 1920, 1920
f_x, f_y = 1000, 1000
c_x, c_y = width / 2, height / 2
near, far = 0.1, 1000

# 计算投影矩阵
projection_matrix = compute_projection_matrix(width, height, f_x, f_y, c_x, c_y, near, far)

# 设置摄像机内参和投影矩阵
set_camera_intrinsics(renderer, camera, width, height, f_x, f_y, c_x, c_y, near, far)
camera.SetExplicitProjectionTransformMatrix(projection_matrix)

# 定义摄像机到世界坐标系的变换矩阵
vector = [-20, -50, -160]
rotation_matrix = crm(90, 0, 0)
matrix = csm(rotation_matrix, vector)
transform_matrix = [
    matrix[0,0], matrix[0,1], matrix[0,2], matrix[0,3],  # 第一行: ...
    matrix[1,0], matrix[1,1], matrix[1,2], matrix[1,3],  # 第二行: ...
    matrix[2,0], matrix[2,1], matrix[2,2], matrix[2,3],  # 第三行: ...
    matrix[3,0], matrix[3,1], matrix[3,2], matrix[3,3]   # 第四行: 固定值
]

# 将列表转换为 vtkMatrix4x4 对象
vtk_matrix = vtk.vtkMatrix4x4()
for i in range(4):
    for j in range(4):
        vtk_matrix.SetElement(i, j, transform_matrix[i * 4 + j])

# 设置摄像机姿态
set_camera_pose(camera, vtk_matrix)
renderer.SetActiveCamera(camera)

# 在这里调用 add_point 函数来添加点
# 例如，添加一个位于质心的红色点
add_point(renderer, [0.0,-160.0,0.0], color=[1, 1, 1], radius=10)


# 渲染并启动交互循环
renderWindow.Render()
renderWindowInteractor.Start()
