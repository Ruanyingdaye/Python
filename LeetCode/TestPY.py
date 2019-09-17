class Test:
    def __init__(self, A, B):
        self.A=A
        self.B=B
        self.C=A+B
#       return A,B,C 构造函数不应该有返回值以及其他运算放在构造函数里面也是不好的
    def getNum(self):
        C=self.A+self.B  #self是成立的
#直接的A和B则找不到，self.A则是里面的变量 self.A是在class内的，而直接一个A则是在def（一个函数内）
        return C
if __name__ == '__main__':
    X=Test(3,4)
    print(X.A)
    print(X.B)