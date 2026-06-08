from main import *


def vypis_okresu():
    data = get_okresy()

    print("\n--- OKRESY ---")
    for d in data:
        print(d[0], d[1])


def obce_v_okrese():
    id_okres = input("Zadej kód okresu: ")

    data = get_obce_okres(id_okres)

    print("\nNázev | Obyvatelé | Průměrný věk")
    print("Žádná data.")

    for d in data:
        print(d[0], "|", d[1], "|", round(d[2], 1))


def hledani_obce():
    text = input("Zadej část názvu obce: ")

    data = search_obec(text)

    print("\n--- VÝSLEDKY ---")

    for d in data:
        print(d[0])


def statistika_okresu():
    id_okres = input("Zadej kód okresu: ")

    data = stats_okres(id_okres)

    if not data or data[0] is None:
        print("Žádná data.")
        return

    print("\n--- STATISTIKA ---")
    print("Celkem:", data[0])
    print("Průměr:", round(data[1], 2))
    print("Muži:", data[2])
    print("Ženy:", data[3])


def top10():
    data = top10_obci()

    print("\n--- TOP 10 OBCE ---")

    for i, d in enumerate(data, 1):
        print(i, ".", d[0], "-", d[1])


def export():
    id_okres = input("Zadej kód okresu pro export: ")

    result = export_csv(id_okres)

    if result:
        print("Soubor uložen:", result)
    else:
        print("Žádná data.")


def graf():
    id_okres = input("Zadej kód okresu pro graf: ")

    result = graf_okres(id_okres)

    if not result:
        print("Žádná data.")


def menu():
    while True:
        print("""
=========================
 DEMOGRAFIE ČR
=========================

1 - Seznam okresů
2 - Obce v okrese
3 - Hledat obec
4 - Statistiky okresu
5 - TOP 10 obcí
6 - Export CSV
7 - Graf
0 - Konec
""")

        volba = input("Vyber: ")

        if volba == "1":
            vypis_okresu()

        elif volba == "2":
            obce_v_okrese()

        elif volba == "3":
            hledani_obce()

        elif volba == "4":
            statistika_okresu()

        elif volba == "5":
            top10()

        elif volba == "6":
            export()

        elif volba == "7":
            graf()

        elif volba == "0":
            print("Konec programu.")
            break

        else:
            print("Neplatná volba!")
