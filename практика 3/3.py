lastTicket = 123321


def lucky(ticket):
    str_number = str(ticket)
    while len(str_number) < 6:
        str_number = "0" + str_number
    first_three = str_number[0:3]
    last_three = str_number[len(str_number) - 3:len(str_number)]
    last_ticket_last_three = str(lastTicket)[0:3]
    last_ticket_first_three = str(lastTicket)[len(str(lastTicket)) - 3:len(str(lastTicket))]
    if int(first_three) == int(last_three) and int(last_ticket_first_three) == int(last_ticket_last_three):
        return "Счастливый"
    else:
        return "Несчастливый"


print(lucky(100001))

