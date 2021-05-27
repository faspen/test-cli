import sys
from .classmodule import MyClass
from .funcmodule import my_function

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]


def main():
    if "--about" in opts:
        print("Print stuff, I guess")
        return
    if "--tell-a-joke" in opts:
        print("Why did the chicken cross the road?\nTo get to the other side!")
        return
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_function('hello world')

    my_object = MyClass('Finn')
    my_object.say_name()

if __name__ == '__main__':
    main()
