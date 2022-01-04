def A(func):
    print('A')
    def B():
        print('B')
        func()
    return (B)

@A
def c():
    print('C')

c()