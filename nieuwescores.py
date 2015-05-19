def Score(CollegeIndeling, Dagen):
    
    aantalvakkencontrole = []
    aantalvakkenperstudent = []
    overlap = []
    overlapreason = []

    for j in range(len(StudentNumbers)):
        aantalvakkenperstudent.append(0)
        overlap.append(0)
        # per tijdslot alle lokalen langs, als een student in meer dan 1 lokaal zit is er overlap
        for d in range(5):
            for k in range(4):
                overlaptemp = 0
                ##overlapreasontemp = "" 
                for i in range(7):
                    if (Dagen[d])[k,i] != '':
                        if StudentNumbers[j] in CollegeIndeling[(Dagen[d])[k,i]]:
                            overlaptemp += 1 
                if overlaptemp > 1:
                    overlap[j] += 1                
               
    # dagen per vak, relevant voor score
    AantalActiviteitenPerVak = []
    AantalDagenPerVak = []
    for v in range(29):
        AantalActiviteitenPerVak.append(AantalWC[v] + AantalHC[v] + AantalPRAC[v])
     
    vakopdag = np.ones((5,29),dtype=bool)

    for v in range(29):
        AantalDagenPerVak.append(0)
        for d in range(5):
            vakopdag[d,v] = False
            for k in range(4):
                for i in range(7):
                    if (Dagen[d])[k,i].startswith(vakken[v]):
                        vakopdag[d,v] = True
                        break
            if vakopdag[d,v]:
                AantalDagenPerVak[v] += 1
                
    hc_en_wc_of_prac_op_dag = np.ones((5,29),dtype=bool)
    slechte_spreiding = np.ones((29),dtype=bool)
    
    for v in range(29):
        slechte_spreiding[v] = False
        for d in range(5):
            hc_op_dag = False
            aantal_hc_op_dag = 0
            wc_of_prac_op_dag = False
            hc_en_wc_of_prac_op_dag[d,v] = False
            for k in range(4):
                for i in range(7):
                    if (Dagen[d])[k,i].startswith(vakken[v]):
                        if (Dagen[d])[k,i].endswith('hc'):
                            hc_op_dag = True
                            aantal_hc_op_dag += 1
                        if (Dagen[d])[k,i].endswith('prac') or (Dagen[d])[k,i].endswith('wc'):
                            wc_of_prac_op_dag = True
            if (hc_op_dag and wc_of_prac_op_dag) or aantal_hc_op_dag > 1:
                hc_en_wc_of_prac_op_dag[d,v] = True
                slechte_spreiding[v] = True

    # spreidingmalus
    spreidingmalus = 0
    for v in range(29):
        if AantalDagenPerVak[v] < AantalActiviteitenPerVak[v]:
            spreidingmalus += 10*(AantalActiviteitenPerVak[v]-AantalDagenPerVak[v])            

    # bonussectie: vak met 2 tot 4 activiteiten, voor 2: ma-do of di-vr, voor 3: ma-wo-vr, voor 4: ma,di,do,vr
    bonusspreiding = 0
    BonusPerVak = []
    for v in range(29):
        if not(slechte_spreiding[v]):
            # 2 activiteiten: ma-do of di-vr geeft bonus
            if AantalActiviteitenPerVak[v] == 2 and AantalDagenPerVak[v] == 2:
                if (vakopdag[0,v] and vakopdag[3,v]) or (vakopdag[1,v] and vakopdag[4,v]):
                    BonusPerVak.append(20)
            # 3 activiteiten: ma-wo-vr
            if AantalActiviteitenPerVak[v] == 3 and AantalDagenPerVak[v] == 3:
                if vakopdag[0,v] and vakopdag[2,v] and vakopdag[4,v]:
                    BonusPerVak.append(20)
            # 4 activiteiten: ma-di-do-vr
            if AantalActiviteitenPerVak[v] == 4 and AantalDagenPerVak[v] == 4:
                if vakopdag[0,v] and vakopdag[1,v] and vakopdag[3,v] and vakopdag[4,v]:
                    BonusPerVak.append(20)
                
    bonusspreiding = np.sum(BonusPerVak)
    start = 1000
    return (start-np.sum(overlap)-spreidingmalus+bonusspreiding)
    
