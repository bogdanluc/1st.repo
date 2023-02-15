from oop.cont_bancar import ContBancar

cont1 = ContBancar('bogdan l', 'ro001')
cont2 = ContBancar('Adelina l', 'ro002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(790)

cont1.plataCard(400)
cont2.plataCard(300)
cont2.plataCard(50)
cont2.plataCard(37)


cont1.interogareSold()
cont2.interogareSold()

#tema
#calsa angajat
#nume, prenume, salariu vechime
#coinstructor = nume, prenume, salariu, vechime
#metode
#descriere
#marire salariu in functie de vechime
#actualizare vechime
    #self.vechime = noua vechime
#sub 3 ani marire - 300, peste 3 ani 500
