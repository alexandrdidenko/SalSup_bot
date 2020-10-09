import config
import task

text = 'Статус по экспортам'


def export(id_person):
    task.run_macro(config.xls_export, config.macros_export)
    task.send(id_person, config.photo_export, text, __file__)
    task.del_fife(config.photo_export)


if __name__ == '__main__':
    export(config.ID_SALESSUPPORT_CHANNEL)
