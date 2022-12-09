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
            f"6 -  add Person\n"
            f'7 -  edit Person\n'
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
          
            f_nam = view.get_str("input name")
            find_get_keys = model.find_nam_keys(f_nam)
            result = model.match_by_id(find_get_keys)
            view.result_page(result)
        elif v == 5:# поиск по телефону
            f_tel= view.get_str('input tel')
            find_get_keys=model.get_tel_keys(f_tel)
            result = model.match_by_id(find_get_keys)
            view.result_page(result)
        # добавление персоны (фио,дата рождения,  № телефлна)
        elif v == 6:
            new_name =view.get_str('enter new name')
            id = model.add_name(new_name)
       
            birth_data = view.get_str('enter birth data(format dd/mm/yyyy')
            model.add_birth(id, birth_data)
            new_tel =view.get_str('enter # tel')
            model.add_tel(id,new_tel)
        # Редактарование персоны    
        elif v == 7:
            view.print_dct(model.view_all_name())
            id= view.get_numb('введите ID для редактирования персоны')
            record = model.get_record(id)
            new_name =view.get_str(record['name']+' Введите новое имя')
            if len(new_name)>0:
                model.edit_name(id, new_name)
            birth_data = view.get_str('введите дату рождения:(format dd/mm/yyyy)')
            if len(birth_data)>0:
                model.edit_birth(id, birth_data)
            new_tel =view.get_str('введите номер телефона')
            if len(new_tel)>0:
                model.edit_tel(id,new_tel)
        elif v == 0:
            break