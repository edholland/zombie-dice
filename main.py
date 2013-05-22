#!/usr/bin/python

import argparse
import random
from itertools import takewhile, cycle

def main():
    """Main function
    
    Parses arguments, sets the game up and prints info about winner(s)
    """
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

class Dice:
    """ Implements a generic dice"""
    def __init__(self, brains):
        """Sets up dice

        Accepts number of positive results on dice
        """
        self.brains = brains
        self.runners = 2
        self.shotguns = 4 - self.brains
        if self.brains == 1:
            self.colour = 'Red'
        elif self.brains == 2:
            self.colour = 'Yellow'
        else:
            self.colour = 'Green'
        self.result = ''

    def roll(self):
        """Rolls a single dice

        Returns a result based on the probabilites when object created
        """
        roll = random.randint(1,6)
        if roll <= self.brains:
            self.result =  'brain'
        elif roll <= (self.brains + self.runners):
            self.result = 'runner'
        else:
            self.result = 'shotgun'
        return self.result
        
class Player:
    """Class to hold info about a player"""
    def __init__(self, name):
        """Sets up the player and creates a first set of dice"""
        self.name = name
        self.score = 0
        self.shotguns = 0        
        self.current_dice = []
        self.newDice()
    def newDice(self):
        """Produces a new set of dice"""
        red_dice = [ Dice(1) for x in range(4) ]
        yellow_dice = [ Dice(2) for x in range(5) ]
        green_dice = [ Dice(3) for x in range(4) ]
        self.dice = red_dice + yellow_dice + green_dice
        random.shuffle(self.dice)
    def printScore(self):
        """prints player name and current score"""
        print "Player: %s \t Score: %s" % (self.name, self.score)
    def inputScore(self):
        """unused method to allow manual input of scores"""
        self.score += int(raw_input("Enter score for %s: " % self.name))
        print
    def get_dice(self):
        """returns a set of three dice, only adds the number needed"""
        temp = []
        for i in  range(3-len(self.current_dice)):
            try:
                temp.append(self.dice.pop())
            except IndexError:
                break
        return  self.current_dice + temp
    def roll(self):
        """implements a round of rolling"""
        self.shotguns = 0
        score = 0
        self.newDice()
        while self.shotguns < 3:
            if raw_input('Total score: %d. Current score: %d. Current shotguns: %d. Do you wish to continue: ' % (self.score + score, score, self.shotguns) ) != 'y':
                break
            self.current_dice = self.get_dice()
            for di in self.current_dice:
                value = di.roll()
                if value == 'brain':
                    print 'NOM BRAIN'
                    score += 1
                elif value == 'shotgun':
                    print 'OUCH'
                    self.shotguns += 1
                elif value =='runner':
                    print 'RUUUUUUN'
            self.current_dice = [ x for x in self.current_dice if x.result == 'runner' ]
        if self.shotguns < 3:
            self.score += score
        return self.score

class Game:
    """class to define a game"""
    def __init__(self, players):
        """sets up game info vars"""
        self.players = players
        self.round = 0
        self.done = False
    def play(self):
        """loops over all the players until one reaches 13 then loop once more over the remaining players"""
        for player in takewhile(lambda p: p.score < 13, cycle(self.players)):
            player.printScore()
            player.roll()
        final =  max( [x.score for x in self.players ] )
        return [ x for x in self.players if x.score == final ]
main()
