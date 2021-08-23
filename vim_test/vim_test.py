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
# 下翻一页  Ctrl + f  命令模式

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
from vim_test.vim_command import VimCommand


class VimTest(object):
    """
    vim test class

    """

    def __init__(self):
        self._command_list = []

    def add_command(self, vim_command: object):
        self._command_list.append(vim_command)


if __name__ == '__main__':

    """
    
    # 文档操作
    # 显示行号  :set nu  末行模式
    # 保存并退出  :wq  末行模式
    # 保存并退出  :x  末行模式
    """
    vim_com_001 = VimCommand(keys=":set nu",model="末行模式",detail="显示行号",category="文档操作")
    vim_com_001 = VimCommand(keys=":set nu",model="末行模式",detail="显示行号",category="文档操作")
    vim_com_001 = VimCommand(keys=":set nu",model="末行模式",detail="显示行号",category="文档操作")
    vim_com_001 = VimCommand(keys=":set nu",model="末行模式",detail="显示行号",category="文档操作")

    pass
