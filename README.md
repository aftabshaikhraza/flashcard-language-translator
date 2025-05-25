# flashcard-language-translator

This is an interactive language-learning flashcard app built using Python and Tkinter. It helps users learn French vocabulary by flipping flashcards with audio pronunciation.

##  Features
- English–French word pairs
- Auto-flipping flashcards
- Audio pronunciation with `pyttsx3`
- "Correct" / "Wrong" buttons
- Saves missed words to `words_to_learn.csv` for review
- Beautiful card-style UI with image background

##  How to Use
1. Run `main.py`
2. The app shows an English word
3. After 3 seconds, it flips and pronounces the French translation
4. Click ✔ Correct or ✘ Wrong to track your progress
5. Missed words are saved when you close the app

##  Files
- `main.py`: The flashcard app
- `french_words.csv`: Cleaned vocabulary dataset
- `card_bg.png`: Flashcard background image
- `words_to_learn.csv`: Generated when you miss words
- `prep_dataset.py`: Script to extract data from `fra.txt` (optional)

## Dataset Attribution

This project uses sentence pairs originally from the **[Tatoeba Project](https://tatoeba.org/)**, distributed by **[ManyThings.org](https://www.manythings.org/anki/)**.

Due to licensing terms, the dataset is **not included in this repository**.

To run the project:
1. Download `fra.txt` from [this link](https://www.manythings.org/anki/)
2. Use `prep_dataset.py` to generate `french_words.csv`

##  Requirements

Install dependencies:

```bash
pip install pandas pyttsx3
