import config
import task

text = 'Статус выгрузки продаж на'


def infochek(id_person):
    task.run_macro(config.xls_infoChek, config.macros_infoChek)
    task.send(id_person, config.photo_infoChek, text, __file__)
    task.del_fife(config.photo_infoChek)


if __name__ == '__main__':
    infochek(config.ID_SALESSUPPORT_CHANNEL)
