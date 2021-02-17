# Author: Harriet Poe
# This program will generate a name using syllables.

import random

consonant_start_syllables = ["tor", "lyn", "belle", "can", "con", "dor", "ric",
                             "ton", "cal", "nia", "for", "ron", "rot", "ram",
                             "ham", "har", "not", "fil", "fol", "nor", "rom",
                             "roc", "cor", "court", "line", "lore", "lam", "lab",
                             "car", "cad", "dale", "dock", "rock", "rook", "mock",
                             "lock", "lack", "loch", "doom", "dig", "notch", "lan"]
vowel_start_syllables = ["ette", "arc", "anne", "elle", "ine", "ella", "irc", "ash",
                         "ate", "end", "ear", "ebb", "art", "arb", "arm", "all", "ell",
                         "inn", "inc", "ice", "ico", "ica", "ide", "ido", "ida", "ill",
                         "if", "ike", "iko", "ick", "ile", "ila", "ild", "ilm", "iln",
                         "ilo", "ima", "im", "imo", "otto", "ock", "on", "old", "ole",
                         "alm", "elm", "olm", "eck", "ode", "ade", "ale", "aim", "air"]

switch_choice = {
    1: consonant_start_syllables,
    2: vowel_start_syllables
}

# Number of syllables
name_len = random.randint(2, 6)
print("Name size: ", name_len)

for x in range(0, name_len):
    random_choice = random.randint(1, 2)

    rand_syllable_choice = random.randint(1, (len(switch_choice[random_choice]) - 1))

    if random_choice == 1:
        print(consonant_start_syllables[rand_syllable_choice], end="")
    elif random_choice == 2:
        print(vowel_start_syllables[rand_syllable_choice], end="")

