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
