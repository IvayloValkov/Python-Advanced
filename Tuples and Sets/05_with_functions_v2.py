def main_input_and_logic(command):
    phone_book = {}

    while True:
        if command.isdigit():
            check_name_and_print(command, phone_book)
            break
        name, number = command.split("-")
        if name not in phone_book:
            phone_book[name] = number
        phone_book[name] = number

        command = input()


def check_name_and_print(count, phone_book):
    count = int(count)
    for _ in range(count):
        line = input()
        if line not in phone_book:
            print(f"Contact {line} does not exist.")
        else:
            print(f'{line} -> {phone_book[line]}')


main_input_and_logic(input())