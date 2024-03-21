# spell checker
# case sensitive
class HashTable:
    def __init__(self, size):
        self.size = size
        # intializes hash table with empty lists
        self.table = [[] for _ in range(size)]

    def hashFunction(self, word):
        return sum(ord(char) for char in word) % self.size

    def insert(self, word):
        # Insert word into hash table
        index = self.hashFunction(word)
        if word not in self.table[index]:
            self.table[index].append(word)

    def search(self, word):
        # check if word is in the hash table
        index = self.hashFunction(word)
        return word in self.table[index]

class SpellChecker:
    def __init__(self, dictionaryFile):
        # initializes spell checker with a hash table for the dictionary
        self.dictionary = HashTable(100)
        self.loadDictionary(dictionaryFile)

    def loadDictionary(self, dictionaryFile):
        # loads dictionary from file into the hash table
        with open(dictionaryFile, 'r') as file:
            for word in file:
                self.dictionary.insert(word.strip())

    def checkSpelling(self, text):
        # checks spelling of each word in the text
        misspelledWords = []
        for word in text.split():
            if not self.dictionary.search(word):
                misspelledWords.append(word)
        return misspelledWords

    def suggestCorrections(self, word):
        # generates suggestions for correcting misspelled word
        suggestions = []
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(word)):
            # deletion
            deletion = word[:i] + word[i+1:]
            if self.dictionary.search(deletion):
                suggestions.append(deletion)
            # transposition
            for j in range(i+1, len(word)):
                transposition = word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
                if self.dictionary.search(transposition):
                    suggestions.append(transposition)
            # substitution
            for char in alphabet:
                substitution = word[:i] + char + word[i+1:]
                if self.dictionary.search(substitution):
                    suggestions.append(substitution)
            # insertion
            for char in alphabet:
                insertion = word[:i] + char + word[i:]
                if self.dictionary.search(insertion):
                    suggestions.append(insertion)
        return suggestions

    def addToDictionary(self, word):
        # adds words to the dictionary
        self.dictionary.insert(word)

def main(): # user input main function
    dictionaryFile = input("Enter the path to the dictionary file: ")
    spellChecker = SpellChecker(dictionaryFile)

    while True:
        print("\nSpell Checker Menu:")
        print("1. Check spelling")
        print("2. Add word to dictionary")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to check spelling: ")
            misspelledWords = spellChecker.checkSpelling(text)
            if misspelledWords:
                print("Misspelled words:", misspelledWords)
                for word in misspelledWords:
                    suggestions = spellChecker.suggestCorrections(word)
                    if suggestions:
                        print("Suggestions for", word + ":", suggestions)
            else:
                print("No misspelled words found.")
        
        elif choice == "2":
            newWord = input("Enter word to add to dictionary: ")
            spellChecker.addToDictionary(newWord)
            print("Word added to dictionary.")

        elif choice == "3":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
