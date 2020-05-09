import config
import task

text = 'Статус выгрузки продаж на'

task.run_macro(config.xls_infoChek, config.macros_infoChek)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_infoChek, text, __file__)
task.del_fife(config.photo_infoChek)
