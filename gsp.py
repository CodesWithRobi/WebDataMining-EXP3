from collections import defaultdict
from itertools import combinations
# Function to generate candidate k-item sequences
def generate_candidates(dataset, k, min_support):
    candidates = defaultdict(int)
    for sequence in dataset:
        for itemset in combinations(sequence, k):
            candidates[itemset] += 1
    return {item: support for item, support in candidates.items() if support >= min_support}
#Function to perform GSP algorithm
def gsp(dataset, min_support):
    frequent_pattern = defaultdict(int)
    k = 1
    sequence = dataset
    while True:
      candidates = generate_candidates(sequence, k, min_support)
      if not candidates:
        break
      frequent_pattern.update(candidates)
      k += 1
    return frequent_pattern
#Example dataset for each category
top_wear_data = [
    ["blouse", "t-shirt", "tank_top"],
    ["hoodie", "sweater", "top"],
    ["hoodie"],
    ["hoodie","sweater"]
 #Add more sequences for top wear
]
bottom_wear_data = [
 ["jeans", "trousers", "shorts"],
 ["leggings", "skirt", "chinos"],
 # Add more sequences for bottom wear
]
party_wear_data = [
 ["cocktail_dress", "evening_gown", "blazer"],
 ["party_dress", "formal_dress", "suit"],
 ["party_dress", "formal_dress", "suit"],
 ["party_dress", "formal_dress", "suit"],
 ["party_dress", "formal_dress", "suit"],
 ["party_dress"],["party_dress"],
 # Add more sequences for party wear
]
#Minimum support threshold
min_support = 2
#Perform GSP algorithm for each category
top_wear_result = gsp(top_wear_data, min_support)
bottom_wear_result = gsp(bottom_wear_data, min_support)
party_wear_result = gsp(party_wear_data, min_support)
#Output the frequent sequential patterns for each category
print("Frequent Sequential Patterns - Top Wear:")
if top_wear_result:
 for pattern, support in top_wear_result.items():
    print(f"Pattern: {pattern}, Support: {support}")
else:
 print("No frequent sequential patterns found in Top Wear.")
print("\nFrequent Sequential Patterns - Bottom Wear:")
if bottom_wear_result:
    for pattern, support in bottom_wear_result.items():
        print(f"Pattern: {pattern}, Support: {support}")
else:
    print("No frequent sequential patterns found in Bottom Wear.")
print("\nFrequent Sequential Patterns - Party Wear:")
if party_wear_result:
    for pattern, support in party_wear_result.items():
        print(f"Pattern: {pattern}, Support: {support}")
else:
    print("No frequent sequential patterns found in Party Wear.")
