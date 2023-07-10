import sqlite3

def create_table():
       with sqlite3.connect("game_alice.db") as conexion:
            try:
                sentence = ''' CREATE TABLE IF NOT EXISTS players
                                (
                                    id INTEGER primary key autoincrement,
                                    name TEXT,
                                    score INTEGER,
                                    level INTEGER
                                )
                            '''

                conexion.execute(sentence)
                # print("Se creó la tabla players")
            except sqlite3.OperationalError:
                print("La tabla ya existe")

def save_score(name, score, level):
  try:
    sqlConnect = sqlite3.connect("game_alice.db")
    cursor = sqlConnect.cursor()
    cursor.execute(
        "INSERT INTO players (name, score, level) VALUES (?, ?, ?)", (name, score, level))
    sqlConnect.commit()
    cursor.close()
  except sqlite3.OperationalError as error:
     print("Error ", error)

def get_score():
  with sqlite3.connect("game_alice.db") as conexion:
      sql_select = "SELECT * FROM players ORDER BY score DESC"
      cur = conexion.cursor()
      res = cur.execute(sql_select)
      return cur.execute(sql_select).fetchall()
