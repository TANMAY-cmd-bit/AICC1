import math
movies = {
    "Movie1": [5, 1, 0],
    "Movie2": [4, 1, 0],
    "Movie3": [1, 5, 4],
    "Movie4": [0, 4, 5]
}
user = [5, 1, 0]
def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
distances = {}
for movie, features in movies.items():
    distance = euclidean_distance(user, features)
    distances[movie] = distance
sorted_movies = sorted(distances.items(), key=lambda x: x[1])
print("Recommended movies (closest match):")
for movie, dist in sorted_movies:
    print(movie, "-> Distance:", round(dist, 2))