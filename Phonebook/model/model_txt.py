from setting import db_setting


nam = {}
tel = {}


def init():
    # global nam
    # global tel
    with open(db_setting["path"] + db_setting["tab_name"], "r") as data:
        for line in data:
            key, value = line.replace("\n", "").split(".", 2)
            nam[int(key)] = value.strip()
    with open(db_setting["path"] + db_setting["tab_tel"], "r") as data:
        for line in data:
            key, value = line.replace("\n", "").split(".", 2)
            tel[int(key)] = value.strip()


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
        with open(db_setting["path"] + db_setting["tab_name"], "w") as data:
            for k, v in nam.items():
                data.write("{}. {}\n".format(k, v))
    elif dct_type == "tel":
        with open(db_setting["path"] + db_setting["tab_tel"], "w") as data:
            for k, v in tel.items():
                data.write("{}. {}\n".format(k, v))
