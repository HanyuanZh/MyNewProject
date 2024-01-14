import vtk
def add_point(renderer, point, color=[1, 0, 0], radius=1):
    """
    在 VTK 渲染器中添加一个表示点的小球体。

    :param renderer: VTK 渲染器
    :param point: 点的坐标，格式为 [x, y, z]
    :param color: 小球体的颜色，格式为 [r, g, b]
    :param radius: 小球体的半径
    """
    # 创建一个球体源
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(*point)
    sphereSource.SetRadius(radius)

    # 创建一个映射器
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())

    # 创建一个 actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color)

    # 将 actor 添加到渲染器
    renderer.AddActor(actor)