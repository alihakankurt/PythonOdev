import sqlite3

def jaccard_similarity(txt1: str, txt2: str) -> float:
    set1 = set(txt1)
    set2 = set(txt2)
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)

def levenshtein(txt1: str, txt2: str) -> int:
    if not txt1:
        return len(txt2)

    if not txt2:
        return len(txt1)

    return min(
        levenshtein(txt1[:-1], txt2) + 1,
        levenshtein(txt1, txt2[:-1]) + 1,
        levenshtein(txt1[:-1], txt2[:-1]) + (txt1[-1] != txt2[-1])
    )

def wagner_fisher(txt1: str, txt2: str) -> int:
    n = len(txt1)
    m = len(txt2)
    current_row: list[int] = [y for y in range(m + 1)]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [i] + [0] * m
        for j in range(1, m + 1):
            add = previous_row[j] + 1
            delete = current_row[j - 1] + 1
            change = previous_row[j - 1] + (txt1[i - 1] != txt2[j - 1])
            current_row[j] = min(add, delete, change)

    return current_row[m]

if __name__ == "__main__":

    connection: sqlite3.Connection = sqlite3.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS Texts (Id INTEGER PRIMARY KEY, Content TEXT)')
    connection.commit()

    text1: str = input("Enter the first text: ")
    text2: str = input("Enter the second text: ")

    connection.execute('INSERT INTO Texts (Content) VALUES (?)', (text1,))
    connection.execute('INSERT INTO Texts (Content) VALUES (?)', (text2,))
    connection.commit()

    cursor: sqlite3.Cursor = connection.execute('SELECT * FROM Texts')
    rows: list = cursor.fetchall()[-2:]
    text1 = rows[0][1]
    text2 = rows[1][1]

    connection.close()

    jaccard_similarity_result: float = jaccard_similarity(text1, text2)
    levenshtein_result: int = levenshtein(text1, text2)
    wagner_fisher_result: int = wagner_fisher(text1, text2)

    result: str = f'Text 1: {text1}\n' \
                  f'Text 2: {text2}\n' \
                  f'Jaccard similarity: {jaccard_similarity_result}\n' \
                  f'Levenshtein distance: {levenshtein_result}\n' \
                  f'Wagner-Fisher distance: {wagner_fisher_result}'

    print(result)
    with open('result.txt', 'w') as file:
        file.write(result)
