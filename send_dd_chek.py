import config
import task

text = 'Статус: точки DD'


def dd_chek(id_person):
    task.run_macro(config.xls_DD_chek, config.macros_DD_chek)
    task.send(id_person, config.photo_DD_chek, text, __file__)
    task.del_fife(config.photo_DD_chek)


if __name__ == '__main__':
    dd_chek(config.id_bot_and_my)
