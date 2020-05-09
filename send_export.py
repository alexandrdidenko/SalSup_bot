import config
import task

text = 'Статус по экспортам'

task.run_macro(config.xls_export, config.macros_export)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_export, text, __file__)
task.del_fife(config.photo_export)
