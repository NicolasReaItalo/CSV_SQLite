import _sqlite3

def database_creation():
    con = _sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE projectInfo( titre TEXT, real TEXT, cinematographer TEXT )')
    cur.execute(
        "CREATE TABLE Clips(clipName TEXT, clipDuration TEXT, Scene TEXT, Shot TEXT, Take TEXT, Circled INTEGER, "
        "Watched INTEGER, Comment TEXT)")

def database_import_csv():
    con = _sqlite3.connect("test.db")
    cur = con.cursor()
    d =  ["Titre du film", "Réalisateur", "Chef-opérateur"]
    cur.execute("INSERT INTO ProjectInfo (titre, real, cinematographer) values (?,?,?)",d )
    con.commit()
    cur.close()

if __name__ == '__main__':
    database_import_csv()
