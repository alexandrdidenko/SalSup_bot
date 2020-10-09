import config
import task

text = 'Статус АДП на'


def prim_sec_sales(id_person):
    task.run_macro(config.xls_prim_sec_sales, config.macros_prim_sec_sales)
    task.send(id_person, config.photo_prim_sec_sales, text, __file__)
    task.del_fife(config.photo_prim_sec_sales)


if __name__ == '__main__':
    prim_sec_sales(config.ID_SALESSUPPORT_CHANNEL)
