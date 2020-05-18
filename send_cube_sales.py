import config
import task

text = 'Проверка продаж в кубе: '

task.run_macro(config.xls_cube_sales, config.macros_cube_sales)
task.send(config.ID_SALESSUPPORT_CHANNEL, config.photo_cube_sales, text, __file__)
task.del_fife(config.photo_cube_sales)
