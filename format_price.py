from argparse import ArgumentParser


def format_price(price):
    try:
        stirng_price = str(price)
        float_price = float(stirng_price)
        comma_separated_price = '{0:,.0f}'.format(float_price)
        return comma_separated_price.replace(',', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    parser = ArgumentParser(prog='format_price',
                            description='Скрипт, форматирующий цену товара')
    parser.add_argument('price', help='цена товара')
    unformatted_price = parser.parse_args().price
    formatted_price = format_price(unformatted_price)
    print(formatted_price)
