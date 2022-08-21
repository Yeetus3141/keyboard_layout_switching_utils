"""
Little script to convert blender keymaps to different keyboard layouts.
Currently only designed to replace letter keys and ;. 
"""

import re

input_kmp_path = "blender_qwerty_keymap.py" # source keymap file location
output_kmp_path = "blender_colemakdh_keymap.py" # output keymap file location

source_chars = "QWERTYUIOPASDFGHJKL;ZXCVBNM" # keys to replace
target_chars = "QWFPBJLUY;ARSTGMNEIOZXCDVKH" # keys to replace with (in the same order)

special_chars = {
    ';': 'SEMI_COLON',
}

def chars_to_kmp(chars):
    kmp = []
    for i in chars:
        if i in special_chars.keys():
            i = special_chars[i]
        kmp.append(i)
    
    return kmp

source_kmp = chars_to_kmp(source_chars)
target_kmp = chars_to_kmp(target_chars)
print(source_kmp)

def replace_key(match_obj):
    if match_obj.group(1) in source_kmp:
        return re.sub(r"\'.\'", f"\'{target_kmp[source_kmp.index(match_obj.group(1))]}\'", match_obj.group(0))

with open(input_kmp_path, 'r') as src:
    input_kmp = src.readlines()

output_kmp = []
for line in input_kmp:
     output_kmp.append(re.sub(r'"type": \'(.)\'', replace_key, line))

with open(output_kmp_path, 'w') as dest:
    dest.writelines(output_kmp)


    