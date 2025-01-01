## 自定义资产

该项目包含可以嵌入 Carla 项目中的自定义资产，比如：车辆、行人等，为项目做出贡献前请查看 [贡献指南](https://github.com/OpenHUTB/.github/blob/master/CONTRIBUTING.md) 。

### 使用
运行`deploy.py`直接覆盖到carla源代码编译版的目录下（注意运行时需要关闭虚幻编辑器，否则`VehicleFactory.uasset`等文件被占用，导致硬链接可能更新不了），在虚幻编辑器中运行场景后运行 [manual_control.py](https://github.com/OpenHUTB/carla_doc/blob/master/src/examples/manual_control.py) 脚本进行测试：
```shell
# 车辆
python manual_control.py --filter vehicle.BYD.seal
# 行人
python manual_control.py --filter walker.pedestrian.0051
```
如果运行行人报找不到行人蓝图的错误，到 [WalkerFactory](https://github.com/OpenHUTB/actors/blob/master/Unreal/CarlaUE4/Content/Carla/Blueprints/Walkers/WalkerFactory.uasset) 蓝图中，找到编译报错的地方，根据错误跳转到节点`Wheelchair Add`节点中，然后删除该节点即可重新正常运行。

### 说明

该仓库的资产兼容Carla的`ue4-dev`分支的最新代码。

### 参考

- [添加新车](https://openhutb.github.io/carla_doc/tuto_A_add_vehicle/)
- [内容创作 - 车辆](https://openhutb.github.io/carla_doc/tuto_content_authoring_vehicles/)
- [内容创作 - 行人](https://openhutb.github.io/carla_doc/tuto_content_authoring_pedestrians/)

