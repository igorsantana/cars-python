from surprise import AlgoBase

class CombinedReduction(AlgoBase):

    def __init__(self):

        # Always call base method before doing anything.
        AlgoBase.__init__(self)

    def estimate(self, u, i):
        return 3


