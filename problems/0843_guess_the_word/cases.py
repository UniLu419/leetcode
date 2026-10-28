import random

METHOD = "findSecretWord"


class Master:
    """LeetCode's judge: guess returns -1 for a word outside words, else the count of exact position matches."""

    def __init__(self, secret, words, allowed_guesses):
        self.secret = secret
        self.words = set(words)
        self.allowed_guesses = allowed_guesses
        self.calls = 0
        self.found_at = None

    def guess(self, word):
        self.calls += 1
        if word not in self.words:
            return -1
        if word == self.secret and self.found_at is None:
            self.found_at = self.calls
        return sum(a == b for a, b in zip(word, self.secret))

    def __repr__(self):
        return f"Master(secret={self.secret!r}, allowedGuesses={self.allowed_guesses})"


def check(output, expected, args):
    """Passes when the secret was guessed and the total number of guess calls is at most allowedGuesses."""
    master = args[1]
    return master.found_at is not None and master.calls <= master.allowed_guesses


def random_words(n, seed=0):
    rng = random.Random(seed)
    words, seen = [], set()
    while len(words) < n:
        w = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6))
        if w not in seen:
            seen.add(w)
            words.append(w)
    return words


def case(secret, words, allowed_guesses):
    return dict(args=(words, Master(secret, words, allowed_guesses)), expected=True)


RANDOM_100 = random_words(100)
ONE_LETTER_APART = ["aaaaa" + c for c in "abcdefghijklmnopqrstuvwxyz"]

CASES = [
    case("acckzz", ["acckzz", "ccbazz", "eiowzz", "abcczz"], 10),
    case("hamada", ["hamada", "khaled"], 10),
    # 只有一个单词
    case("abcdef", ["abcdef"], 10),
    # 100 个随机单词，按列表顺序猜（即使每次过滤候选）都超过 10 次
    case(RANDOM_100[59], RANDOM_100, 10),
    case(RANDOM_100[96], RANDOM_100, 10),
    # 单词两两只差最后一位，每次猜测最多排除一个；需要 26 次，不能只循环 10 次
    case("aaaaaz", ONE_LETTER_APART, 30),
]
