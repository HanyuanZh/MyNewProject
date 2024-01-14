# 导入必要的模块
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
liver_model = VTKSurfaceModel("C:\\Users\\hanyu\\Desktop\\liver.vtk", colour=[1.0, 0.0, 0.0], visibility=True, opacity=1.0, pickable=False)
import vtk

# 创建一个渲染器、渲染窗口和交互器
renderer = vtk.vtkRenderer()  # 创建一个渲染器，用于渲染可视化场景
renderWindow = vtk.vtkRenderWindow()  # 创建一个渲染窗口，用于显示渲染结果
renderWindow.AddRenderer(renderer)  # 将渲染器添加到渲染窗口
renderWindowInteractor = vtk.vtkRenderWindowInteractor()  # 创建一个渲染窗口交互器
renderWindowInteractor.SetRenderWindow(renderWindow)  # 将渲染窗口交互器与渲染窗口关联

# 将要显示的模型添加到场景中
renderer.AddActor(liver_model.actor)  # 将肝脏模型添加到渲染器中

# 渲染并交互
renderWindow.Render()  # 执行渲染
renderWindowInteractor.Start()  # 启动渲染窗口的交互操作循环
