#!/usr/bin/python

import argparse

def get_scores(players):
    scores = []
    for player in players:
        scores.append(int(player.score))
    return scores
def main():
    parser = argparse.ArgumentParser(description='Score counter for zombie dice')
    parser.add_argument('-p', help='Names of all players', nargs='+')
    opts = parser.parse_args()
    print "Start of game"
    players = []
    for opt in opts.p:
        players.append(Player(opt))
    round = 0
    while max(get_scores(players)) < 13:
        round =+ 1
        print "Round: %d" % round
        for player in players:
            player.getScore()
            player.printScore()        
    print "FINAL ROUND:"
    
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def printScore(self):
        print "Player: %s \t Score: %s" % (self.name, self.score)
    def getScore(self):
        self.score += int(raw_input("Enter score for %s" % self.name))
main()