def ScoreUitleg(CollegeIndeling, Dagen):
    aantalvakkencontrole = []
    aantalvakkenperstudent = []
    overlap = []
    overlapreason = []

    for j in range(len(StudentNumbers)):
        aantalvakkenperstudent.append(0)
        overlap.append(0)
        # per tijdslot alle lokalen langs, als een student in meer dan 1 lokaal zit is er overlap
        for d in range(5):
            for k in range(4):
                overlaptemp = 0
                ##overlapreasontemp = "" 
                for i in range(7):
                    if (Dagen[d])[k,i] != '':
                        if StudentNumbers[j] in CollegeIndeling[(Dagen[d])[k,i]]:
                            overlaptemp += 1 
                if overlaptemp > 1:
                    overlap[j] += 1
                
               
    # dagen per vak, relevant voor score
    AantalActiviteitenPerVak = []
    AantalDagenPerVak = []
    for v in range(29):
        AantalActiviteitenPerVak.append(AantalWC[v] + AantalHC[v] + AantalPRAC[v])
     
    vakopdag = np.ones((5,29),dtype=bool)

    for v in range(29):
        AantalDagenPerVak.append(0)
        for d in range(5):
            vakopdag[d,v] = False
            for k in range(4):
                for i in range(7):
                    if (Dagen[d])[k,i].startswith(vakken[v]):
                        vakopdag[d,v] = True
                        break
            if vakopdag[d,v]:
                AantalDagenPerVak[v] += 1
                
    hc_en_wc_of_prac_op_dag = np.ones((5,29),dtype=bool)
    slechte_spreiding = np.ones((29),dtype=bool)
    
    for v in range(29):
        slechte_spreiding[v] = False
        for d in range(5):
            hc_op_dag = False
            aantal_hc_op_dag = 0
            wc_of_prac_op_dag = False
            hc_en_wc_of_prac_op_dag[d,v] = False
            for k in range(4):
                for i in range(7):
                    if (Dagen[d])[k,i].startswith(vakken[v]):
                        if (Dagen[d])[k,i].endswith('hc'):
                            hc_op_dag = True
                            aantal_hc_op_dag += 1
                        if (Dagen[d])[k,i].endswith('prac') or (Dagen[d])[k,i].endswith('wc'):
                            wc_of_prac_op_dag = True
            if (hc_op_dag and wc_of_prac_op_dag) or aantal_hc_op_dag > 1:
                hc_en_wc_of_prac_op_dag[d,v] = True
                slechte_spreiding[v] = True

    # spreidingmalus
    spreidingmalus = 0
    for v in range(29):
        if AantalDagenPerVak[v] < AantalActiviteitenPerVak[v]:
            spreidingmalus += 10*(AantalActiviteitenPerVak[v]-AantalDagenPerVak[v])

    # bonussectie: vak met 2 tot 4 activiteiten, voor 2: ma-do of di-vr, voor 3: ma-wo-vr, voor 4: ma,di,do,vr
    bonusspreiding = 0
    BonusPerVak = []
    for v in range(29):
        if not(slechte_spreiding[v]):
            # 2 activiteiten: ma-do of di-vr geeft bonus
            if AantalActiviteitenPerVak[v] == 2 and AantalDagenPerVak[v] == 2:
                if (vakopdag[0,v] and vakopdag[3,v]) or (vakopdag[1,v] and vakopdag[4,v]):
                    print vakken[v]
                    BonusPerVak.append(20)
            # 3 activiteiten: ma-wo-vr
            if AantalActiviteitenPerVak[v] == 3 and AantalDagenPerVak[v] == 3:
                if vakopdag[0,v] and vakopdag[2,v] and vakopdag[4,v]:
                    print vakken[v]
                    BonusPerVak.append(20)
            # 4 activiteiten: ma-di-do-vr
            if AantalActiviteitenPerVak[v] == 4 and AantalDagenPerVak[v] == 4:
                if vakopdag[0,v] and vakopdag[1,v] and vakopdag[3,v] and vakopdag[4,v]:
                    print vakken[v]
                    BonusPerVak.append(20)
    
    print "Bonus per vak: ",BonusPerVak
    bonusspreiding = np.sum(BonusPerVak)
    
    start = 1000
    print "Beginscore: ",start
    print "MALUS Student overlap: ",np.sum(overlap)
    print "MALUS Spreiding: ",spreidingmalus
    print "BONUS Spreiding: ",bonusspreiding
    print "Eindscore: ",(start-np.sum(overlap)-spreidingmalus+bonusspreiding)

def SaveRooster(Dagen):
    with open('test.csv', 'w') as excel:
        a = csv.writer(excel, delimiter=';', lineterminator='\n')

        data = [[' '] + Classroom]
        dagnamen = ['Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag']
        tijden = [
        ['0900-1100'],
        ['1100-1300'],
        ['1300-1500'],
        ['1500-1700']]
        
        for dag in range(5):
            data.append([dagnamen[dag]])
            for tijd in range(4):
                tijdslotregel = [tijden[tijd][0]] + Dagen[dag][tijd].tolist()
                data.append(tijdslotregel)

        a.writerows(data)       
  
def EmptyDagen(Dagen):
    Maandag[:] = ''
    Dinsdag[:] = ''
    Woensdag[:] = ''
    Donderdag[:] = ''
    Vrijdag[:] = ''
    Dagen = [Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag]
