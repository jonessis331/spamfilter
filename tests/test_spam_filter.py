import unittest
from spamfilter.email_processor import load_tokens
from spamfilter.spam_filter import SpamFilter, log_probs

class TestSpamFilterFunctionality(unittest.TestCase):
    def setUp(self):
        # Assuming the 'data' folder is at the root of your project structure
        self.base_dir = "data/"
        self.ham_dir = self.base_dir + "ham/"
        self.spam_dir = self.base_dir + "spam/"

    def test_load_tokens_ham(self):
        self.assertEqual(load_tokens(self.ham_dir+"ham1")[200:204], ['of', 'my', 'outstanding', 'mail'])
        self.assertEqual(load_tokens(self.ham_dir+"ham2")[110:114], ['for', 'Preferences', '-', "didn't"])

    def test_load_tokens_spam(self):
        self.assertEqual(load_tokens(self.spam_dir+"spam1")[1:5], ['You', 'are', 'receiving', 'this'])
        self.assertEqual(load_tokens(self.spam_dir+"spam2")[:4], ['<html>', '<body>', '<center>', '<h3>'])

    def test_log_probs_ham(self):
        paths = [self.ham_dir+"ham%d" % i for i in range(1, 11)]
        p = log_probs(paths, 1e-5)
        self.assertAlmostEqual(p["the"], -3.6080194731874062)
        self.assertAlmostEqual(p["line"], -4.272995709320345)

    def test_log_probs_spam(self):
        paths = [self.spam_dir+"spam%d" % i for i in range(1, 11)]
        p = log_probs(paths, 1e-5)
        self.assertAlmostEqual(p["Credit"], -5.837004641921745)
        self.assertAlmostEqual(p["<UNK>"], -20.34566288044584)

    def test_is_spam(self):
        sf = SpamFilter(self.spam_dir, self.ham_dir, 1e-5)
        self.assertTrue(sf.is_spam(self.spam_dir+"spam1"))
        self.assertTrue(sf.is_spam(self.spam_dir+"spam2"))
        self.assertFalse(sf.is_spam(self.ham_dir+"ham1"))
        self.assertFalse(sf.is_spam(self.ham_dir+"ham2"))

    def test_most_indicative_tokens(self):
        sf = SpamFilter(self.spam_dir, self.ham_dir, 1e-5)
        self.assertEqual(sf.most_indicative_spam(5), ['<a', '<input', '<html>', '<meta', '</head>'])
        self.assertEqual(sf.most_indicative_ham(5), ['Aug', 'ilug@linux.ie', 'install', 'spam.', 'Group:'])

if __name__ == '__main__':
    unittest.main()
