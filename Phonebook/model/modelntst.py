import name_number as name

# import controller

nam = {}
tel = {}

def init():
    global nam
    global tel
    nam = name.dct_name
    tel = name.dct_tel


def get_all_data():# Возвращает форматированный словарь с ФИО И № тел
    dct_all = nam.copy()
    for k, v in nam.items():
        dct_all[k] = v + " ---- " + tel.get(k, "")
    return dct_all


def match_by_id(a_keys): # принимает список ключей возвращает форматированную строку с ФИО и №тел
    st = []
    for key in a_keys:
        st.append(nam[key] + "------" + tel.get(key, ""))
    return st


def view_all_name():
    return nam


def view_all_tel():
    return tel


def find_nam_keys(a):# принимает имя , возвращает список с ключами
    find = []
    for k in nam:
        if a.lower() in nam[k].lower():
            find.append(k)
    return find
