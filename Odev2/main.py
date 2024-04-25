from module import identify_me, analyze

if __name__ == "__main__":
    identify_me()

    txt: str = input("Please input text message: ")

    print("\nFrequency analysis of first 100 characters: ")
    analyze(txt[:100])

    if len(txt) > 100:
        print("\nFrequency analysis of first 1000 characters: ")
        analyze(txt[:1000])

    if len(txt) > 1000:
        print("\nFrequency analysis of first 10000 characters: ")
        analyze(txt[:10000])
