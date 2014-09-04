
class WordChecker(object):
    def __init__(self):
        self.all_words = {}
        WORDS_FILE = '/usr/share/dict/words'
        self.compile(WORDS_FILE)

    def is_word(self, word):
        return word.strip().lower() in self.all_words

    def compile(self, input):
        all_words = {}
        with open(input, 'rb') as f:
            for line in f.readlines():
                all_words[line.strip().lower()] = True
        
        self.all_words = all_words

class WordMutator(object):
    def __init__(self):
        pass

    def mutate(self, word):
        all_mutations = []
        for letter_idx in range(0, len(word)):
            prefix = word[:letter_idx]
            suffix = word[letter_idx+1:]
            for new_letter in ALL_LETTERS:
                new_word = prefix + new_letter + suffix
                all_mutations.append(new_word)
        return all_mutations


ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class WordPathFinder(object):
    def __init__(self, word_checker, mutator, all_letters=ALL_LETTERS):
        self.letters = dict.fromkeys(all_letters)
        self.checker = word_checker
        self.mutator = mutator

    def is_word(self, word):
        return self.checker.is_word(word)

    def find_path(self, start, end):
        """
        Given start='cat', end='dog' return
        ['cat', 'cot', 'cog', 'dog']
        """
        assert self.is_word(start), start
        assert self.is_word(end), end
        return self.breadth_first_search(start, end)

    def get_next_word_options(self, word):
        return filter(self.is_word, self.mutator.mutate(word))

    def breadth_first_search(self, start, end):
        if start == end: return [end]
        next_words = self.get_next_word_options(start)
        paths = []
        for word in next_words:
            try:
                return [start]+self.breadth_first_search(word, end)
            except NoResults:
                continue
        if not paths:
            raise NoResults(start, end, "No paths available")
        return paths[0]

class NoResults(Exception): pass

