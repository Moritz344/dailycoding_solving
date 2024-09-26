def choose_language(languages):
    # Zähle die Vorkommen jeder Sprache
    count = { 'D': 0, 'F': 0, 'I': 0, 'K': 0 }
    for lang in languages:
        count[lang] += 1
    # alle 3
    for lang in languages:
        if count[lang] == 3:
            return lang

    
    # alle 2

    for lang in count:
        if count[lang] == 2:
            for x in count:
                if count[x] == 1:
                    return x

    # alle diff

    for lang in count:
        if count[lang] == 0:
            return lang




# Beispielaufrufe
print(choose_language("FFF"))  # Ausgabe: F
print(choose_language("IIK"))  # Ausgabe: K
print(choose_language("DFK"))  # Ausgabe: I
