# -*- coding: utf-8 -*-

import copy
from typing import List

from flowlauncher import FlowLauncher

from plugin.templates import *
from plugin.devtoys import *


class Main(FlowLauncher):
    messages_queue = []

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        self.messages_queue.append(message)

    def sendActionMess(self, title: str, subtitle: str, icopath: str, method: str, value: List):
        # information
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle
        if icopath != "":
            message["IcoPath"] = icopath

        # action
        action = copy.deepcopy(ACTION_TEMPLATE)
        action["JsonRPCAction"]["method"] = method
        action["JsonRPCAction"]["parameters"] = value
        message.update(action)

        self.messages_queue.append(message)

    def query(self, param: str) -> List[dict]:
        q = param.strip().lower()
        for tool in DEVTOYS_TOOLS:
            key = tool["tool"]
            name = tool["name"]
            icon = tool["icon"] if "icon" in tool else ""
            if q in key.lower() or q in name.lower():
                self.sendActionMess(name, key, icon, "startDevtoysTool", [key])
        return self.messages_queue

    def startDevtoysTool(self, tool):
        startTool(tool)
