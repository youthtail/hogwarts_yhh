# python 自带日志模块，初始化之后就可以用了，注意指定输出日志级别
import _thread
import logging
import time

logging.basicConfig(level=logging.INFO)

# loops = [2, 4]
#
#
# def loop0():
#     logging.info('start loop0 at' + time.ctime())
#     time.sleep(2)
#     logging.info(f'end loop0 at {time.ctime()}')
#
#
# def loop1():
#     logging.info(f'start loop1 at {time.ctime()}')
#     time.sleep(3)
#     logging.info(f'end loop1 at {time.ctime()}')
#
#
# def main():
#     logging.info(f'start main thread at {time.ctime()}')
#     # 开辟新的线程，loop0、loop1和主线程一起执行
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, (), {})
#     # _thread规定：当主线程退出，所有的子线程就会kill
#     #time.sleep(1)
#     logging.info(f'end main fun at {time.ctime()}')
#
#
# main()
import threading
class myThread(threading.Thread): # 继承threading module ,Thread类
    def __init__(self,threadID,name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        


