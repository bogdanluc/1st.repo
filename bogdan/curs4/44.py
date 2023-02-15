def afisare_elemente(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])


afisare_elemente(a=1, b=2, alt_parametru=True)