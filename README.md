# ffmpeg_converter

基于 FFmpeg 的视频编码格式转换器，使用 Python 调用。

Python 版本: 3.7

### 使用方法
终端中逐条运行以下命令下载FFmpeg

```
# 下载 FFmpeg 最新发行版
wget --trust-server-names https://evermeet.cx/ffmpeg/getrelease/dmg

# 将 DMG 挂载在 /Volumes 下
hdiutil attach ffmpeg*.dmg

# 复制 ffmpeg 到 ffmpeg文件夹下
cp -rf /Volumes/FFmpeg*/ffmpeg ~/ffmpeg/

# 推出
hdiutil detach /Volumes/FFmpeg*
```

设置文件输出路径

**1. Python 命令行运行**

Terminal 中运行 `python ffmpeg_converter.py` 即可(其他环境下可能会报错)。

**2. 编译运行**

直接运行 Repository 目录下 dist 中的可执行程序即可。

默认 ffmpeg 存放位置: ~/ffmpeg/

默认文件输出路径: ~/Downloads/ffmpeg_output/

**由于 Shell 的限制，目前不支持文件名中包含空格的文件**

### 编译方法
Repository 存放路径: /Users/tianjierong/Documents/GitHub/

安装 pyinstaller

```
pip install pyinstaller
```

终端执行

```
pyinstaller --onefile --clean /Users/tianjierong/Documents/GitHub/FFmpeg_converter/ffmpeg_converter.py
```

### 更新日志
#### 2019.02.22 
在 Terminal 实现基本功能，可设定转换参数有：编码器，编码速度，封装格式，输出文件名。

未进行界面优化和注释。

#### 2018.02.23
增加初始界面，版本号v1.0。

改进交互界面，增加默认转换参数。（编码器: libx264, 编码速度: ultrafast, 封装格式: mp4）

转换前显示源文件信息。

添加部分注释。

新增可在全局变量中修改 ffmpeg 路径和文件输出路径。

使用 pyinstaller 进行封装。

添加 ffmpeg 下载方式。

