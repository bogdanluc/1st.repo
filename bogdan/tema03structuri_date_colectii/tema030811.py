# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să aﬁșezi Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota {dict1["Ana"]}')
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')

#10. Dorel a făcut contestație și a primit 6
# ● Modiﬁcă nota lui Dorel în 6
# ● Printează nota după modiﬁcare

dict1["Dorel"] = 6
print(f'Dorel a facut contestatie iar nota finala e {dict1["Dorel"]}')
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop("Gigel")
print(dict1)

dict1.update({"Ionica": 9})
print(dict1)