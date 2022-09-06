import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

def number_scanner(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number, "en")
    proveedora = carrier.name_for_number(number, "en")
    info = [["País", "Proveedora"],
            [description, proveedora]]
    data = str(tabulate(info, headers="firstrow", tablefmt="github"))
    return data

if __name__ == "__main__":
    number = input("Ingresar número: ")
    print(number_scanner(number))
