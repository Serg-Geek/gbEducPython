import model.model_txt as m_txt
import model.model_json as m_json
from setting import db_setting


def init():
    if db_setting["db_format"] == "txt":
        m_txt.init()
    elif db_setting["db_format"] == "json":
        m_json.init()


def get_all_data():  # Возвращает форматированный словарь с ФИО И № тел
    if db_setting["db_format"] == "txt":
        return m_txt.get_all_data()
    elif db_setting["db_format"] == "json":
        return m_json.get_all_data()


def match_by_id(a_keys):  # принимает список ключей возвращает форматированную строку с ФИО и №тел
    if db_setting["db_format"] == "txt":
        return m_txt.match_by_id(a_keys)

    elif db_setting["db_format"] == "json":
        return m_json.match_by_id(a_keys)


def view_all_name():
    if db_setting["db_format"] == "txt":
        return m_txt.view_all_name()
    elif db_setting["db_format"] == "json":
        return m_json.view_all_name()


def view_all_tel():
    if db_setting["db_format"] == "txt":
        return m_txt.view_all_tel()
    elif db_setting["db_format"] == "json":
        return m_json.view_all_tel()


def find_nam_keys(a):  # принимает имя , возвращает список с ключами
    if db_setting["db_format"] == "txt":
        return m_txt.find_nam_keys(a)
    elif db_setting["db_format"] == "json":
        return m_json.find_nam_keys(a)


def get_tel_keys(a):  # принимает имя , возвращает список с ключами
    if db_setting["db_format"] == "txt":
        return m_txt.get_tel_keys(a)
    elif db_setting["db_format"] == "json":
        return m_json.get_tel_keys(a)


def add_name(value):  # добфвляум имя в бд
    if db_setting["db_format"] == "txt":
        m_txt.add_name(value)
    elif db_setting["db_format"] == "json":
        m_json.add_name(value)


def add_tel(id, value):  # добфвляум tel в бд
    if db_setting["db_format"] == "txt":
        m_txt.add_tel(id, value)
    elif db_setting["db_format"] == "json":
        m_json.add_tel(id, value)
