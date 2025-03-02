zakupy={
    "piekarnia":["chleb", "bułki", "pączki"],
    "warzywniak":["marchew", "seler", "rukola"]
}
sets_sum=sum(len(wartosci) for wartosci in zakupy.values())
for nazwa, (wartosc) in zakupy.items():
    print(f"Idę do {nazwa}, kupiuję tu następujące rzeczy:{wartosc}")
