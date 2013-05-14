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
    winners = game.play()
    
    print
    print
    print "Winner%s: %s" % ("s"[len(winners)==1:], ', '.join([ x.name for x in winners ]))
    print "Final Scores:"
    [ x.printScore() for x in players ]

            
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
        final =  max( [x.score for x in self.players ] )
        return [ x for x in self.players if x.score == final ]
main()
