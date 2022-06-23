
def lol(cls):
    return cls.__lol__()

class A:
    def __lol__(self):
        return "lol"


a=A() # output => logging called
print(lol(a))
