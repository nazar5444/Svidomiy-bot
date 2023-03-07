import sqlite3 as sq

global db, cur


async def db_start():
    global db, cur

    with sq.connect("users.db") as db:
        cur = db.cursor()

        cur.execute(
            "CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, phone_number TEXT, verified TEXT, photo TEXT, "
            "geo_lat TEXT, geo_long TEXT, banned INTEGER, description TEXT)")
        db.commit()


async def profile(user_id, verified):
    user = cur.execute("SELECT 1 FROM users WHERE user_id = '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (user_id, " ", verified, '', " ", "", "", ""))
    db.commit()


async def edit_profile(user_id, phone_number):
    cur.execute("UPDATE users SET phone_number = '{}' WHERE user_id = '{}'".format(phone_number, user_id))
    db.commit()


async def change_profile(user_id):
    cur.execute("UPDATE users SET verified = 'True' WHERE user_id = '{}'".format(user_id))
    db.commit()


async def verif_profile(user_id):
    cur.execute("SELECT verified FROM users WHERE user_id = '{}'".format(user_id))
    ftchprnt = cur.fetchone()
    db.commit()
    return ftchprnt[0]


async def photo_add(user_id, photo):
    cur.execute("UPDATE users SET photo = '{}' WHERE user_id = '{}'".format(photo, user_id))
    db.commit()


async def lat_add(user_id, geo_lat):
    cur.execute("UPDATE users SET geo_lat = '{}' WHERE user_id = '{}'".format(geo_lat, user_id))
    db.commit()


async def long_add(user_id, geo_long):
    cur.execute("UPDATE users SET geo_long = '{}' WHERE user_id = '{}'".format(geo_long, user_id))
    db.commit()


async def photo_get(user_id):
    cur.execute("SELECT photo FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    db.commit()
    return row[0]


async def lat_get(user_id):
    cur.execute("SELECT geo_lat FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    db.commit()
    return row[0]


async def long_get(user_id):
    cur.execute("SELECT geo_long FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    db.commit()
    return row[0]


async def photo_delete(user_id):
    cur.execute("UPDATE users SET photo = NULL WHERE user_id = '{}'".format(user_id))
    db.commit()


async def lat_delete(user_id):
    cur.execute("UPDATE users SET geo_lat = NULL WHERE user_id = '{}'".format(user_id))
    db.commit()


async def long_delete(user_id):
    cur.execute("UPDATE users SET geo_long = NULL WHERE user_id = '{}'".format(user_id))
    db.commit()


async def ban_user(user_id):
    cur.execute("UPDATE users SET banned = 1 WHERE user_id = '{}'".format(user_id))
    db.commit()


async def unban_user(user_id):
    cur.execute("UPDATE users SET banned = 0 WHERE user_id = '{}'".format(user_id))
    db.commit()


def is_banned(user_id):
    cur.execute("SELECT banned FROM users WHERE user_id = '{}'".format(user_id))
    result = cur.fetchone()
    return result is not None and result[0] == 1


async def description_add(description, user_id):
    cur.execute("UPDATE users SET description = '{}' WHERE user_id = '{}'".format(description, user_id))
    db.commit()


async def description_get(user_id):
    cur.execute("SELECT description FROM users WHERE user_id = '{}'".format(user_id))
    row = cur.fetchone()
    db.commit()
    return row[0]


async def description_delete(user_id):
    cur.execute("UPDATE users SET description = NULL WHERE user_id = '{}'".format(user_id))
    db.commit()
