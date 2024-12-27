## 自定义资产

该项目包含可以嵌入 Carla 项目中的自定义资产，比如：车辆、行人等，为项目做出贡献前请查看 [贡献指南](https://github.com/OpenHUTB/.github/blob/master/CONTRIBUTING.md) 。

### 使用
直接覆盖到carla源代码编译版的目录下，然后运行脚本进行测试：
```shell
# 车辆
python manual_control.py --filter vehicle.BYD.seal
# 行人
python manual_control.py --filter walker.pedestrian.0051
```

### 说明

该仓库的资产兼容Carla的`ue4-dev`分支的最新代码。

### 参考

- [添加新车](https://openhutb.github.io/carla_doc/tuto_A_add_vehicle/)
- [内容创作 - 车辆](https://openhutb.github.io/carla_doc/tuto_content_authoring_vehicles/)
- [内容创作 - 行人](https://openhutb.github.io/carla_doc/tuto_content_authoring_pedestrians/)

