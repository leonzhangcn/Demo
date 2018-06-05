
#在代码变动的前提下增加额外功能
# def debug():
#     import inspect
#     caller_name=inspect.stack()[1][3]
#     print("[DEBUG]:enter{}()".format(caller_name))
#
# def say_hello():
#     debug()
#     print("hello!")
#
# def say_goodbye():
#     debug()
#     print("hello!")


#在代码没有变动的前提下增加额外功能
# def debug(func):
#     def wrapper():
#         print("[DEBUG]:enter{}()".format(func.__name__))
#         return func()
#     return wrapper
#
# def say_hello():
#     print("hello!")
#
# def say_goodbye():
#     print("hello!")

#装饰器：在代码没有变动的前提下增加额外功能，但没有参数
# def debug(func):
#     def wrapper():
#         print("[DEBUG]:enter{}()".format(func.__name__))
#         return func()
#     return wrapper
#
# @debug
# def say_hello():
#     print("hello!")
#
# @debug
# def say_goodbye():
#     print("hello!")

#装饰器：在代码没有变动的前提下增加额外功能，带有参数

def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]:enter{}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@debug
def say(something0,something1):
    print("hello {0},i am {1}!".format(something0,something1))

if __name__ =="__main__":
   say("ZhangLiang","WangJin")