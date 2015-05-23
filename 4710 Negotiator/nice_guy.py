__author__ = 'Michael'
__author__ = 'Michael'
from negotiator_base import BaseNegotiator
from functools import reduce
from random import randint


# Important things to note: We always set self.offer to be equal to whatever
# we eventually pick as our offer. This is necessary for utility computation.
# Second, note that we ensure that we never accept an offer of "None".
class NiceGuy(BaseNegotiator):

    def __init__(self):
        self.preferences = [] #our given preferences
        self.offer = [] #the current offer given to us
        self.exchange_counter = 0
        self.upper_threshold = 0 #the threshold before we consider accepting an offer when we are in a position of power
        self.lower_threshold = 0 #the threshold where we are just trying to minimize loss
        self.dick_counter = 0 #a measure of how stubborn the opposition is
        self.list_of_opponent_negotiation_utilities = []
        self.list_of_opponent_offers = [] #the utility of the opponent from the last offer they made
        self.round = 1
        self.successful_dick = False #a trigger for if being stubborn ourselves is beneficial
        self.wins = 0 #how many rounds have we won
        self.a = False
        self.past_offers = []

    # initialize(self : BaseNegotiator, preferences : list(String), iter_limit : Int)
        # Performs per-round initialization - takes in a list of items, ordered by the item's
        # preferability for this negotiator
        # You can do other work here, but still need to store the preferences
    def initialize(self, preferences, iter_limit):
        self.preferences = preferences[:]
        self.iter_limit = iter_limit
        self.offer = self.preferences[:] #temporary to calculate the full points possible
        self.full_points = self.utility() #calculate the full points possible
        self.offer = []
        self.upper_threshold = self.full_points / 2
        # self.upper_threshold = self.full_points * 3 / 5
        self.lower_threshold = 0 - len(self.preferences)
        self.random_round = randint(5,10)

    # make_offer(self : BaseNegotiator, offer : list(String)) --> list(String)
        # Given the opposing negotiator's last offer (represented as an ordered list),
        # return a new offer. If you wish to accept an offer & end negotiations, return the same offer
        # Note: Store a copy of whatever offer you make in self.offer at the end of this method.
    def make_offer(self, offer):
        self.exchange_counter += 1
        if offer:
            self.list_of_opponent_offers.append(offer)
            similar = self.dick_offer_checker(offer)
            if similar:
                self.dick_counter += 1
            else:
                self.dick_counter -= 1
            self.offer = offer[:]
            u = self.utility()

# ---------------- tell them to fuck off if lose more than fail negotiation penalty ----
            if u <= self.lower_threshold:
                self.offer = self.preferences[:]
                return self.offer

# ---------------- accept on last -------
            if self.exchange_counter >= 10:
                self.offer = offer[:]
                return self.offer

# ---------------- if first exchange or past dick move was successful
            if self.round == 1 or self.successful_dick:
                if self.dick_counter < 3:
                    if u >= self.upper_threshold:
                        return offer
                    else:
                        if self.exchange_counter == 1:
                            self.offer = self.preferences[:]
                            return self.offer
                        else:
                            if self.exchange_counter >= 5:
                                self.upper_threshold -= self.full_points/20 # TODO: TWEAK
                            self.offer = self.scramble() #makes it slightly trickier to read our offers
                            return self.offer
                elif self.dick_counter >= 3:
                    self.upper_threshold -= self.full_points/20 # TODO: TWEAK
                    if u >= self.upper_threshold:
                        return offer
                    else:
                        if self.exchange_counter == 1:
                            self.offer = self.preferences[:]
                            return self.offer
                        else:
                            if self.exchange_counter >= 5:
                                self.upper_threshold -= self.full_points/20 # TODO: TWEAK
                            self.offer = self.scramble() #makes it slightly trickier to read our offers
                            return self.offer

# ------------- if not first exchange and not successful at being a dick
            else:
                if self.dick_counter < 3:
                    if u >= self.upper_threshold:
                        return offer
                    else:
                        if self.exchange_counter == 1:
                            self.offer = self.preferences[:]
                            return self.offer
                        else:
                            if self.exchange_counter >= 5:
                                self.upper_threshold -= self.full_points/10 # TODO: TWEAK
                            self.offer = self.scramble() #makes it slightly trickier to read our offers
                            return self.offer
                elif self.dick_counter >= 3:
                    self.upper_threshold -= self.full_points/10 # TODO: TWEAK
                    if u >= self.upper_threshold:
                        return offer
                    else:
                        if self.exchange_counter == 1:
                            self.offer = self.preferences[:]
                            return self.offer
                        else:
                            if self.exchange_counter >= 5:
                                self.upper_threshold -= self.full_points/10 # TODO: TWEAK
                            self.offer = self.scramble() #makes it slightly trickier to read our offers
                            return self.offer

        else:
            self.offer = self.preferences[:]
            return self.offer

    def dick_offer_checker(self, offer):
        if offer in self.list_of_opponent_offers:
            return True
        if len(self.list_of_opponent_negotiation_utilities) > 1:
            if self.list_of_opponent_negotiation_utilities[-1] > self.list_of_opponent_negotiation_utilities[-2]:
                return True
        return False

    def scramble(self):
        index = 0
        offer = self.preferences[:]
        while index < len(self.preferences) - 1:
            temp = offer[index]
            offer[index] = offer[index + 1]
            offer[index + 1] = temp
            index += 2

        return offer

    # receive_utility(self : BaseNegotiator, utility : Float)
        # Store the utility the other negotiator received from their last offer
    def receive_utility(self, utility):
        self.list_of_opponent_negotiation_utilities.append(utility)

    # receive_results(self : BaseNegotiator, results : (Boolean, Float, Float, Int))
        # Store the results of the last series of negotiation (points won, success, etc.)
    def receive_results(self, results):
        if self.exchange_counter == 11:
            self.a = True

        if self.a:
            if results[1] > results[2]:
                self.successful_dick = True
            else:
                self.successful_dick = False
        else:
            if results[2] > results[1]:
                self.successful_dick = True
            else:
                self.successful_dick = False

        self.a = False
        self.exchange_counter = 0
        self.round += 1
        pass