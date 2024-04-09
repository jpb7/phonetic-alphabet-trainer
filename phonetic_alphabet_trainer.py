"""
Phonetic alphabet trainer

    Command-line tool for practicing the NATO phonetic alphabet.

Instructions:
    Run from the terminal. You'll be prompted with the English letter
    corresponding to a given phonetic code. Type in the full phonetic
    code, properly spelled and capitalized, within the per-response time
    limit `TIME_LIMIT` (which can be adjusted below). Responses given
    outside the time limit will be considered correct but will be
    flagged with a warning at the end of the run. Note that the order of
    the codes will be randomized from run to run, and that missing a
    code will cause the answer to be displayed and the prompt repeated
    until the code is entered in correctly.

Author: Jacob Bentley
Date: 04/08/2024
Version: 1.0
"""

import sys
from random import shuffle
from time import time
from typing import List, Tuple

TIME_LIMIT = 3 # seconds per prompt

#   Functions

def shuffled_codes() -> List[str]:
    """
    Returns a shuffled list of NATO phonetic alphabet codes.
    """
    codes = [
        'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
        'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November',
        'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform',
        'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu'
    ]
    shuffle(codes)
    return codes

def timed_input(prompt: str) -> Tuple[str, float, bool]:
    """
    Prompts the user, gets a response, and measures how long it took.
    """
    start = time()
    entry = input(prompt)
    duration = time() - start
    return entry, duration, duration <= TIME_LIMIT

#   Main function

def main() -> None:
    """
    Loops through randomized NATO codes, prompting the user for exact
    matches and timing their responses.
    """
    warnings = []
    misses = 0
    codes = shuffled_codes()
    start = time()
        
    print('\nEnter "quit" at any time.\n')

    while codes:
        code = codes[-1]
        letter = code[0]

        try:
            entry, duration, fast_enough = timed_input(f'{letter}: ')
        except KeyboardInterrupt:
            entry = 'quit'
            print()

        if entry.lower() == 'quit':
            print('\nQuitting...\n')
            sys.exit()

        if entry == code:
            codes.pop()
            if not fast_enough:
                warnings.append((code, round(duration, 2)))
        else:
            misses += 1
            print(f'\n - {code} - \n')

    session = round(time() - start, 2)
    print(f'\nTime: {session}s\nMisses: {misses}')

    if warnings:
        print('\nTook too long on:')
        for code, duration in warnings:
            print(f'  - {code}: {duration}s')

    print()

if __name__ == '__main__':
    main()

