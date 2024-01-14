# 导入必要的模块
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgeryvtk.camera.vtk_camera_model import compute_projection_matrix, set_camera_intrinsics, set_camera_pose
import vtk
import numpy as np
from add_point import add_point
from generate_rotation_matrix import create_rotation_matrix as crm
from combine_single_matrix import combine_single_matrix as csm

vector = [0, 50, -100]
class RotationSliderCallback:
    def __init__(self, camera, liver_model, renderer):
        self.camera = camera
        self.liver_model = liver_model
        self.renderer = renderer
        self.rotation_x = 0  # 初始化x轴旋转角度

    def execute(self, caller, event):
        sliderRep = caller.GetRepresentation()
        new_rotation_x = sliderRep.GetValue()
        delta_rotation_x = new_rotation_x - self.rotation_x

        # 重新计算旋转矩阵
        rotation_matrix_3x3 = crm(delta_rotation_x, 0, 0)
        vtk_matrix_4x4 = to_vtk_transform_matrix(rotation_matrix_3x3)

        # 将矩阵转换为VTK可以接受的格式
        flat_matrix = vtk_matrix_4x4.flatten().tolist()
        # 创建一个新的vtkTransform
        transform = vtk.vtkTransform()
        transform.SetMatrix(flat_matrix)
        self.liver_model.actor.SetUserTransform(transform)
        # 重新渲染
        self.renderer.Render()
        # 更新角度
        self.rotation_x = new_rotation_x

    def to_vtk_transform_matrix(rotation_matrix_3x3):
        # 创建一个4x4的单位矩阵
        transform_matrix_4x4 = np.eye(4)
        # 将3x3旋转矩阵放入4x4矩阵的左上角
        transform_matrix_4x4[:3, :3] = rotation_matrix_3x3
        return transform_matrix_4x4


# 创建滑块代表
sliderRep = vtk.vtkSliderRepresentation2D()
sliderRep.SetMinimumValue(0.0)  # 设置最小值
sliderRep.SetMaximumValue(180.0)  # 设置最大值
sliderRep.SetValue(90.0)  # 设置初始值
sliderRep.SetTitleText("Camera angle")  # 设置标题
# 设置滑块位置
sliderRep.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay()
sliderRep.GetPoint1Coordinate().SetValue(0.1, 0.1)
sliderRep.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay()
sliderRep.GetPoint2Coordinate().SetValue(0.4, 0.1)
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

rotation_matrix = crm(0, 0, 0)
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
# 创建滑块小部件
sliderWidget = vtk.vtkSliderWidget()
sliderWidget.SetInteractor(renderWindowInteractor)
sliderWidget.SetRepresentation(sliderRep)
sliderWidget.KeyPressActivationOff()
# 设置滑块的回调
# 创建滑块的回调
rotation_callback = RotationSliderCallback(camera, liver_model, renderer)
sliderWidget.AddObserver("InteractionEvent", rotation_callback.execute)

# 激活滑块
sliderWidget.SetEnabled(True)
# 在这里调用 add_point 函数来添加点
# 例如，添加一个位于质心的红色点
add_point(renderer, [0.0,-160.0,0.0], color=[1, 1, 1], radius=10)
print(centroid)
# 渲染并启动交互循环
renderWindow.Render()
renderWindowInteractor.Start()

