import psycopg
import csv
import matplotlib.pyplot as plt


# =========================
# PŘIPOJENÍ K DB
# =========================
def connect():
    return psycopg.connect(
        host="192.168.135.10",
        port=5432,
        dbname="obce",
        user="student",
        password="bluemonkey3"
    )


# =========================
# SQL FUNKCE
# =========================

def get_okresy():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id_okres, nazev FROM okresy ORDER BY id_okres")
    data = cur.fetchall()

    conn.close()
    return data


def get_obce_okres(id_okres):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT nazev, pocet_obyvatel, prumerny_vek
        FROM obce_pob
        WHERE id_okres = %s
        ORDER BY pocet_obyvatel DESC
    """, (id_okres,))

    data = cur.fetchall()
    conn.close()
    return data


def search_obec(text):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT nazev
        FROM obce_pob
        WHERE nazev ILIKE %s
        ORDER BY nazev
    """, (f"%{text}%",))

    data = cur.fetchall()
    conn.close()
    return data


def stats_okres(id_okres):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            SUM(pocet_obyvatel),
            AVG(prumerny_vek),
            SUM(pocet_muzi),
            SUM(pocet_zeny)
        FROM obce_pob
        WHERE id_okres = %s
    """, (id_okres,))

    data = cur.fetchone()
    conn.close()
    return data


def top10_obci():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT nazev, pocet_obyvatel
        FROM obce_pob
        ORDER BY pocet_obyvatel DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    conn.close()
    return data


# =========================
# BONUS CSV
# =========================
def export_csv(id_okres):
    data = get_obce_okres(id_okres)

    if not data:
        return False

    filename = f"{id_okres}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")

        writer.writerow(["Název", "Obyvatelé", "Průměrný věk"])

        for row in data:
            writer.writerow(row)

    return filename


# =========================
# BONUS GRAF
# =========================
def graf_okres(id_okres):
    data = get_obce_okres(id_okres)

    if not data:
        return False

    data = data[:10]

    nazvy = [d[0] for d in data]
    obyvatel = [d[1] for d in data]

    plt.figure(figsize=(10, 5))
    plt.bar(nazvy, obyvatel)

    plt.title(f"TOP obce v okrese {id_okres}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()

    return True