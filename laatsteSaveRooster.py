def SaveRooster(Dagen, naam):
    with open(naam, 'w') as excel:
        a = csv.writer(excel, delimiter=';', lineterminator='\n')

        data = [[' '] + Classroom]
        dagnamen = ['Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag']
        tijden = [
        ['0900-1100'],
        ['1100-1300'],
        ['1300-1500'],
        ['1500-1700']]
        overlapsom = sum(Overlap(CollegeIndeling,Dagen))
        bonusspreiding = BonusSpreiding(CollegeIndeling,Dagen)
        malusspreiding = MalusSpreiding(CollegeIndeling,Dagen)
        totaalscore = Score(CollegeIndeling,Dagen)
        
        for dag in range(5):
            data.append([dagnamen[dag]])
            for tijd in range(4):
                tijdslotregel = [tijden[tijd][0]] + Dagen[dag][tijd]
                data.append(tijdslotregel)
        data.append([''])
        data.append(['Beginscore','1000'])
        data.append(['MALUS unassigned',TotalUnassignedStudents])
        data.append(['Collisions',overlapsom])
        data.append(['Bonus spreiding',bonusspreiding])
        data.append(['Malus spreiding',malusspreiding])
        data.append(['Totaal',totaalscore])
        
        data.append([''])
        data.append(['BONUS Uitleg'])
        data.append(['Vak','Perfecte spreiding over # dagen'])
        for i in range(0,len(BonusUitleg)):
            data.append(BonusUitleg[i])
           
        data.append([''])
        data.append(['MALUS Uitleg'])
        data.append(['Vak','AantalActiviteiten - AantalDagen'])
        for i in range(0,len(MalusUitleg)):
            data.append(MalusUitleg[i])
        a.writerows(data)
