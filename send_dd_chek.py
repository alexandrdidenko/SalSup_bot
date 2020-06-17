import config
import task

text = 'Статус: точки DD'

task.run_macro(config.xls_DD_chek, config.macros_DD_chek)
task.send(config.id_bot_and_my, config.photo_DD_chek, text, __file__)
task.del_fife(config.photo_DD_chek)
