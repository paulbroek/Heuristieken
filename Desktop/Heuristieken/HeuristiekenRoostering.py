
# Bob van den Hoogen
# Lectures and Lesroosters
# 13 - 04 - 2015
# Start of Heuristieken project
# Begin's with loading in the CSV-file

import csv
import math
import numpy as np
from array import array
from random import randint

AchternaamLijst = []
VoornaamLijst = []
StudentNumbers = []
Vak1 = []
Vak2 = []
Vak3 = []
Vak4 = []
Vak5 = []

with open('studenten_roostering.csv', 'rb') as csvfile:
    studentRoostering = csv.DictReader(csvfile)
    for row in studentRoostering:
        AchternaamLijst.append(row['Achternaam'])
        VoornaamLijst.append(row['Voornaam'])
        StudentNumbers.append(row['Stud.Nr.'])
        Vak1.append(row['Vak1'])
        Vak2.append(row['Vak2'])
        Vak3.append(row['Vak3'])
        Vak4.append(row['Vak4'])
        Vak5.append(row['Vak5'])

##with open('vak_roostering.csv', 'rb') as csvfile2:
##    vakRoostering = csv.DictReader(csvfile2)
    

vakken = ['Advanced Heuristics', 'Algoritmen en complexiteit', 'Analysemethoden en -technieken',
          'Architectuur en computerorganisatie', 'Autonomous Agents 2', 'Bioinformatica', 'Calculus 2',
          'Collectieve Intelligentie', 'Compilerbouw', 'Compilerbouw practicum', 'Data Mining',
          'Databases 2', 'Heuristieken 1', 'Heuristieken 2', 'Informatie- en organsatieontwerp',
          'Interactie-ontwerp', 'Kansrekenen 2', 'Lineaire Algebra', 'Machine Learning',
          'Moderne Databases', 'Netwerken en systeembeveiliging', 'Programmeren in Java 2',
          'Project Genetic Algorithms', 'Project Numerical Recipes', 'Reflectie op de digitale cultuur',
          'Software engineering', 'Technology for games', 'Webprogrammeren en databases',
          'Zoeken sturen en bewegen']

def NumberOfStudents(vak):
    number = 0
    for row in Vak1:
        if row == vak:
            number = number + 1
    for row in Vak2:
        if row == vak:
            number = number + 1
    for row in Vak3:
        if row == vak:
            number = number + 1
    for row in Vak4:
        if row == vak:
            number = number + 1
    for row in Vak5:
        if row == vak:
            number = number + 1
    return number

    

# Creates dictionary for number of student in a course
NumOfStudDict = {}

# Creates dictionary for studentnumbers in a course
StudNumList = {}


def StudentsNumbers(vak):
    lijstje = []
    for i in range(len(Vak1)):
        if Vak1[i] == vak:
            lijstje.append(StudentNumbers[i])
    return lijstje

for i in range(29):
    StudNumList[vakken[i]] = StudentsNumbers(vakken[i])
##    print vakken[i], StudNumList[vakken[i]], "\n"

    
StudDict = {}
for vak in vakken:
    NumOfStudDict[vak] = NumberOfStudents(vak)

CollegeIndeling = {}

