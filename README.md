# pairwise-baseball-pitch-strikezone

## 领域

游戏、图形与多媒体

## 主题

棒球投球缝线旋转与好球带判定

## 说明

缝线旋转解缠、出手时刻回溯、好球带随打者重建。

初始状态下 `game/pitch_zone.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
