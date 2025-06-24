names = ["Bob", "Alice", "Eve"]
scores = [42, 97, 68]

for name, score in zip(names, scores):
    print(f"{name} has {score} score")


names = ["Bob", "Alice", "Eve"]
scores = [42, 97, 68]
zip_result = zip(names, scores)

# Zip is a Generator type, it will get exhaust after first iteration through it
# Works fine the first time!
for name, score in zip_result:
    print(f"{name} had a score of {score}.")
# But empty if we try to loop over it again.
for name, score in zip_result:
     print(f"{name} had a score of {score}.")
