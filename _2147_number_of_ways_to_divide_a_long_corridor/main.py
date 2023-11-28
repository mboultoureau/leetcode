class Solution:
    def numberOfWays(self, corridor: str) -> int:
        result = 1
        i = 0

        while i < len(corridor):
            # Iterate while two seats found
            nbSeats = 0
            while i < len(corridor) and nbSeats < 2:
                if corridor[i] == 'S':
                    nbSeats += 1
                i += 1

            # If we finish with odd number of seats, no solution
            if nbSeats != 2:
                return 0

            # Count number of plants
            nbPlants = 0
            while i < len(corridor) and corridor[i] != 'S':
                nbPlants += 1
                i += 1

            # Multiply number of plants (representing number of possibility - 1) only if we don't reach the end
            if i != len(corridor) and nbPlants > 0:
                result *= nbPlants + 1

        return result % (10**9 + 7)