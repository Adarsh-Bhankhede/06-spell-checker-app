
#! Project Name - Spell Checker App

import re
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
        self.spell.word_frequency.load_words([
                        'Adarsh',
                        'Rahul',
                        'Amit',
                        'Priya', 
                        'bhai'
                    ])

    def correct_text(self, text):
        words = re.findall(r"\b[\w']+\b|[^\w\s]", text)
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word is None:
                corrected_word = word

            if word != corrected_word:
                print(f"Correcting \"{word}\" to \"{corrected_word}\"")
            
            corrected_words.append(corrected_word)

        
        corrected_text = ""

        for word in corrected_words:
            if re.fullmatch(r"[^\w\s]", word):
                corrected_text += word
            else:
                if corrected_text and not corrected_word.endswith(' '):
                    corrected_text += " "
                corrected_text += word
        return corrected_text
        # return ''.join(corrected_words)

    def run_spell_checker_app(self):
        print("\n===== Spell Checker App =====")

        while True:
            text = input("\nEnter the text to spell check: ")
            corrected_text = self.correct_text(text)
            if text != corrected_text:
                print(f"Corrected Text : {corrected_text}")
            else:
                print("No correction needed!!!")
    
            choice = input("\nDo you want to spell check another text? (yes/no):  ")
            if choice.lower() == 'yes':
                continue
            else:
                print("\nThank you..!!!\n")
                break

if __name__ == "__main__":
    spell_checker = SpellCheckerApp()
    spell_checker.run_spell_checker_app()