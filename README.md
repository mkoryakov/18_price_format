# Price Formatter

Скрипт предназначен для форматирования цены в удобный для восприятия вид. При запуске из командной строки необходимо передать скрипту обязательны параметр - цену. Также можно импортировать функцию format\_price из модуля format\_price.py и использовать ее в других скриптах.

# Установка
Для запуска скрипта дополнительных действий не требуется.

# Примеры работы скрипта
    $ python format_price 2014
    2 014.00
    $ python format_price error_value
    None

# Запуск автоматических тестов
Для тестирования работы скрипта написаны автоматические тесты, которые запускаются командой

    $ python tests.py
Если все тесты прошли удачно появится вывод
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
в противном случае будет сообщение об ошибке.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
