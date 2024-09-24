
def hangman(wrong_answers):
    if wrong_answers == 0:
        print(stage_0)
    elif wrong_answers == 1:
        print(stage_1)
    elif wrong_answers == 2:
        print(stage_2)
    elif wrong_answers == 3:
        print(stage_3)
    elif wrong_answers == 4:
        print(stage_4)
    elif wrong_answers == 5:
        print(stage_5)
    else:
        print(stage_6)        
        
        
        
        
        
        
stage_0 = r"""
+---+
|   |
    |
    |
    |
    |
=========
"""

stage_1 =r"""
+---+
|   |
O   |
    |
    |
    |
=========
"""

stage_2 =r"""
+---+
|   |
O   |
|   |
    |
    |
=========
"""


stage_3 =r"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========

"""


stage_4 =r"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========

"""


stage_5 =r"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========

"""


stage_6 =r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========

"""