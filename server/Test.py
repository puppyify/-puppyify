

import os

# 相对路径
relative_path = 'path/to/file.txt'

# 获取当前运行程序的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将相对路径转换为绝对路径
absolute_path = os.path.join(current_dir, relative_path)

print(f"相对路径 '{relative_path}' 的绝对路径是 '{absolute_path}'")


if __name__ == '__main__':

    ...