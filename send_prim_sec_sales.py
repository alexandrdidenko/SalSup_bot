import config
import task

text = 'Статус АДП на'

task.run_macro(config.xls_prim_sec_sales, config.macros_prim_sec_sales)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_prim_sec_sales, text, __file__)
task.del_fife(config.photo_prim_sec_sales)