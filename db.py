import psycopg2

global conn, cur


async def db_start():
    global conn, cur

    conn = psycopg2.connect(
        database="users",
        user="svidomiy",
        password="lfjfFFids565",
        host="178.128.241.165",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(user_id BIGINT PRIMARY KEY, city_id TEXT, phone_number TEXT, verified TEXT, photo TEXT, "
        "geo_lat TEXT, geo_long TEXT, banned INTEGER, alert_state INTEGER, description TEXT, photo_bomb TEXT, geo_lat_bomb TEXT, geo_long_bomb TEXT, description_bomb TEXT)")
    conn.commit()


async def profile(user_id, verified):
    cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))

    user = cur.fetchone()
    if not user:
        cur.execute(
            "INSERT INTO users (user_id, phone_number, verified, photo, geo_lat, geo_long, banned, alert_state, description, photo_bomb, geo_lat_bomb, geo_long_bomb, description_bomb) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (user_id, " ", verified, '', " ", "", 0, 0, "", "", "", "", ""))
    conn.commit()


async def edit_profile(user_id, phone_number):
    cur.execute("UPDATE users SET phone_number = '{}' WHERE user_id = '{}'".format(phone_number, user_id))
    conn.commit()


async def change_profile(user_id):
    cur.execute("UPDATE users SET verified = 'True' WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def del_profile(user_id):
    cur.execute("UPDATE users SET verified = 'False' WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def verif_profile(user_id):
    cur.execute("SELECT verified FROM users WHERE user_id = '{}'".format(user_id))
    ftchprnt = cur.fetchone()
    conn.commit()
    return ftchprnt[0]


async def photo_add(user_id, photo):
    cur.execute("UPDATE users SET photo = '{}' WHERE user_id = '{}'".format(photo, user_id))
    conn.commit()


async def lat_add(user_id, geo_lat):
    cur.execute("UPDATE users SET geo_lat = '{}' WHERE user_id = '{}'".format(geo_lat, user_id))
    conn.commit()


async def long_add(user_id, geo_long):
    cur.execute("UPDATE users SET geo_long = '{}' WHERE user_id = '{}'".format(geo_long, user_id))
    conn.commit()


async def photo_get(user_id):
    cur.execute("SELECT photo FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def lat_get(user_id):
    cur.execute("SELECT geo_lat FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def long_get(user_id):
    cur.execute("SELECT geo_long FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def photo_delete(user_id):
    cur.execute("UPDATE users SET photo = NULL WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def lat_delete(user_id):
    cur.execute("UPDATE users SET geo_lat = NULL WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def long_delete(user_id):
    cur.execute("UPDATE users SET geo_long = NULL WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def ban_user(user_id):
    cur.execute("UPDATE users SET banned = 1 WHERE user_id = %s", (user_id,))
    conn.commit()


async def unban_user(user_id):
    cur.execute("UPDATE users SET banned = 0 WHERE user_id = %s", (user_id,))
    conn.commit()


def is_banned(user_id):
    cur.execute("SELECT banned FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    return result is not None and result[0] == 1


async def description_add(user_id, description):
    cur.execute("UPDATE users SET description = %s WHERE user_id = %s", (description, user_id))
    conn.commit()


async def description_get(user_id):
    cur.execute("SELECT description FROM users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def description_delete(user_id):
    cur.execute("UPDATE users SET description = NULL WHERE user_id = %s", (user_id,))
    conn.commit()


async def city_add(user_id, city_id):
    cur.execute("UPDATE users SET city_id = %s WHERE user_id = %s", (city_id, user_id))
    conn.commit()


async def city_get(user_id):
    cur.execute("SELECT city_id FROM users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def alert_on(user_id):
    cur.execute("UPDATE users SET alert_state = 1 WHERE user_id = %s", (user_id,))
    conn.commit()


async def alert_off(user_id):
    cur.execute("UPDATE users SET alert_state = 0 WHERE user_id = %s", (user_id,))
    conn.commit()


def is_alert_on(user_id):
    cur.execute("SELECT alert_state FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    return result is not None and result[0] == 1


async def photo_bomb_add(user_id, photo_bomb):
    cur.execute("UPDATE users SET photo_bomb = '{}' WHERE user_id = '{}'".format(photo_bomb, user_id))
    conn.commit()


async def photo_bomb_get(user_id):
    cur.execute("SELECT photo_bomb FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def photo_bomb_delete(user_id):
    cur.execute("UPDATE users SET photo_bomb = NULL WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def lat_bomb_add(user_id, geo_lat_bomb):
    cur.execute("UPDATE users SET geo_lat_bomb = '{}' WHERE user_id = '{}'".format(geo_lat_bomb, user_id))
    conn.commit()


async def lat_bomb_get(user_id):
    cur.execute("SELECT geo_lat_bomb FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def lat_bomb_delete(user_id):
    cur.execute("UPDATE users SET geo_lat_bomb = NULL WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def long_bomb_add(user_id, geo_long_bomb):
    cur.execute("UPDATE users SET geo_long_bomb = '{}' WHERE user_id = '{}'".format(geo_long_bomb, user_id))
    conn.commit()


async def long_bomb_get(user_id):
    cur.execute("SELECT geo_long_bomb FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def long_bomb_delete(user_id):
    cur.execute("UPDATE users SET geo_long_bomb = NULL WHERE user_id = '{}'".format(user_id))
    conn.commit()


async def description_bomb_add(user_id, description_bomb):
    cur.execute("UPDATE users SET description_bomb = %s WHERE user_id = %s", (description_bomb, user_id))
    conn.commit()


async def description_bomb_get(user_id):
    cur.execute("SELECT description_bomb FROM users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    conn.commit()
    return row[0]


async def description_bomb_delete(user_id):
    cur.execute("UPDATE users SET description_bomb = NULL WHERE user_id = %s", (user_id,))
    conn.commit()
