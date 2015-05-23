__author__ = 'Michael'
from negotiator_base import BaseNegotiator
from functools import reduce

class JackassNegotiator(BaseNegotiator):
    # Constructor - Note that you can add other fields here; the only
    # required fields are self.preferences and self.offer
    def __init__(self):
        self.preferences = []
        self.offer = []
        self.iter_limit = 0
        self.exchange_count = 0

    # initialize(self : BaseNegotiator, preferences : list(String), iter_limit : Int)
        # Performs per-round initialization - takes in a list of items, ordered by the item's
        # preferability for this negotiator
        # You can do other work here, but still need to store the preferences
    def initialize(self, preferences, iter_limit):
        self.preferences = preferences[:]
        self.iter_limit = iter_limit

    # make_offer(self : BaseNegotiator, offer : list(String)) --> list(String)
        # Given the opposing negotiator's last offer (represented as an ordered list),
        # return a new offer. If you wish to accept an offer & end negotiations, return the same offer
        # Note: Store a copy of whatever offer you make in self.offer at the end of this method.
    def make_offer(self, offer):
        self.exchange_count += 1
        if self.exchange_count >= 10:
            self.offer = offer[:]
            return self.offer
        else:
            self.offer = self.preferences[:]
            return self.offer

    # receive_utility(self : BaseNegotiator, utility : Float)
        # Store the utility the other negotiator received from their last offer
    def receive_utility(self, utility):
        pass

    # receive_results(self : BaseNegotiator, results : (Boolean, Float, Float, Int))
        # Store the results of the last series of negotiation (points won, success, etc.)
    def receive_results(self, results):
        self.exchange_count = 0
        pass