class Colleges:
    def __init__(self, hc, wc, prac, name):
        self.hc = hc
        self.wc = wc
        self.prac = prac
        self.name = name
    def hoorcollege(self):
        if self.hc == 1:
            hoorcolleges.append(self.name +' hc')
            CollegeIndeling[self.name + ' hc'] = StudNumList[self.name]
        elif self.hc == 2:
            hoorcolleges.append(self.name +' 1hc')
            hoorcolleges.append(self.name +' 2hc')
            CollegeIndeling[self.name + ' 1hc'] = StudNumList[self.name]
            CollegeIndeling[self.name + ' 2hc'] = StudNumList[self.name]
        elif self.hc == 3:
            hoorcolleges.append(self.name +' 1hc')
            hoorcolleges.append(self.name +' 2hc')
            hoorcolleges.append(self.name +' 3hc')
            CollegeIndeling[self.name + ' 1hc'] = StudNumList[self.name]
            CollegeIndeling[self.name + ' 2hc'] = StudNumList[self.name]
            CollegeIndeling[self.name + ' 3hc'] = StudNumList[self.name]

    def werkcollege(self):
        NumberOfWC = math.ceil(NumOfStudDict[self.name] / PerWCDict[self.name])
        if self.wc == 1:
            if NumberOfWC == 1:
                werkcolleges.append(self.name + ' wc')
                CollegeIndeling[self.name + ' wc'] = StudNumList[self.name]
                AantalZalenWC.append(1)
            if NumberOfWC == 2:
                werkcolleges.append(self.name + ' 1wc')
                werkcolleges.append(self.name + ' 2wc')
                AantalZalenWC.append(2)
                CollegeIndeling[self.name + ' 1wc'] = StudNumList[self.name][0:len(StudNumList[self.name])/2]
                CollegeIndeling[self.name + ' 2wc'] = StudNumList[self.name][len(StudNumList[self.name])/2:len(StudNumList[self.name])]
            if NumberOfWC == 3:
                werkcolleges.append(self.name + ' 1wc')
                werkcolleges.append(self.name + ' 2wc')
                werkcolleges.append(self.name + ' 3wc')
                AantalZalenWC.append(3)
                CollegeIndeling[self.name + ' 1wc'] = StudNumList[self.name][0:len(StudNumList[self.name])/3]
                CollegeIndeling[self.name + ' 2wc'] = StudNumList[self.name][len(StudNumList[self.name])/3:2/3 * len(StudNumList[self.name])]
                CollegeIndeling[self.name + ' 3wc'] = StudNumList[self.name][len(StudNumList[self.name])* 2/3:len(StudNumList[self.name])]

    def practicum(self):
        NumberOfPRAC = math.ceil(NumOfStudDict[self.name] / PerPRACDict[self.name])
        if self.prac == 1:
            if NumberOfPRAC == 1:
                practica.append(self.name + ' prac')
                CollegeIndeling[self.name + ' prac'] = StudNumList[self.name]
            if NumberOfPRAC == 2:
                practica.append(self.name + ' 1prac')
                practica.append(self.name + ' 2prac')
                CollegeIndeling[self.name + ' 1prac'] = StudNumList[self.name][0:len(StudNumList[self.name])/2]
                CollegeIndeling[self.name + ' 2prac'] = StudNumList[self.name][len(StudNumList[self.name])/2:len(StudNumList[self.name])]
            if NumberOfPRAC == 3:
                practica.append(self.name + ' 1prac')
                practica.append(self.name + ' 2prac')
                practica.append(self.name + ' 3prac')
                CollegeIndeling[self.name + ' 1prac'] = StudNumList[self.name][0:len(StudNumList[self.name])/3]
                CollegeIndeling[self.name + ' 2prac'] = StudNumList[self.name][len(StudNumList[self.name])/3:2/3 * len(StudNumList[self.name])]
                CollegeIndeling[self.name + ' 3prac'] = StudNumList[self.name][len(StudNumList[self.name])* 2/3:len(StudNumList[self.name])]



# Makes dictionary from two lists.
def combine_lists(LIST1, LIST2):
    j = 0
    dictionary = dict()
    for i in LIST1:
        dictionary[i] = LIST2[j]
        j += 1
    return dictionary

