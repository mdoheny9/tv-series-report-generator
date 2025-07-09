import sys
import psycopg2

def main():
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 ./series.py 'Series Name'")
        sys.exit(1)

    print("enter username: ", file=sys.stderr, end = "")
    db_user = input()
    print("enter password: ", file=sys.stderr, end = "")
    db_password = input()


    DB_NAME = "imdb"
    DB_USER = db_user
    DB_PASS = db_password
    DB_HOST = "studentdb.csc.uvic.ca"
    DB_PORT = "5432"

    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
    except:
        print("Database not connected successfully")

    series_name = sys.argv[1]

    cur = conn.cursor()
    cur.execute("select * from user0179_series(%s)", (series_name,))
    rows1 = cur.fetchall()

    if len(rows1) != 1 or rows1[0][0] is None:
        print("Multiple or no series found with the same name, please enter a different name.", file=sys.stdout)
        sys.exit(2)

    cur.execute("select * from user0179_episodes(%s)", (series_name,))
    rows2 = cur.fetchall()

    # Output HTML to console
    result = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{series_name} - Series Info</title>
        <link rel="stylesheet" href="style2.css">
    </head>
    <body>
        <p>Series: {series_name}</p>
        <p>Year: {rows1[0][1]}</p>
        <p>Number of Seasons: {rows1[0][2]}</p>
        <p>Number of Episodes: {rows1[0][3]}</p>
        <p>Runtime: {rows1[0][4]}</p>
        <p>Rating: {rows1[0][5]}</p>
        <p>Votes: {rows1[0][6]}</p>

    <table>
        <tr>
            <th>Season</th>
            <th>Year</th>
            <th>Episodes</th>
            <th>Avg. Votes</th>
            <th>Avg. Rating</th>
            <th>Difference</th>
        </tr>\n"""
    
    for j in range(len(rows2)):
        result += """<tr> \n"""
        for i in range(len(rows2[0])):
            result += f"        <td>{rows2[j][i]}</td>\n"
        result += """</tr>"""

    result += """
    </table>
    </body>
    </html>"""
    print(result)
    conn.close()
    sys.exit()


if __name__ == "__main__":
    main()