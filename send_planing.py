import config
import task

text = 'Статус планирования на'
text2 = 'Статус обновления фокусов на'

task.run_macro(config.xls_planing, config.macros_planing)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_plaping, text, __file__)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_plaping_focus, text2, __file__)
task.del_fife(config.photo_plaping)
task.del_fife(config.photo_plaping_focus)