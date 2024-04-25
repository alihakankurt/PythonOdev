def identify_me() -> None:
    print("Id: 211213090")
    print("FirstName: Ali Hakan")
    print("LastName: Kurt")
    print("Note: My foot is broken!")

def is_space(c: str) -> str:
    v: int = ord(c)
    return v <= 32

def to_lower(c: str) -> str:
    v: int = ord(c)
    if v >= 65 and v <= 90:
        return chr(v + 32)
    return c

def count_frequency(txt: str) -> dict[str, int]:
    frequency: dict[str, int] = {}

    for letter in txt:
        if is_space(letter):
            continue

        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    return dict(sorted(frequency.items(), key=lambda item: item[0]))

def analyze(txt: str) -> None:
    frequency: dict[str, int] = count_frequency(txt)
    totalLetters: int = sum(frequency.values())

    for (letter, count) in frequency.items():
        print(f"'{letter}' -> Number of Usings: {count:,}, Using Rate: {count / totalLetters:.5f}")