AantalHC = [1, 1, 1, 2, 2, 3, 1, 3, 2, 0, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 2, 1, 2, 2, 0]
AantalWC = [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
AantalPRAC = [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1]
AantalZalenWC = []


# Maximum Amount of students per Werkcollege en practicum.
AantalPerWC = [0, 25, 0, 0, 10, 20, 40, 20, 40, 0, 10, 40, 25, 20, 15, 0, 0, 0, 0, 20, 0, 0, 0, 0, 20, 40, 20, 20, 0]
AantalPerPRAC = [10, 25, 0, 0, 10, 20, 0, 20, 40, 15, 10, 0, 0, 0, 15, 0, 0, 0, 0, 20, 20, 20, 15, 15, 0, 40, 0, 20, 15]

PerWCDict = combine_lists(vakken, AantalPerWC)
PerPRACDict = combine_lists(vakken, AantalPerPRAC)

hoorcolleges = []
werkcolleges = []
practica = []

# Adds all classes  to the new array.
for vak in range(len(vakken)):
    VakToevoegen = Colleges(AantalHC[vak], AantalWC[vak], AantalPRAC[vak], vakken[vak])
    VakToevoegen.hoorcollege()
    if AantalWC[vak] != 0:
        VakToevoegen.werkcollege()
    else:
        AantalZalenWC.append(0)
    if AantalPRAC[vak] != 0:
        VakToevoegen.practicum()


Classroom = ['A1.04','A1.06', 'A1.08', 'A1.10', 'B0.201', 'C0.110', 'C1.112']

Tijden = ['0900-1100', '1100-1300','1300-1500', '1500-1700']

Maandag = np.chararray((4, 7), itemsize = 50)
Dinsdag = np.chararray((4, 7), itemsize = 50)
Woensdag = np.chararray((4, 7), itemsize = 50)
Donderdag = np.chararray((4, 7), itemsize = 50)
Vrijdag = np.chararray((4, 7), itemsize = 50)

Maandag[:] = ''
Dinsdag[:] = ''
Woensdag[:] = ''
Donderdag[:] = ''
Vrijdag[:] = ''


Dagen = [Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag]


ClassroomCapacity = {'A1.04': 41, 'A1.06': 22, 'A1.08': 20, 'A1.10': 56, 'B0.201': 48, 'C0.110': 117, 'C1.112': 60}




#Inplannen geldig rooster 


TempPrac = []
TempHC = []
TempWC = []
Temp = []

def DetectCollision(vak):
    collisions = 0
    for dag in range(5):
        for i in range(4):
            collisions = 0
            for j in range(7):
                if (Dagen[dag])[i, j].startswith(vak):
                    collisions = collisions + 1
                    if collisions > 1:
                        Temp.append((Dagen[dag])[i,j])
                        (Dagen[dag])[i, j] = ''
                        return collisions, [dag, i]
    return collisions, [-1, -1]
                
# Colleges toevoegen aan rooster
def PlanColleges(colleges, omitTijdslot):
    vak = 0
    for dag in range(5):
        for tijdslot in range(4):
            for lokaal in range(7):
                if vak == len(colleges):
                    return
                
                for i in range(29):
                    if colleges[vak].startswith(vakken[i]):
                        if colleges[vak].endswith('hc'):
                            AantalStudenten = NumOfStudDict[vakken[i]]
                        elif colleges[vak].endswith('wc'):
                            AantalStudenten = PerWCDict[vakken[i]]
                        elif colleges[vak].endswith('prac'):
                            AantalStudenten = PerPRACDict[vakken[i]]
                        break
                    
                # Check for Capacity constraints
                while ClassroomCapacity[Classroom[lokaal]] < AantalStudenten:
                    if lokaal < 6:
                        lokaal = lokaal + 1
                    elif tijdslot < 3:
                        lokaal = 0
                        tijdslot = tijdslot + 1
                    elif dag < 5:
                        lokaal = 0
                        tijdslot = 0
                        dag = dag + 1

                # Check if need to be omitted
                if [dag, tijdslot] in omitTijdslot:
                    if tijdslot < 3:
                        lokaal = 0
                        tijdslot = tijdslot + 1
                    elif dag < 4:
                        lokaal = 0
                        tijdslot = 0
                        dag = dag + 1
                        
                if (Dagen[dag])[tijdslot, lokaal] == '':
                    (Dagen[dag])[tijdslot, lokaal] = colleges[vak]
                    vak = vak + 1

def PlanCollegesRandomly(colleges,omitTijdslot):
    vak = 0
    while vak != len(colleges):
        for i in range(len(vakken)):
            if colleges[vak].startswith(vakken[i]):
                if colleges[vak].endswith('hc'):
                    AantalStudenten = NumOfStudDict[vakken[i]]
                elif colleges[vak].endswith('wc'):
                    AantalStudenten = PerWCDict[vakken[i]]
                elif colleges[vak].endswith('prac'):
                    AantalStudenten = PerPRACDict[vakken[i]]
                break

        dag = randint(0,4)
        tijdslot = randint(0,3)
        lokaal = randint(0,6)
        if Dagen[dag][tijdslot, lokaal] == '' and ClassroomCapacity[Classroom[lokaal]] >= AantalStudenten:
            if [dag, tijdslot] not in omitTijdslot:
                (Dagen[dag])[tijdslot, lokaal] = colleges[vak]
                vak = vak + 1
    return
                


PlanCollegesRandomly(hoorcolleges, [-1, -1])
PlanCollegesRandomly(werkcolleges, [-1 ,-1])
PlanCollegesRandomly(practica, [-1, -1])

def PlanTemporary(omitTijdslot):
    PlanColleges(Temp, omitTijdslot)

# Solve Collisions in planning

for i in range(29):
    omitTijdslot = []
    collisions, [dag, tijdslot] = DetectCollision(vakken[i])
    omitTijdslot.append([dag, tijdslot])
    pogingen = 0
    PlanTemporary(omitTijdslot)
    TempHC = []
    TempWC = []
    TempPrac = []
    Temp = []
    while collisions > 1:
        PlanTemporary(omitTijdslot)
        TempHC = []
        TempWC = []
        TempPrac = []
        Temp = []
        collisions, [dag, tijdslot] = DetectCollision(vakken[i])
        omitTijdslot.append([dag, tijdslot])

        pogingen = pogingen + 1
        if pogingen % 10000 == 0:
            print pogingen, i

        



##for j in range(len(StudentNumbers)):
##    overlap = 0
##    for i in range(7):
##        if StudentNumbers[j] in CollegeIndeling[Maandag[1,i]]:
##            overlap = overlap + 1
##            if overlap > 1:
##                print overlap
##    if overlap > 1:
##        print StudentNumbers[j]
    
    
print 'Maandag: ', '\n', Maandag, '\n'
print 'Dinsdag: ', '\n', Dinsdag, '\n'
print 'Woensdag: ', '\n', Woensdag, '\n'
print 'Donderdag: ', '\n', Donderdag, '\n'
print 'Vrijdag: ', '\n', Vrijdag, '\n'
##print CollegeIndeling


