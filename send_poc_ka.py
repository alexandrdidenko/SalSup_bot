import config
import task

text = 'Статус: мастердата КА'


def poc_ka(id_person):
    task.run_macro(config.xls_poc_ka, config.macros_poc_ka)
    task.send(id_person, config.photo_poc_ka, text, __file__)
    task.del_fife(config.photo_poc_ka)


if __name__ == '__main__':
    poc_ka(config.ID_SALESSUPPORT_CHANNEL)
