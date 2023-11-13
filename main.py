from sys import argv
from util import CSVConverter, PKLConverter, TXTConverter, JSONConverter

try:
    in_file = argv[1]
    out_file = argv[2]
    out_extension = out_file.split('.')[-1]
    changes = argv[3:]
    supported_converters = {
        'csv': CSVConverter,
        'pkl': PKLConverter,
        'txt': TXTConverter,
        'json': JSONConverter
    }

    converter = supported_converters[out_extension](in_file, changes)
    converter.convert()

except IndexError:
    print('Podaj argumenty w formacie <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>\n'
            '<zmiana_x> - zmiana w postaci "x(kolumna),y(wiersz),wartość"')
except FileNotFoundError:
    print('Podaj prawidłową ścieżkę pliku. Obsługiwane formaty: csv, json, pkl, txt')
except ValueError:
    print('Współrzędne do zmiany muszą być liczbami całkowitymi')