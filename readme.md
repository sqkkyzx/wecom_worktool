这只是 [WorkTool](https://worktool.ymdyes.cn/) API 的简单封装，以便于能够在各种程序中引入复用。

可以参考 [WorkTool的API文档](https://worktool.apifox.cn/)，但部分功能尚未封装。


# 已封装的功能

- [x] 发送文本
- [x] 发送图片/文件/音频/视频/其他


# 使用示例

安装模块

`pip install wecom_worktool`

```python
import worktool

with worktool.Worktool("your_robot_id") as bot:
        bot.send_file(
            ["群1", "好友1"],
            "文件名.jpg",
            "https://your_image_url.jpg",
            bot.FileType.IMAGE
        )
        bot.send_text(
            ["好友1"],
            "Hello world!"
        )
        bot.send_text(
            ["群1"],
            "Hello world!",
            ["@所有人"]
        )

```