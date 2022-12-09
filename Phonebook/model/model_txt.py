from setting import db_setting


nam = {}
tel = {}
birth ={}

def init():
    # прорверяем есть ли файл, естли есть исключение
    try: 
        f =  open(db_setting["path"] + db_setting.get("tab_name",'tab_name.')+ db_setting['db_format'], "x")# 
        f.close
    except: None
    try: 
        f =  open(db_setting["path"] + db_setting.get("tab_tel",'tab_tel.')+ db_setting['db_format'], "x")
        f.close
    except: None
    try: 
        f =  open(db_setting["path"] + db_setting.get("tab_birth",'tab_birth.')+ db_setting['db_format'], "x")
        f.close
    except: None

   
    with open(db_setting["path"] + db_setting.get("tab_name",'tab_name.')+ db_setting['db_format'], "r") as data:
        for line in data:
            key, value = line.replace("\n", "").split(".", 2)
            nam[int(key)] = value.strip()
    with open(db_setting["path"] + db_setting.get("tab_tel",'tab_tel.')+ db_setting['db_format'], "r") as data:
        for line in data:
            key, value = line.replace("\n", "").split(".", 2)
            tel[int(key)] = value.strip()
    with open(db_setting["path"] + db_setting.get("tab_birth",'tab_birth.')+ db_setting['db_format'], "r") as data:
        for line in data:
            key, value = line.replace("\n", "").split(".", 2)
            birth[int(key)] = value.strip()


def get_all_data():  # Возвращает форматированный словарь с ФИО И № тел
    dct_all = nam.copy()
    for k, v in nam.items():
        dct_all[k] = v + " ---- " + birth.get(k,"")+ "г.р." + "-----" + tel.get(k, "")
    return dct_all


def match_by_id(a_keys):  # принимает список ключей возвращает форматированную строку с ФИО и №тел
    st = []
    for key in a_keys:
        st.append(nam[key] + "------" + birth.get(k,"")+ "г.р." + tel.get(key, ""))
    return st

def view_all_name():
    return nam

def view_all_tel():
    return tel

# принимает id возвращает словарь с даннымии
def get_record(id):
    new_birth = birth.get(id,'')
    name=nam.get(id,'')
    new_tel=tel.get(id,'')
    record = { "name":  name,
               "birth": new_birth,
               "tel": new_tel,
    }
    return record

def edit_name(id, new_name):
    nam[id] = new_name
    save_changes_in_DB("nam")

def edit_birth(id, new_birth):
    birth[id] = new_birth
    save_changes_in_DB('birth')

def edit_tel(id, new_tel):
    tel[id] = new_tel
    save_changes_in_DB('tel')

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
    return new_id+1

def add_tel(id, value):  # добфвляум tel в бд
    tel[id] = value
    save_changes_in_DB("tel")

def add_birth(id, value):  # добфвляум дату в бд
    birth[id] = value
    save_changes_in_DB('birth')

def save_changes_in_DB(dct_type):
    if dct_type == "nam":
        with open(db_setting["path"] + db_setting.get("tab_name",'tab_name.')+ db_setting['db_format'], "w") as data:
            for k, v in nam.items():
                data.write("{}. {}\n".format(k, v))
    elif dct_type == "tel":
        with open(db_setting["path"] + db_setting.get("tab_tel",'tab_tel.')+ db_setting['db_format'], "w") as data:
            for k, v in tel.items():
                data.write("{}. {}\n".format(k, v))
    elif dct_type == "birth":
        with open(db_setting["path"] + db_setting.get("tab_birth",'tab_birth.')+ db_setting['db_format'], "w") as data:
            for k, v in birth.items():
                data.write("{}. {}\n".format(k, v))