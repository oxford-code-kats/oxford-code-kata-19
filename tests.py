import unittest

class TestWords(unittest.TestCase):
    def setUp(self):
        import words
        self.checker = words.WordChecker()

    def test_caaaaaat_is_not_word(self):
        self.failIf(self.checker.is_word('caaaaaaaat'))

    def test_cat_is_word(self):
        self.failUnless(self.checker.is_word('cat'))

class TestMutator(unittest.TestCase):
    def setUp(self):
        import words
        mutator = words.WordMutator()

    def test_mutations(self):
        # ....
        pass

class TestPaths(unittest.TestCase):
    def setUp(self):
        import words
        checker = words.WordChecker()
        mutator = words.WordMutator()
        self.pathfinder = words.WordPathFinder(checker, mutator)

    def test_cat_to_dog(self):
        path = self.pathfinder.find_path('cat', 'dog')
        self.assertEqual(['cat', 'cot', 'cog', 'dog'], path)

if __name__ == '__main__':
    unittest.main()




