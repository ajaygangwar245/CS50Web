def announce(f):
    def wrapper():
        print("function f is about to start")
        f()
        print("function f is executed succesfully")
    return wrapper
    
@announce
def hello():
    print("Hello, world!")

hello()