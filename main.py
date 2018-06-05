from surprise import Dataset
from surprise.model_selection import cross_validate
from algo.combined import CombinedReduction

data = Dataset.load_builtin('ml-100k')
algo = CombinedReduction()

cross_validate(algo, data, verbose=True)