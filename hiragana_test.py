import os
import random
import time
import datetime


def clear():
    os.system('cls||clear')


alphabet_to_hiragana = {
    "a": "あ",
    "i": "い",
    "u": "う",
    "e": "え",
    "o": "お",

    "ka": "か",
    "ki": "き",
    "ku": "く",
    "ke": "け",
    "ko": "こ",

    "sa": "さ",
    "shi": "し",
    "su": "す",
    "se": "せ",
    "so": "そ",

    "ta": "た",
    "chi": "ち",
    "tsu": "つ",
    "te": "て",
    "to": "と",

    "na": "な",
    "ni": "に",
    "nu": "ぬ",
    "ne": "ね",
    "no": "の",

    "ha": "は",
    "hi": "ひ",
    "fu": "ふ",
    "he": "へ",
    "ho": "ほ",

    "ma": "ま",
    "mi": "み",
    "mu": "む",
    "me": "め",
    "mo": "も",

    'ya': 'や',
    'yu': 'ゆ',
    'yo': 'よ',

    "ra": "ら",
    "ri": "り",
    "ru": "る",
    "re": "れ",
    "ro": "ろ",

    "wa": "わ",
    "wi": "ゐ",
    "we": "ゑ",
    "wo": "を",

    "n": "ん",

    "ga": "が",
    "gi": "ぎ",
    "gu": "ぐ",
    "ge": "げ",
    "go": "ご",

    "gya": "ぎゃ",
    "gyu": "ぎゅ",
    "gyo": "ぎょ",

    "za": "ざ",
    "ji": "じ",
    "zu": "ず",
    "ze": "ぜ",
    "zo": "ぞ",

    "ja": "じゃ",
    "ju": "じゅ",
    "jo": "じょ",

    "da": "だ",
    "2ji": "ぢ",  # uncommon and the same as ず
    "2zu": "づ",  # uncommon and the same as ぜ
    "de": "で",
    "do": "ど",

    "2ja": "ぢゃ",  # uncommon and the same as じゃ
    "2ju": "ぢゅ",  # uncommon and the same as じゅ
    "2jo": "ぢょ",  # uncommon and the same as じょ

    "ba": "ば",
    "bi": "び",
    "bu": "ぶ",
    "be": "べ",
    "bo": "ぼ",

    "bya": "びゃ",
    "byu": "びゅ",
    "byo": "びょ",

    "pa": "ぱ",
    "pi": "ぴ",
    "pu": "ぷ",
    "pe": "ぺ",
    "po": "ぽ",

    "pya": "ぴゃ",
    "pyu": "ぴゅ",
    "pyo": "ぴょ",
}


alphabet_to_hiragana_keys = list(alphabet_to_hiragana)

if __name__ == "__main__":
    tstart = datetime.datetime.now()
    for num_answered in range(0, 50):
        clear()
        alphabet_key = random.choice(alphabet_to_hiragana_keys)
        hiragana = alphabet_to_hiragana[alphabet_key]
        print(
            "answered " +
            str(num_answered) +
            "\n\n", hiragana, "\n")
        answer = input('English: ')
        if answer == "quit":
            break
        if answer != alphabet_key:
            print("\n"+"Wrong, the answer is:\n"+alphabet_key)
            time.sleep(5)
        else:
            print("\nCorrect")
            time.sleep(.25)

    tend = datetime.datetime.now()
    print('you scored', tend - tstart)
