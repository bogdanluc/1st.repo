# Fiind dat un dictionar cu perechi {nume: nota}, sa se afle cine are cea mai mare nota.

catalog = {
    "Andrei": 8,
    "Ioana": 9,
    "Vlad": 5
}

maxim = None
om_maxim = None
for key in catalog:
    if maxim is None:
        maxim = catalog[key]
        om_maxim = key
    else:
        if catalog[key] > maxim:
            maxim = catalog[key]
            om_maxim = key
print(om_maxim, maxim)