# this synchronous program takes 20 seconds to run
import time

def message():
    print("hello")
    time.sleep(2)
    print("world")

def main():
    for i in range(10):
        message()

start = time.time()
main()
end = time.time()
print(end - start)