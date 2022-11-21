x_bin=None
y_bin=None

def init_bin(a,b):
    global x_bin
    global y_bin

    x_bin=int(a)
    y_bin=int(b)

def summa_bin():
    return bin(x_bin+y_bin)
def mult_bin():
    return bin(x_bin*y_bin)
def div_bin():
    return x_bin/y_bin
def minus():
    return x_bin-y_bin
