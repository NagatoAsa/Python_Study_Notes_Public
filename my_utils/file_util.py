def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except FileNotFoundError:
        print("文件不存在")
    else:
        fr = f.read()
        print(fr)
    finally:
        if f:  # None可以当False使用，一旦变量f中有内容，就会输出为True
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
