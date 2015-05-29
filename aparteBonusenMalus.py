def MalusSpreiding(CollegeIndeling,Dagen):
    # Aantal dagen en activiteiten per vak, relevant voor score
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
                    if Dagen[d][k][i] != [] and Dagen[d][k][i].startswith(vakken[v]):
                        vakopdag[d,v] = True
                        break
            if vakopdag[d,v]:
                AantalDagenPerVak[v] += 1                

    spreidingmalus = 0
    
    MalusUitleg[:] = []

    for v in range(29):
        if AantalDagenPerVak[v] < AantalActiviteitenPerVak[v]:
            spreidingmalus += 10*(AantalActiviteitenPerVak[v]-AantalDagenPerVak[v]) 
            MalusUitleg.append([vakken[v],AantalActiviteitenPerVak[v]-AantalDagenPerVak[v]])

    return spreidingmalus

def BonusSpreiding(CollegeIndeling,Dagen):
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
                    if Dagen[d][k][i] != [] and Dagen[d][k][i].startswith(vakken[v]):
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
                    if Dagen[d][k][i] != [] and Dagen[d][k][i].startswith(vakken[v]):
                        if Dagen[d][k][i].endswith('hc'):
                            hc_op_dag = True
                            aantal_hc_op_dag += 1
                        if Dagen[d][k][i].endswith('prac') or Dagen[d][k][i].endswith('wc'):
                            wc_of_prac_op_dag = True
            if (hc_op_dag and wc_of_prac_op_dag) or aantal_hc_op_dag > 1:
                hc_en_wc_of_prac_op_dag[d,v] = True
                slechte_spreiding[v] = True           

    # bonussectie: vak met 2 tot 4 activiteiten, voor 2: ma-do of di-vr, voor 3: ma-wo-vr, voor 4: ma,di,do,vr
    bonusspreiding = 0
    BonusPerVak = []
    BonusUitleg[:] = []
    for v in range(29):
        if not(slechte_spreiding[v]):
            # 2 activiteiten: ma-do of di-vr geeft bonus
            if AantalActiviteitenPerVak[v] == 2 and AantalDagenPerVak[v] == 2:
                if (vakopdag[0,v] and vakopdag[3,v]) or (vakopdag[1,v] and vakopdag[4,v]):
                    BonusPerVak.append(20)
                    BonusUitleg.append([vakken[v],2])
            # 3 activiteiten: ma-wo-vr
            if AantalActiviteitenPerVak[v] == 3 and AantalDagenPerVak[v] == 3:
                if vakopdag[0,v] and vakopdag[2,v] and vakopdag[4,v]:
                    BonusPerVak.append(20)
                    BonusUitleg.append([vakken[v],3])
            # 4 activiteiten: ma-di-do-vr
            if AantalActiviteitenPerVak[v] == 4 and AantalDagenPerVak[v] == 4:
                if vakopdag[0,v] and vakopdag[1,v] and vakopdag[3,v] and vakopdag[4,v]:
                    BonusPerVak.append(20)
                    BonusUitleg.append([vakken[v],4])
                    
    bonusspreiding = np.sum(BonusPerVak)
    return bonusspreiding

def ScoreUitleg(CollegeIndeling, Dagen):
    for d in range(5):
        for k in range(4):
            for i in range(7):
                try:
                    if Dagen[d][k][i] != []:
                        probleemVakken[Dagen[d][k][i]] = 0
                except IndexError:
                    continue
    
    overlap = Overlap(CollegeIndeling,Dagen)
    malusspreiding = MalusSpreiding(CollegeIndeling,Dagen)       
    bonusspreiding = BonusSpreiding(CollegeIndeling,Dagen)
    
    start = 1000
    print "Beginscore: ",start
    print "MALUS Unassigned students: ",TotalUnassignedStudents
    print "MALUS Student overlap: ",sum(overlap)
    print "MALUS Spreiding: ",malusspreiding
    print "BONUS Spreiding: ",bonusspreiding
    print "Eindscore: ",(start-sum(overlap)-malusspreiding+bonusspreiding-TotalUnassignedStudents)
    print ""
    print "BONUS Uitleg"
    for i in range(0,len(BonusUitleg)):
        print BonusUitleg[i]
    print "MALUS Uitleg"
    for i in range(0,len(MalusUitleg)):
        print MalusUitleg[i]
