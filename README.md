# TV Series Report Generator 🎬

A command-line Python program that generates a HTML report for a user-input TV series based off of information from the PostgreSQL IMDB database. Built using `psycopg2`, the program follows best practices for input handling and SQL query security. 

Developed as a project for **CSC370 (Database Systems)** at UVic. 

## How it works:

- Connects to a PostgreSQL database via `psycopg2`

- Accepts a TV series title as a command-line argument

- Prompts user securely for username and password (via `stderr`)

- Uses only pre-defined user-defined functions

- Prevents SQL injection using parameterized queries

## Usage:

run the program with:
```bash
python3 ./series.py '<series-name>' > output.html
```

### Example:
```bash
python3 ./series.py 'Young Sheldon' > output.html
```

The above command will generate an HTML report in output.html like the one displayed below.

![Screenshot of Young Sheldon HTML report](https://github.com/user-attachments/assets/61d942a1-edee-4c5f-93a0-efac24bf8bcb)
