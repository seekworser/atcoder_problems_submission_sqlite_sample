import sqlite3

con = sqlite3.connect("submissions.db")
cursor = con.cursor()
records = cursor.execute("SELECT user_id, problem_id, epoch_second FROM submissions WHERE user_id = 'kemuniku' AND epoch_second >= 1680319000")
for user_id, problem_id, epoch_second in records:
    print(user_id, problem_id, epoch_second)
con.close()
