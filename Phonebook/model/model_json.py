import json
import setting as set

nam = {}
tel = {}


def init():
    global nam
    global tel
    with open(set.db_setting["path"] + set.db_setting["tab_name"]+ set.db_setting['db_format'], "r") as data:
        data_nam = data.read()  # get str

        nam = json.loads(data_nam)
        # for line in data:
        #     key, value = line.replace('\n','').split('.',2)
        #     nam[int(key)] = value.strip()
    with open(set.db_setting["path"] + set.db_setting["tab_tel"]+ set.db_setting['db_format'], "r") as data:
        data_tel = data.read()  # get str
        tel = json.loads(data_tel)
        # for line in data:
        #     key, value = line.replace('\n','').split('.',2)
        #     tel[int(key)] = value.strip()

    # nam = name.dct_name
    # tel = name.dct_tel


def get_all_data():  # Возвращает форматированный словарь с ФИО И № тел
    dct_all = nam.copy()
    for k, v in nam.items():
        dct_all[k] = v + " ---- " + tel.get(k, "")
    return dct_all


def match_by_id(a_keys):  # принимает список ключей возвращает форматированную строку с ФИО и №тел
    st = []
    for key in a_keys:
        st.append(nam[key] + "------" + tel.get(key, ""))
    return st


def view_all_name():
    return nam


def view_all_tel():
    return tel


def find_nam_keys(a):  # принимает имя , возвращает список с ключами
    find = []
    for k in nam:
        if a.lower() in nam[k].lower():
            find.append(k)
    return find


def get_tel_keys(a):  # принимает имя , возвращает список с ключами
    find = []
    for k in tel:
        if a.lower() in tel[k].lower():
            find.append(k)
    return find


def add_name(value):  # добфвляум имя в бд
    new_id = 0
    for k in nam:
        if int(k) > new_id:
            new_id = int(k)
    nam[new_id + 1] = value
    save_changes_in_DB("nam")


def add_tel(id, value):  # добфвляум tel в бд
    tel[id] = value
    save_changes_in_DB("tel")


def save_changes_in_DB(dct_type):
    if dct_type == "nam":
        with open(set.db_setting["path"] + set.db_setting["tab_name"]+ set.db_setting['db_format'], "w") as data:
            data.write(json.dumps(nam))
    elif dct_type == "tel":
        with open(set.db_setting["path"] + set.db_setting["tab_tel"]+ set.db_setting['db_format'], "w") as data:
            data.write(json.dumps(tel))
