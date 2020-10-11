from collections import Counter
import re

def count_words(str):
    str = str.lower()
    str_list = re.findall(r"\b[\w'-]+\b", str)
    counter = Counter(str_list)
    return counter