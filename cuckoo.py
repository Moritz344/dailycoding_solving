def cuckoo_time(initial_time, n):
    # Hilfsfunktion, um die Zeit in Minuten zu konvertieren
    def time_to_minutes(time):
        hh, mm = map(int, time.split(':'))
        return hh * 60 + mm

    # Hilfsfunktion, um die Minuten in das HH:MM-Format zurückzukonvertieren
    def minutes_to_time(minutes):
        hh = (minutes // 60) % 12
        mm = minutes % 60
        return f"{hh if hh > 0 else 12:02}:{mm:02}"

    # Startzeit in Minuten umwandeln
    current_time = time_to_minutes(initial_time)
    chimes_count = 0

    while chimes_count < n:
        # Berechne die nächsten Schläge
        for minute in [0, 15, 30, 45]:
            next_time = (current_time // 60) * 60 + minute
            if next_time < current_time:
                next_time += 60  # Nächste Stunde

            # Berechne die Anzahl der Schläge
            hour = (next_time // 60) % 12
            if hour == 0:
                hour = 12
            if next_time % 60 == 0:
                chimes = hour  # volle Stunde
            else:
                chimes = 1  # viertel, halb oder dreiviertel Stunde

            chimes_count += chimes

            if chimes_count >= n:
                return minutes_to_time(next_time)

            current_time = next_time

# Beispielaufrufe
print(cuckoo_time("07:22", 1))   # Beispiel 1
print(cuckoo_time("12:22", 2))   # Beispiel 2
print(cuckoo_time("01:30", 2))   # Beispiel 3
print(cuckoo_time("04:01", 10))  # Beispiel 4
print(cuckoo_time("03:38", 19))  # Beispiel 5

