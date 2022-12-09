import json
import setting as set


base = {}
def init():
    global base
    with open(set.db_setting["path"] + set.db_setting["base"]+ set.db_setting['db_format'], "r") as data:
        data_nam = data.read()  # get str
        base = json.loads(data_nam)
    

def get_all_data():  # Возвращает форматированный словарь с ФИО И № тел
    dct_all = base["nam"].copy()
    for k, v in base["nam"].items():
        dct_all[k] = v + " ---- "+ base["birth"].get(k,"")+"г.р.----" + base["tel"].get(k, "")
    return dct_all


def match_by_id(a_keys):  # принимает список ключей возвращает форматированную строку с ФИО и №тел
    st = []
    for key in a_keys:
        st.append(base['nam'][key] + "------" + base["birth"].get(key,"")+ "г.р."+ "----" + base["tel"].get(key, ""))
    return st

# принимает id возвращает словарь с даннымии
def get_record(id):
    birth = base["birth"].get(id, '')
    name=base["nam"].get(id,'')
    new_tel=base["tel"].get(id,'')
    record = { "name":  name,
               "birth": birth,
               "tel": new_tel,
    }
    return record

def edit_name(id, name):
    base["nam"][id] = name
    save_changes_in_DB()

def edit_birth(id, birth):
    base["birth"][id] = birth
    save_changes_in_DB()

def edit_tel(id, tel):
    base["tel"][id] = tel
    save_changes_in_DB()


def view_all_name():
    return base["nam"]


def view_all_tel():
    return base["tel"]

def find_nam_keys(a):  # принимает имя , возвращает список с ключами
    find = []
    for k in base['nam']:
        if a.lower() in base['nam'][k].lower():
            find.append(k)
    return find


def get_tel_keys(a):  # принимает имя , возвращает список с ключами
    find = []
    for k in base['tel']:
        if a.lower() in base['tel'][k].lower():
            find.append(k)
    return find


def add_name(value):  # добфвляум имя в бд
    new_id = 0
    for k in base['nam']:
        if int(k) > new_id:
            new_id = int(k)
    base['nam'][new_id + 1] = value
    save_changes_in_DB("nam")
    return new_id+1

def add_tel(id, value):  # добфвляум tel в бд
    base['tel'][id] = value
    save_changes_in_DB("tel")


def add_birth(id,value):  # добфвляум дату рождения в бд
    base['birth'][id] = value
    save_changes_in_DB("birth")


def save_changes_in_DB():
    with open(set.db_setting["path"] + set.db_setting["base"]+ set.db_setting['db_format'], "w") as data:
        data.write(json.dumps(base))