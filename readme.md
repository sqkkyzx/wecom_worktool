这只是 [WorkTool](https://worktool.ymdyes.cn/) API 的简单封装，以便于能够在各种程序中引入复用。

可以参考 [WorkTool的API文档](https://worktool.apifox.cn/)，但部分功能尚未封装。


# 已封装的功能

- [x] 发送文本
- [x] 发送图片/文件/音频/视频/其他
- [x] 发送腾讯文档/收集表
- [x] 发送微盘图片
- [x] 添加群成员
- [x] 移除群成员
- [x] 修改群名
- [x] 修改公告
- [x] 修改群备注
- [x] 解散群
- [x] 添加待办
- [x] 添加好友（从手机号）
- [x] 添加好友（从群）
- [x] 移除好友
- [x] 修改好友


# 使用示例

安装模块

`pip install wecom_worktool`

```python
from wecom_worktool import Worktool

with Worktool("your_robot_id") as bot:
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