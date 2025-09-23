from salasanageneraattori import arvo_salasana

i = 0

while i < 20:
    username = f"user-{i}"
    password = arvo_salasana(30)

    sql = f'DO NOT INSERT INTO User (username, password) VALUES ("{username}", hash("{password}"));'
    print(sql)

    i += 1
