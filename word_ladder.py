#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony',
    'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots',
    'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    words = []
    if(start_word == end_word):
        return [start_word]
    if len(start_word) != len(end_word):
        return None
    with open(dictionary_file, 'r') as f:
        for word in f.readlines():
            words.append(word.strip('\n'))
    list1 = []
    list1.append(start_word)
    q1 = deque()
    q1.append(list1)

    while len(q1) != 0:
        stack = q1.popleft()
        for word in set(words):
            if _adjacent(word, stack[-1]):
                if word == end_word:
                    stack.append(word)
                    return stack
                newstack = copy.deepcopy(stack)
                newstack.append(word)
                q1.append(newstack)
                words.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 1:
        return True
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]):
            i += 1
            if i == len(ladder) - 1:
                return True
        else:
            return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    list1 = list(word1)
    list2 = list(word2)
    counter = 0
    for i in range(len(list1)):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                counter += 1
            else:
                pass
        if counter == 1:
            return True
        else:
            return False
