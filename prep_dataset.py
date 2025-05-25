import pandas as pd

# Read only first two columns: English and French
df = pd.read_csv("fra.txt", sep='\t', header=None, usecols=[0, 1], names=["english", "french"])

# Optional: Filter out long sentences to keep flashcards simple
df = df[df['english'].str.split().str.len() <= 6]
df = df[df['french'].str.split().str.len() <= 6]

# Save cleaned data
df.to_csv("french_words.csv", index=False)
print(f"Saved {len(df)} word pairs to french_words.csv")