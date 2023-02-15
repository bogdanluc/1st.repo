# 2. Fiind dat un timp masurat in secunde (ex. timp=3689), sa se scrie o functie care
# returneaza un string format din zile, ore, minute, secunde (ex. 0z, 1h 1min 29s).

def timp_secunde(secunde):
    z = ((secunde // 3600) // 24) % 30
    h = (secunde // 3600)
    m = (secunde % 3600) // 60
    s = (secunde % 3600) % 60
    return (f'{z}z, {h}h, {m}m, {s}s')


print(timp_secunde(66400))
