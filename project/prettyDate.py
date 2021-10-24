from datetime import date


def pretty_date():
    months = {"01": "januari", "02": "februari", "03": "maret",
              "04": "april", "05": "mei", "06": "juni",
              "07": "juli", "08": "agustus", "09": "september",
              "10": "oktober", "11": "november", "12": "desember"}

    today = date.today().strftime("%d-%m-%y").split("-")
    day, month, year = today[0], str(today[1]), today[2]
    return f"{day} {months[month]} {year}"


print(pretty_date)
