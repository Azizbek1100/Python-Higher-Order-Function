votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
most_voted = max(votes, key=lambda x: x["votes"])
print(most_voted)