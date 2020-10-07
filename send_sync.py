import config
import task

text = 'Статус по синкам'


def send_sync():
    task.run_macro(config.xls_sync, config.macros_sync)
    task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_sync, text, __file__)
    task.del_fife(config.photo_sync)


def send_sync_my():
    task.run_macro(config.xls_sync, config.macros_sync)
    task.send(config.id_bot_and_my, config.photo_sync, text, __file__)
    task.del_fife(config.photo_sync)


if __name__ == '__main__':
    send_sync()
