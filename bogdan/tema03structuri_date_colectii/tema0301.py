# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Aﬁșeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.


note = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note)
note = note[::-1]
print(note)
note.reverse()
print(note)

# 2. De câte ori apare ‘do’?
print(note.count("do"))