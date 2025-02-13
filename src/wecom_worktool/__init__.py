from typing import List

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
        self.push_action()

    def push_action(self):
        return requests.post(
            url="https://api.worktool.ymdyes.cn/wework/sendRawMessage",
            params={"robotId": self.robotid},
            json={
                "socketType": 2,
                "list": self.action
            }
        )

    def clear_action(self):
        return requests.post(
            url="https://api.worktool.ymdyes.cn/wework/sendRawMessage",
            params={"robotId": self.robotid},
            json={
                "socketType": 2,
                "list": {"type": 304}
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

    def group_member_add(self, group_name: str, members: list, show_history: bool):
        self.action.append(
            {
                "type": 207,
                "groupName": group_name,
                "selectList": members,
                "showMessageHistory": show_history
            }
        )

    def group_member_remove(self, group_name: str, members: list):
        self.action.append(
            {
                "type": 207,
                "groupName": group_name,
                "removeList": members
            }
        )

    def group_member_remark(self, group_name: str, nickname: str, mark_name: str):
        self.action.append(
            {
                "type": 225,
                "groupName": group_name,
                "friend": {
                    "name": nickname,
                    "markName": mark_name
                }
            }
        )

    def group_notice(self, group_name: str, notice: str):
        self.action.append(
            {
                "type": 207,
                "groupName": group_name,
                "newGroupAnnouncement": notice
            }
        )

    def group_rename(self, group_name: str, new_group_name: str):
        self.action.append(
            {
                "type": 207,
                "groupName": group_name,
                "newGroupName": new_group_name
            }
        )

    def group_remark(self, group_name: str, remark: str):
        self.action.append(
            {
                "type": 207,
                "groupName": group_name,
                "groupRemark": remark
            }
        )

    def group_disband(self, group_name: str):
        self.action.append(
            {
                "type": 219,
                "groupName": group_name
            }
        )

    def todo(self, content: str, nickname: List[str] = None, group_name: List[str] = None):
        if group_name or nickname:
            title_list = []
            if group_name:
                title_list.extend(group_name)
            if nickname:
                title_list.extend(nickname)
            self.action.append(
                {
                    "type": 221,
                    "titleList": title_list,
                    "receivedContent": content
                }
            )

    def friend_remove(self, nickname: str):
        self.action.append(
            {
                "type": 234,
                "friend": {
                    "name": nickname
                }
            }
        )

    def friend_add(self, phone: str, mark_name: str = None, mark_extra: str = None, tags: List[str] = None, msg: str = None):
        self.action.append(
            {
                "type": 213,
                "friend": {
                    "phone": phone,
                    "markName": mark_name,
                    "markExtra": mark_extra,
                    "tagList": tags,
                    "leavingMsg": msg
                }
            }
        )