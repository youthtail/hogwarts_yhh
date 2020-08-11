# 文件操作3步曲 1、打开 2、操作 3、关闭
# open('data') 是一个io对象，默认'r' read,'t' text mode
print(open('data'))
# output: <_io.TextIOWrapper name='data' mode='r' encoding='cp936'>
f = open('data')
print(f.readlines())
# output: ['1,\n', '2,\n', '3'],是一个列表
f.close()

# 使用这种写法，不需要再手动关闭文件，他会在每次操作后自动关闭
with open('data') as f:
    print(f.readlines())
# 读取图片，使用二进制’b‘
f = open('iImage.png', 'rb')
# print(f.read())



