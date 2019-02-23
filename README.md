# ffmpeg_converter

基于 FFmpeg 的视频编码格式转换器，使用 Python 调用。

### 使用方法
下载[FFmpeg](https://evermeet.cx/ffmpeg/ffmpeg-4.1.1.dmg)(链接版本v4.1.1)，下载完成后解压文件 **ffmpeg** 至 Home 文件夹下 ffmpeg 子目录中。在 Downloads 下新建 ffmpeg_output 文件夹。Terminal 中运行 `python ffmpeg_converter.py` 即可(其他环境下可能会报错)。

**由于 Shell 的限制，目前不支持文件名中包含空格的文件**

### 更新日志
#### 2019.02.22 
在 Terminal 实现基本功能，可设定转换参数有：编码器，编码速度，封装格式，输出文件名。

未进行界面优化和注释。

#### 2018.02.23
改进交互界面，增加默认转换参数。（编码器: libx264, 编码速度: ultrafast, 封装格式: mp4）

转换前显示源文件信息。

添加部分注释。