import view
import model.model as model


def start():
    view.showinfo("hello! ")
    while True:
        v = view.get_numb_menu(
            f"Choose:\n"
            f"1 -  print all list\n"
            f"2 -  print all names\n"
            f"3 -  print all phones\n"
            f"4 -  find name\n"
            f"5 -  find phone\n"
            f"6 -  add name\n"
            f'7 -  add tel\n'
            f'0 -  exit'
        )
        
        model.init()
        if v == 1:
            result = model.get_all_data()
            view.print_dct(result)
        elif v == 2:
            result = model.view_all_name()
            view.print_dct(result)
        elif v == 3:
            result = model.view_all_tel()
            view.print_dct(result)
        elif v == 4:#поиск по имени
            print("input name")
            f_nam = view.get_str()
            find_get_keys = model.find_nam_keys(f_nam)
            result = model.match_by_id(find_get_keys)
            view.result_page(result)
        elif v == 5:# поиск по телефону
            print('input tel')
            f_tel= view.get_str()
            find_get_keys=model.get_tel_keys(f_tel)
            result = model.match_by_id(find_get_keys)
            view.result_page(result)
        
        elif v == 6:
            print('enter new name')
            new_name =view.get_str()
            model.add_name(new_name)
            
        elif v == 7:
            view.print_dct(model.view_all_name())
            print('enter id for new tel or changed tel')
            id= view.get_numb()
            print('enter # tel')
            new_tel =view.get_str()
            model.add_tel(id,new_tel)
        elif v == 0:
            break