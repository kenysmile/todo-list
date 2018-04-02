tu = (
    ('Tu', 'phamvantu', 'cau long'),
    ('Tuan','nguyentrongtuan', 'bong ban'),
    ('Nam', 'giangvannam', 'boi')
)

con = sqlite3.connect('tudz.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Pvt")
    cur.execute("CREATE TABLE Pvt(Ten Varchar(20) PRIMARY KEY , Hoten Varchar(20), work Varchar(20))")
    cur.executemany("INSERT INTO Pvt VALUES( ?, ?, ?)", tu)
