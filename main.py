zakupy={
    "piekarnia":["chleb", "bułki", "pączki"],
    "warzywniak":["marchew", "seler", "rukola"]
}
sets_sum=sum(len(wartosci) for wartosci in zakupy.values())
for nazwa, (wartosc) in zakupy.items():
    nazwa_capitalized=nazwa.capitalize()
    wartosc_capitalized=tuple(wartosc.capitalize() for wartosc in wartosc)
    print(f"Idę do {nazwa_capitalized}, kupiuję tu następujące rzeczy:{wartosc_capitalized}")
print(f"W sumie kupuję {sets_sum} produktów")

