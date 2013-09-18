from API import *
from skills import *

class Hackathon():
	def __init__(self, hackers = [], food = [], prizes = []):
		self.hackers = hackers
		self.food = food
		self.prizes = prizes

	def brainstorm(self):
		self.ideas = self.hackers.random()

	def implement(self, team):
		self.ideas = self.hackers.random()

	def support(self, experts):
		experts.help(self.hackers)

	def demo(self, team, audience):
		team.showNTell()
		audience.applause()
		self.hackers.emjoy()
		self.hackers.win(self,prizes)

if __name__== "__main__":
	BGHackathon = new Hackathon([you, me, geekettes],
		[fruits, healthyStuff], [iPads, coolPrizes])
	BGHackathon.brainstorm()
	BGHackathon.support(geekettes)
	for team in allTeams:
		BGHackathon.implement(team)
		BGHackathon.demo(team, audience)
		