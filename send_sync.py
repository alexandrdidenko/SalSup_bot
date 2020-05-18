import config
import task

text = 'Статус по синкам'

task.run_macro(config.xls_sync, config.macros_sync)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_sync, text, __file__)
task.del_fife(config.photo_sync)
