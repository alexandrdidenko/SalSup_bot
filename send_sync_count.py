import config
import task

text = 'Статус: синки ТПД'

task.run_macro(config.xls_sync_count, config.macros_sync_count)
task.send(config.id_bot_and_my, config.photo_sync_count, text, __file__)
task.del_fife(config.photo_sync_count)
