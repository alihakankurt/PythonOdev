def analyze(txt: str) -> None:
    frequency: dict[str, int] = {}
    for letter in txt:
        if letter.isspace():
            continue

        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    totalLetters: int = sum(frequency.values())

    for (letter, count) in sorted(frequency.items(), key=lambda item: item[0]):
        print(f"'{letter}' -> Number of Usings: {count:,}, Using Rate: {count / totalLetters:.5f}")

if __name__ == "__main__":
    txt: str = input("Please input text message: ")

    print("\nFrequency analysis of first 100 characters: ")
    analyze(txt[:100])

    if len(txt) > 100:
        print("\nFrequency analysis of first 1000 characters: ")
        analyze(txt[:1000])

    if len(txt) > 1000:
        print("\nFrequency analysis of first 10000 characters: ")
        analyze(txt[:10000])
