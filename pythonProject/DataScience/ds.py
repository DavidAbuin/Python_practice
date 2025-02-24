

# Chapter 1-----------------------------
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

print(friendship_pairs)



# Chapter 11: Machine Learning ------------------------------------------------
import random

from typing import TypeVar, List, Tuple
X = TypeVar('X') # generic type to represent a data point

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """ Split data into fractions [ prob, 1- prob]"""
    data = data[:]                  # Make a shallow copy
    random.shuffle(data)            # because shuffle modifies the list.
    cut = int(len(data) * prob)     # Use prob to find a cutoff
    return data[:cut], data[cut:]   # and split the shuffled list here

data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

# The proportions should be currect
assert len(train) == 750
assert len(test) == 250

# And the original data should be preserved (in some order).
assert sorted(train + test) == data


Y = TypeVar('Y')  # generic type to represent output variables

def train_test_split(xs: List[X],
                     ys: List[Y],
                     test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:

    # Generate the indices and split them
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)

    return ([xs[i] for i in train_idxs],    #x_train
            [xs[i] for i in test_idxs],     #x_test
            [ys[i] for i in train_idxs],    #y_train
            [ys[i] for i in train_idxs])    #y_test

xs = [x for x in range(1000)]   # xs are 1...1000
ys = [2 * x for x in xs]        # each y_i is twice x_i
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)

#Check that the proportions are correct
#assert all(y == 2 * x for x, y in zip(x_train, y_train))
#assert all(y == 2 * x for x, y in zip(x_test, y_test))

"""
model = SomeKindOfModel()
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.33)
model.train(x_train, y_train)
performance = model.test(x_test, y_test)
"""

# Chapter 12 ---------------------------------------------------------------------------
# K-Nearest Neighbors
from typing import List
from collections import Counter

from typing import NamedTuple
from linearAlgebraDS import Vector, distance

class LabeledPoint(NamedTuple):
    point: Vector
    label: str

def majority_vote(labels: List[str]) -> str:
    """Assumes that the labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values() if count == winner_count])
    if num_winners == 1:
        return winner                       # unique winner
    else:
        return majority_vote(labels[:-1]) # try again without the farthest

def knn_classify(k: int, labeled_points: List[LabeledPoint], new_point: Vector) -> str:
    # Order the labeled points from nearest to farthest.
    by_distance = sorted(labeled_points, key = lambda lp: distance(lp.point, new_point))

    #find the labels for the k closest
    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    #and let them vote
    return majority_vote(k_nearest_labels)

# Iris Dataset
import requests

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

with open('iris.data', 'w') as f:
    f.write(data.text)



from typing import Dict
import csv
from collections import defaultdict

def parse_iris_row(row: List[str]) -> LabeledPoint:
    """ sepal_length, sepal_width, petal_length, petal_width, class"""
    measurements = [float(value) for value in row[:-1]]
    # class is e.g. "iris-virginica: we just want "virginica"
    label = row[-1].split("-")[-1]
    return LabeledPoint(measurements, label)


with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]

# We'll also group just the points by species/label so we can plot them
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

from matplotlib import pyplot as plt
metrics = ['sepal length', 'sepal width', 'petal length', 'petal width']
pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
marks = ['+', '.', 'x'] # we have 3 classes, so 3 markers

fig, ax = plt.subplots(2, 3)

for row in range(2):
    for col in range(3):
        i, j = pairs[3 * row + col]
        ax[row][col].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize=8)
        ax[row][col].set_xticks([])
        ax[row][col].set_yticks([])

    for mark, (species, points) in zip(marks, points_by_species.items()):
        xs = [point[i] for point in points]
        ys = [point[j] for point in points]
        ax[row][col].scatter(xs, ys, marker=mark, label=species)

ax[-1][-1].legend(loc='lower right', prop={'size': 6})
plt.show()

import random