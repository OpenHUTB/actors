# 将该项目的资产部署到carla源代码编译的工程中
# 运行示例：python deploy.py -r C:/workspace/carla/Unreal
# 参考：https://support.i-search.com.cn/article/1548747150529
import argparse
import hashlib
import os

import shutil

import glob


# 通过校验MD5 判断B内的文件与A 不同
# 参考：https://www.cnblogs.com/xiaodekaixin/p/11203857.html
def get_MD5(file_path):
    with open(file_path, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    return file_md5


def copy_directory(path, out):
    '''
    :param path:  文件输出源路径
    :param out:  文件复制目标路径
    :return:
    '''
    # 判断目标文件夹是否存在，如不存在，则创建。
    if not os.path.isdir(out):
        os.makedirs(out)
    # os.listdir(path) 获取源目录下的文件列表
    for files in os.listdir(path):
        name = os.path.join(path, files)
        print('name', name)
        back_name = os.path.join(out, files)
        print('back_name', back_name)
        # 如果源文件是文件
        if os.path.isfile(name):
            print('源文件是否存在', os.path.isfile(name))
            # 如果目标文件夹中文件存在
            if os.path.isfile(back_name):
                print('目标文件夹中文件存在', os.path.isfile(back_name))
                # 通过 MD5值来判断文件是否一致：一致，不做操作；不一致，覆盖。
                if get_MD5(name) != get_MD5(back_name):
                    print('MD5值', get_MD5(name))
                    shutil.copy(name, back_name)
            # 如果目标文件夹中文件不存在，复制
            else:
                print('目标文件夹中文件不存在', back_name)
                shutil.copy(name, back_name)
        # 如果源文件是一个目录
        else:
            # 如果目标目录不存在
            if not os.path.isdir(back_name):
                # 创建目标文件目录
                os.makedirs(back_name)
            # 递归执行
            copy_directory(name, back_name)


def main():
    argparser = argparse.ArgumentParser(
        description='CARLA Assert Deploy Configuration')
    argparser.add_argument(
            '-r', '--root',
            help='The carla root directory')
    # carla的源代码目录
    args = argparser.parse_args()
    print(args.root)

    # 使用方法
    source_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Unreal')
    # destination_dir = 'C:/buf/Unreal'
    destination_dir = args.root

    copy_directory(source_dir, destination_dir)


if __name__ == '__main__':
    main()
