import config
import task

text = 'Проверка продаж в кубе: '


def cube_sales(id_person):
    task.run_macro(config.xls_cube_sales, config.macros_cube_sales)
    task.send(id_person, config.photo_cube_sales, text, __file__)
    task.del_fife(config.photo_cube_sales)


if __name__ == '__main__':
    cube_sales(config.ID_SALESSUPPORT_CHANNEL)
