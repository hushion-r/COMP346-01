from Requests import *

# author: Rae Hushion
# MetroTransitActivity
# Due Fri 7 Sept 2018


# do requests
# raw_input() ?


class GetInfo:
    def __init__(self):
        self.route = 000
        self.direction = 1
        self.stops = []

    def get_routes(self):
        all_routes = []     # add
        while self.route not in all_routes:
            self.route = input("Which bus route are you taking?")
            if self.route not in all_routes:
                print("ERROR. TRY AGAIN.")

    def get_direction(self):
        directions = [1, 2]
        while self.direction not in directions:
            self.direction = input("\nWhich direction are you travelling on route " + self.route
                                   + "(Enter number)" + "\n1 for Northbound" + "\n2 for Southbound")
            if self.direction not in directions:
                print("ERROR. TRY AGAIN.")

    def get_stops(self):
        all_stops = []      # add
        while self.stops not in all_stops:
            self.stops = input("\nWhich stop will you depart from? (Enter stop code)")
            if self.stops not in all_stops:
                print("ERROR. TRY AGAIN.")


class CallMetroAPI:
    def __init__(self):
        self


userInfo = GetInfo()
