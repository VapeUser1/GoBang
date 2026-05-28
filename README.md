# AI五子棋项目

一个基于 Python + Tkinter 实现的 AI 五子棋项目。  
支持图形化棋盘、人机对战、AI 自动落子与胜负判定。

---

## Features

- 图形化五子棋界面（Tkinter）
- 人类玩家 vs AI
- 自动胜负检测
- 支持不同等级的 AI 策略
- 棋盘实时刷新
- 回合显示与音效支持

---

## Preview

### 游戏界面

![image](https://github.com/VapeUser1/GoBang/blob/master/icon.png)

---

## Project Structure

AI-Gobang/
│
├── pycode        # 代码文件

├── build.bat     # 启动命令
├── start.vbs      # 一键启动
└── README.md

---

## Requirement

- Python 3.10+

- tkinter
  
  如果 tkinter 缺失：
  
  #Windows
  
  通常 Python 自带 tkinter。
  
  #Ubuntu / Debian
  
  ```
  sudo apt install python3-tk
  ```

---

## Quick Start

启动start.vbs

---

## AI Strategy

当前 AI 使用：

- 局部评分搜索
- 威胁检测
- 决策树搜索

评估内容包括：

- 连五
- 活四
- 冲四
- 活三
- 双三

后续计划加入：

- Minimax
- Alpha-Beta Pruning

---

## Future Work

- 悔棋功能

- 多线程 AI 思考

- 网络联机

- 棋谱保存

- 更强 AI

- 深度学习模型支持

---

## Author

https://github.com/VapeUser1/GoBang
