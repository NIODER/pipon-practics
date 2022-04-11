from faulthandler import cancel_dump_traceback_later
from http.client import SWITCHING_PROTOCOLS
from turtle import goto

while True:
    first_number = float(input())
    second_number = float(input())
    operation = input()

    calculate = {
        "-": first_number - second_number,
        "+": first_number + second_number,
        "*": first_number * second_number,
        "/": first_number / second_number
    }

    try:
        print(calculate[operation])
    except KeyError as e:
        print("ошибка ввода")