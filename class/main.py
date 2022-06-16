
import types


class Strip:
    a=3

    def __init__(self,arg):
        self.a=arg

    def setter(self,arg):
        self.a = arg

    def getter(self,arg):
        return self.a


async def corout():
    pass


def main():
    p = Strip(5)
    r = Strip(6)
    print(p.a)
    print(r.a)
    print(Strip.a)


if __name__ == '__main__':
    main()
else:
    pass
