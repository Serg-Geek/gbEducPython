import model
import view
import model_2
def start():
    view.showinfo('hello! ')
    v= int(view.get_numb(f'Choose:\n'
                f'1 -  +\n'
                f'2 -  *\n'
                f'3 -  /\n'
                f'4 -  -\n'
                f'--->>'))
    a= view.get_numb('input num a-->>')
    b = view.get_numb('input num b-->>')
    dec_bin=int(view.get_numb(f'choose dec or bin\n'
                            f'if dec -->> 1\n'
                            f'if bin -->> 2\n'
                            f'--->>>'))
    if dec_bin == 1:
        model.init(a,b)
        if v==1:
            result = model.summa()
        elif v==2:
            result = model.mult()
        elif v==3:
            result = model.div()
        else:
            result = model.minus()
        view.showinfo(result)
    else :
        model_2.init_bin(a,b)
        if v==1:
            result = model_2.summa_bin()
        elif v==2:
            result = model_2.mult_bin()
        elif v==3:
            result = model_2.div_bin()
        else:
            result = model_2.minus_bin()
        view.showinfo(result)