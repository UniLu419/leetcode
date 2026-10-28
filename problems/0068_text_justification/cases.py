METHOD = "fullJustify"

CASES = [
    dict(
        args=(["This", "is", "an", "example", "of", "text", "justification."], 16),
        expected=["This    is    an", "example  of text", "justification.  "],
    ),
    dict(
        args=(["What", "must", "be", "acknowledgment", "shall", "be"], 16),
        expected=["What   must   be", "acknowledgment  ", "shall be        "],
    ),
    dict(
        args=(
            ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
            20,
        ),
        expected=[
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
    ),
    dict(args=(["a"], 1), expected=["a"]),
    dict(args=(["a", "b", "c", "d"], 1), expected=["a", "b", "c", "d"]),
    dict(args=(["ab", "c"], 5), expected=["ab c "]),
    dict(
        args=(["Listen", "to", "many,", "speak", "to", "a", "few."], 6),
        expected=["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "],
    ),
]
