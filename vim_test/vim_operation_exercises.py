# vim 所有命令 [{},{},{}]
# https://blog.csdn.net/weixin_37657720/article/details/80645991

# 文档操作
# 显示行号  :set nu  末行模式
# 保存并退出  :wq  末行模式
# 保存并退出  :x  末行模式

# 光标移动
# 光标左移n列  n_h  命令模式
# 光标右移n列  n_l  命令模式
# 光标上移n行  n_k  命令模式
# 光标下移n行  n_j  命令模式
# 光标移动到n行  n_G  命令模式
# 光标移动到首行  gg  命令模式
# 光标移动到结尾行  G  命令模式

# 翻页
# 上翻一页  Ctrl + b  命令模式
# 下翻一页  Ctrl + f  命令模式
# 到文件n%的位置  n_%  命令模式

# 复制粘贴
# 复制整行  yy or Y  命令模式
# 剪切n行  n_dd  命令模式
# 粘贴  p  命令模式

# 查找替换
# 查找  /something  命令模式
# 查找上一个  N  命令模式
# 查找下一个  n  命令模式
# 用new替换当前行第一个old  :s/old/new  末行模式
# 用new替换当前行所有的old  :s/old/new/g  末行模式
# 用new替换文件n1行到n2行所有的old  :n1,n2s/old/new/g  末行模式
# 用new替换文件中所有的old  :%s/old/new/g  末行模式
# 在每一行的行首插入xxx  :%s/^/xxx/g  末行模式

# 撤销恢复
# 撤销  u  命令模式
# 恢复  Ctrl + r  命令模式


"""
构建 command 对象
    directive
    detail
    means
    category

构建 command_list 列表

随机 n 个 command 对象
    将对象的 detail 输出到文件
    分割
    将对象的 detail 和 directive 输出到文件

"""
import random

from vim_test.vim_command import VimCommand


class VimOperationExercises(object):
    """
    vim test class

    """

    def __init__(self):
        self._command_list = []

    def add_command(self, vim_command: object):
        self._command_list.append(vim_command)

    def random_vim_command(self, num: int, category: int = -1):
        """
        随机 n 个 command 对象

        分类:

            -1 不分类
            0 文档操作
            1 光标移动
            2 翻页
            3 复制粘贴
            4 查找替换
            5 撤销恢复
        :param category: 分类
        :param num: 输出个数
        :return:
        """
        category_list = ["文档操作", "光标移动", "翻页", "复制粘贴", "查找替换", "撤销恢复"]

        # 获得 command_list_ , 用于后续处理
        command_list_ = self._command_list

        """
        处理分类
        """
        if category != -1:
            command_list_ = []

            # 获取分类
            category_ = category_list[category]

            for obj_ in self._command_list:  # type:VimCommand

                # 判断分类是否相等
                if obj_.category == category_:
                    command_list_.append(obj_)

        # 调整 num
        if num > len(command_list_):
            num = len(command_list_)

        """
        随机 n 个 command 对象
        """
        # 存储结果
        result_command = []

        # 随机 n 个 command 对象
        for index_ in range(num):
            # 随机索引
            rand_int = random.randint(0, len(command_list_)-1)

            # 获取索引对应的对象
            command_obj = command_list_[:][rand_int]

            # 加入结果集
            result_command.append(command_obj)

            # 从数据源移除对象
            command_list_.remove(command_obj)

        """
        将 result_command 写入文件 
        
        描述
        分割
        描述
        命令  
        """

        with open("OperationExercises.md", "w", encoding="utf8") as wf:

            # 操作行数
            command_line = random.randint(1, 20)

            # 写入描述
            for command_obj in result_command:  # type:VimCommand

                if "n_" in command_obj.keys:
                    command_obj.keys = command_obj.keys.replace("n_", str(command_line))
                    command_obj.detail = command_obj.detail.replace("n", str(command_line))

                wf.write("#" * 3 + " " + command_obj.detail)
                wf.write("\n")

            # 写入分割
            wf.write("\n" * 20)

            wf.write("`" * 3 + " bash\n")

            # 写入 描述 & 命令
            for command_obj in result_command:  # type:VimCommand
                wf.write("# " + command_obj.detail)
                wf.write("\n")
                wf.write(command_obj.keys)
                wf.write("\n")

            wf.write("`" * 3 + " \n")


if __name__ == '__main__':
    # 文档操作,显示行号,:set nu,末行模式

    # 读取文件,构建 command_list 列表

    vim_test = VimOperationExercises()

    with open("./vim_command.text", "r", encoding="utf8") as rf:
        while True:
            read_line = rf.readline().strip()
            if len(read_line) <= 0:
                break
            vim_command = VimCommand(*(read_line.split(";;")))
            vim_test.add_command(vim_command)

    vim_test.random_vim_command(15)
