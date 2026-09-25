import re

from rapidfuzz import fuzz


FUZZY_THRESHOLD = 90


def judge(question, expects, answer, results) -> bool:
    """Return whether the answer contains an exact or close expected phrase."""
    del question, results

    if isinstance(expects, (str, bytes)):
        expects = (expects,)
    else:
        try:
            expects = tuple(expects)
        except TypeError:
            expects = (expects,)

    def normalize(value):
        text = str(value).casefold()
        text = re.sub(r"(\d{1,2}:\d{2})\s*(am|pm)\b", r"\1 \2", text)
        words = re.sub(r"[^\w\s]", " ", text).split()
        return " ".join(word for word in words if word not in {"a", "an", "the"})

    normalized_answer = normalize(answer)
    return any(
        normalized_expected in normalized_answer
        or fuzz.token_set_ratio(normalized_expected, normalized_answer)
        >= FUZZY_THRESHOLD
        for expected in expects
        if (normalized_expected := normalize(expected))
    )
	
	