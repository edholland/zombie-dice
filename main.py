#!/usr/bin/python

import argparse
from itertools import takewhile, cycle

def main():
    parser = argparse.ArgumentParser(description='Score counter for zombie dice')
    parser.add_argument('-p', help='Names of all players', nargs='+')
    opts = parser.parse_args()
    print "Start of game"
    players = [ Player(x) for x in opts.p]
    game = Game(players)
    game.play()
    print "Final Scores:"
    [ x.printScore() for x in players ]
    top_score = max( [ x.score for x in players ] )
    winners = [ x for x in players if x.score == top_score ]
    if len(winners) == 1:
        print "The winner is %s" % each.name
    else:
        print "The winners are: "
        for each in winners:
            print each.name
            
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def printScore(self):
        print "Player: %s \t Score: %s" % (self.name, self.score)
    def inputScore(self):
        self.score += int(raw_input("Enter score for %s: " % self.name))
        print
    def roll(self):
        self.inputScore()
        self.printScore()
        
class Game:
    def __init__(self, players):
        self.players = players
        self.round = 0
        self.done = False
    def play(self):
        for player in takewhile(lambda p: p.score < 13, cycle(self.players)):
            player.roll()

main()
