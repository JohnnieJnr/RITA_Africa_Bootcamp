movies = {"Aladin", "Men in Black", "Avengers", "Hawkeye", "Iron Man"}

# Adding a single movie to the set
movies.add("Thor")
print(movies)
print("\n")

# Adding multiple movies to the set using a single method
movies.update(["Black Widow", "Ant Man", "Spiderman"])
print(movies)
print("\n")

# Remove one movie from the set
movies.remove("Aladin")
print(movies)
print("\n")

if "Aladin" in movies:
    print("Yes, Aladin is in the set")
else:
    print("No, the movie is not in the set")
