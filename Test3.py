"""
Simulador de resultados de futbol
"""

from random import randint #Esto lo vemos despues

def getScore(): #Genera marcadores aleatoriamente (rango entre 0 y 5)
    localScore = randint(0,5)
    visitScore = randint(0,5)

    return {"homeScore":localScore,"visitScore":visitScore} #Diccionario de datos


def showMatches(matchList): #Muestra lista de partidos con sus marcadores
    for match in matchList:
        print(f"{match['home']} vs {match['away']}: {match['homeGoals']} - {match['visitGoals']}")

def main():
    counter = 0
    matches = [] #Lista en blanco
    while(counter < 4):
        localTeam = input('Ingrese el equipo local ')
        visitTeam = input('Ingrese el equipo de visita ')

        matchScore = getScore()
        match = {"home":localTeam,"away":visitTeam,"homeGoals":matchScore["homeScore"],"visitGoals":matchScore["visitScore"]}
        matches.append(match)
        counter +=1
    showMatches(matches)

if __name__ == "__main__":
    main()
