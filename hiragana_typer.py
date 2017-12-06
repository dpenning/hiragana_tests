from hiragana_test import alphabet_to_hiragana


def translate_to_hiragana(transliteration):
    syllable = ""
    hiragana = ""
    for index, letter in enumerate(transliteration):
        syllable += letter
        if (
            syllable in alphabet_to_hiragana and (
                letter != "n" or index == len(transliteration) - 1 or
                transliteration[index + 1] not in ['a', 'e', 'i', 'o', 'u'])):
            hiragana += alphabet_to_hiragana[syllable]
            syllable = ""
    return hiragana


if __name__ == "__main__":
    while True:
        print(translate_to_hiragana(input("english transliteration:\n")))
