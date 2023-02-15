# 8. Același string.
# ● Salvează într-o variabilă și aﬁșează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, aﬁșează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '

coral = 'Coral is either the stupidest animal or the smartest rock'
rock1 = coral.index('rock') # index 53
print(rock1)
print(coral[:rock1]) # output: 'Coral is either the stupidest animal or the smartest '