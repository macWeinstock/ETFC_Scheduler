#Basic scheduler program for Eugene Timbers Little Timbers Program to randomize teams week by week without repeating
#Current usage: python3 ETFC_Scheduler.py
#Author: Mac Weinstock

import sys

def rotatePol(teamList):
	last = teamList.pop()
	return [last] + teamList

def createWeek(teamList):
	
	for i in range(len(teamList) // 2):
		print(f"Team {teamList[i]} vs. Team {teamList[-1 * (i + 1)]}")

	return teamList[i+1]

def fillSched(numTeams):

	teamList = [x+1 for x in range(numTeams)]

	lastOpp = "Bye"
	if len(teamList) % 2 == 0:
		lastOpp = teamList.pop()

	for i in range(len(teamList)):
		print(f"Week {i + 1}:")
		lastTeam = createWeek(teamList)
		print(f"Team {lastTeam} vs. Team {lastOpp}")
		teamList = rotatePol(teamList)

def main():
	print("Enter number of teams: ")
	numTeams = int(sys.stdin.readline())

	fillSched(numTeams)

if __name__ == '__main__':
	main()
