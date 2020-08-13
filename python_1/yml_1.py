import yaml

# 传入文件路径，open() open a file and return stream
# r-read,w-write,a-append
with open('yamldata', mode='a+') as f:
    # w+ :清空文件在写入；r+:读和写
    # load() parse stream to object
    # Loader=yaml.FullLoader,能够过滤掉warning
    f.seek(0)
    print(yaml.load(f, Loader=yaml.FullLoader))
    a = ['lalalal']
    # dump() parse object to yaml stream
    yaml.dump(a, f)
    f.seek(0)
    print(yaml.load(f, Loader=yaml.FullLoader))


