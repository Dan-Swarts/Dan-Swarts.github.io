from typing import List, Any, Union

import sample_text

file_obj = open(sample_text.file, r)

alphabet: = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for letter in alphabet:
    letter_count = 0
    for letter in sample_text:
        letter_count += 1
    print(letter, letter_count)

file_obj.close()