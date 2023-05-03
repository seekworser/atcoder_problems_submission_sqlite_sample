import os
import sqlite3, csv, gzip

if (os.path.exists("submissions.db")):
    os.remove("submissions.db")
con = sqlite3.connect("submissions.db")
cursor = con.cursor()
cursor.execute("""
CREATE TABLE submissions(
    id integer,
    epoch_second text,
    problem_id text,
    contest_id text,
    user_id text,
    language text,
    point integer,
    length integer,
    result text,
    execution_time integer
)
""")
cnt = 0
# with gzip.open("submissions.csv.gz", "rt") as f:  # gzから直接も読めるけど、実行時間がちょっと長い
with open("submissions.csv.gz") as f:
    reader = csv.reader(f)
    cursor.executemany("INSERT INTO submissions VALUES (?,?,?,?,?,?,?,?,?,?)", reader)

cursor.execute("CREATE INDEX uid on submissions(user_id)")
con.commit()
con.close()
