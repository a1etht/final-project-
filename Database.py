import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    student_id TEXT,
    major TEXT,
    hometown TEXT,
    gpa REAL,
    credits INTEGER,
    email TEXT
)''')

students = [
    ('Jay Sherm', '445774', 'Biochemistry', 'Houston, TX', 3.8, 14, 'jaysherm@gmail.com'),
    ("Emily Nguyen", "5915012", "Biological Sciences", "St. Paul, MN", 3.8, 14, "Watermelons678782@gmail.com"),
    ("Elijah Budd", "01716233", "Marine Biology", "Forest Lake, MN", 3.9, 16, "eabudd@students.unwsp.edu"),
    ("Alethea Lo", "01711463", "Computer Science", "Cottage Grove, MN", 3.9, 19, "aylo@students.unwsp.edu"),
    ("Genevie Lo", "3782936182", "Computer Science", "Cottage Grove, MN", 3.95, 6, "genylo@gmail.com"),
    ("Sophia Le", "8271528828", "Zoology", "Woodbury, Minnesota", 4.0, 20, "sophiale499@gmail.com"),
    ("Matt Anderson", "01710828", "Undecided", "White Bear Lake, Minnesota", 3.2, 12, "mranderson4@students.unwsp.edu"),

]

c.executemany("INSERT INTO students (name, student_id, major, hometown, gpa, credits, email) VALUES (?, ?, ?, ?, ?, ?, ?)", students)

conn.commit()   # ✅ this saves changes
conn.close()    # ✅ this closes the file and writes it

