"""

构建 command 对象
    keys
    model
    detail
    category

"""


class VimCommand(object):
    """
    Vim command class

    """

    def __init__(self, category, detail, keys, model):
        """

        :param keys: 指令/命令
        :param model: 模式
        :param detail: 描述
        :param category: 分类
        """
        self.keys = keys
        self.model = model
        self.detail = detail
        self.category = category
