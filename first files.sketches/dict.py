# declaram si initializam un dictionary (map)

note_elevi = {'gigel': 10, 'costel': 9, 'ana':10}
print(note_elevi)

#adaugam elemente
note_elevi['sebi'] = 7

#printam dictul
print(note_elevi)

#aflam elemente
print(note_elevi['gigel'])
print(note_elevi.get('gigel'))

# actualizam note
note_elevi['sebi'] = 10
print(note_elevi)

#aflam dimensiunea
print(note_elevi.__len__())
print(len(note_elevi))

#stergem valori
note_elevi.pop('gigel')
print(note_elevi.get('gigel', 'nu mai avem acest elev'))

print(note_elevi.keys())
print(note_elevi.values())