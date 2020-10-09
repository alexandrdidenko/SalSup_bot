import config
import task

text = 'Статус по синкам'


def sync(id_person):
    task.run_macro(config.xls_sync, config.macros_sync)
    task.send(id_person, config.photo_sync, text, __file__)
    task.del_fife(config.photo_sync)


if __name__ == '__main__':
    sync(config.ID_SALESSUPPORT_CHANNEL)
