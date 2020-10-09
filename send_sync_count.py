import config
import task

text = 'Статус: синки ТПД'


def sync_count(id_person):
    task.run_macro(config.xls_sync_count, config.macros_sync_count)
    task.send(id_person, config.photo_sync_count, text, __file__)
    task.del_fife(config.photo_sync_count)


if __name__ == '__main__':
    sync_count(config.id_bot_and_my)
