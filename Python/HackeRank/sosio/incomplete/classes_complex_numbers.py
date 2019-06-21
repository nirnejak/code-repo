import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        self.real += no.real
        self.imaginary += no.imaginary

        print("{0:.2f}+{0:.2f}i".format(self.real, self.imaginary))

    def __sub__(self, no):
        self.real -= no.real
        self.imaginary -= no.imaginary

        print("{0:.2f}+{0:.2f}i".format(self.real, self.imaginary))

    def __mul__(self, no):
        self.real = ((self.real*no.real)-(self.imaginary*no.imaginary))
        self.imaginary = ((self.real*no.imaginary)+(self.imaginary*no.real))

        print("{0:.2f}+{0:.2f}i".format(self.real, self.imaginary))

    def __truediv__(self, no):
        self.real = (((self.real)*(no.real))+((self.imaginary)*(no.imaginary)))/(pow(no.real,2)+pow(no.imaginary,2))
        self.imaginary = (((no.real)*(self.imaginary))-((self.real)*(no.imaginary)))/(pow(no.real,2)+pow(no.imaginary,2))

        print("{0:.2f}+{0:.2f}i".format(self.real, self.imaginary))

    def mod(self):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')