import request_code
from threading import Thread

url_base = r'https://lab.je-clark.com'

if __name__ == "__main__":
        workers = 10
        for x in range(100):
                thread_list=[]
                for i in range(workers):
                        thread_list.append(Thread(target=request_code.quick, args=(url_base,)))

                for t in thread_list:
                        t.start()

                for t in thread_list:
                        t.join()