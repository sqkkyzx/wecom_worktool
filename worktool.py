import requests


class Worktool(object):
    class FileType:
        IMAGE = 'image'
        AUDIO = 'audio'
        VIDEO = 'video'
        OTHERS = '*'

    def __init__(self, robotid):
        self.robotid: str = robotid
        self.action: list = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        requests.post(
            url="https://api.worktool.ymdyes.cn/wework/sendRawMessage",
            params={"robotId": self.robotid},
            json={
                "socketType": 2,
                "list": self.action
            }
        )

    def send_text(self, receiver: list, msg: str, at_list: list = None):
        if at_list:
            self.action.append(
                {
                    "type": 203,
                    "titleList": receiver,
                    "receivedContent": msg,
                    "atList": at_list
                }
            )
        else:
            self.action.append(
                {
                    "type": 203,
                    "titleList": receiver,
                    "receivedContent": msg
                }
            )

    def send_file(self, receiver: list, object_name: str, object_url: str, file_type: FileType, extra_msg: str = ""):
        self.action.append(
            {
                "type": 218,
                "titleList": receiver,
                "objectName": object_name,
                "fileUrl": object_url,
                "fileType": file_type,
                "extraText": extra_msg
            }
        )