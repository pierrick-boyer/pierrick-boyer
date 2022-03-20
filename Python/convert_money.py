from currency_converter import CurrencyConverter


def convert_sum():
    convert = CurrencyConverter()
    sum_to_convert = input("Enter the sum to convert : ")

    try:
        result_sum = int(sum_to_convert)

        choices = [
            'EUR', 'USD',
            'CAD', 'JPY',
        ]
        print(choices)

        choices_1 = input("Choose the type of currency to convert : ")
        result_1 = str(choices_1)

        choices_2 = input("Choose the type of currency to convert to : ")
        result_2 = str(choices_2)

        if result_1 in choices or result_2 in choices:

            if result_1 != result_2:
                convert_result = convert.convert(result_sum, result_1, result_2)
                return f"The result of the {result_sum}{result_1} in {result_2} is {convert_result}."

            else:
                convert_error = f"You can convert {choices_1} in {choices_2}."
                return convert_error

        else:
            return "this choice does not exist."

    except Exception as error:
        print(error)
        return str("This is not a number.")
