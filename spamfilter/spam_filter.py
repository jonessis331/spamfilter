import math
import os
from .email_processor import load_tokens

def log_probs(email_paths, smoothing):
    frequencyDict = {}
    total = 0
    for p in email_paths:
        words = load_tokens(p)
        total += len(words)
        for w in words:
            if w in frequencyDict:
                frequencyDict[w] += 1
            else:
                frequencyDict[w] = 1
    v = len(frequencyDict)
    dict = {}
    bottom = total + smoothing * (v+1)
    for w, c in frequencyDict.items():
        probability = (c+smoothing)/ bottom
        dict[w] = math.log(probability)
        

    dict["<UNK>"] = math.log(smoothing/bottom)

    return dict


class SpamFilter(object):
    def __init__(self, spam_dir, ham_dir, smoothing):
        spamEmails= []
        hamEmails = []
        for f in os.listdir(spam_dir):
            spamEmails.append(os.path.join(spam_dir, f))
        for f in os.listdir(ham_dir):
            hamEmails.append(os.path.join(ham_dir, f))

        self.spamLogProbDict = log_probs(spamEmails, smoothing)
        self.hamLogProbDict = log_probs(hamEmails, smoothing)

        totalEmails = len(spamEmails) + len(hamEmails)
        self.p_spam = len(spamEmails) / totalEmails
        self.p_notSpam = len(hamEmails) / totalEmails
        self.smoothing = smoothing

    def is_spam(self, email_path):
        loadedTokens = load_tokens(email_path)

        logSpam = math.log(self.p_spam)
        logHam = math.log(self.p_notSpam)

        for t in loadedTokens:
            defualt = self.spamLogProbDict.get('<UNK>', math.log(self.smoothing))
            logSpam += self.spamLogProbDict.get(t, defualt)
            defualt = self.hamLogProbDict.get('<UNK>', math.log(self.smoothing))
            logHam += self.hamLogProbDict.get(t, defualt)
        if logSpam > logHam:
            return True
        return False

    def most_indicative_spam(self, n):
        wordCount = {}
        for word, prob in self.spamLogProbDict.items():
            if word in self.hamLogProbDict:
                wordCount[word] = prob - math.log(math.exp(prob) + math.exp(self.hamLogProbDict[word]))

        sortedWords = []
        while wordCount:
            mostFrequent = max(wordCount, key= wordCount.get)
            sortedWords.append(mostFrequent)
            del wordCount[mostFrequent]
        return sortedWords[:n]

    def most_indicative_ham(self, n):
        wordCount = {}

        for word, prob in self.hamLogProbDict.items():
            if word in self.spamLogProbDict:
                wordCount[word] = prob - math.log(math.exp(prob) + math.exp(self.spamLogProbDict[word]))

        sortedWords = []
        while wordCount:
            mostFrequent = max(wordCount, key=wordCount.get)
            sortedWords.append(mostFrequent)
            del wordCount[mostFrequent]
        return sortedWords[:n]


