def judge(question, expects, answer, results) -> bool:
	"""Determine whether ``answer`` matches an expected answer."""
	return expects.lower().strip() in answer.lower()

	"""
	def judge(question, expects, answer, results) -> bool:
    
    del question, results  # Not used in this check

    # If expects is a single string/bytes, wrap it in a tuple.
    if isinstance(expects, (str, bytes)):
        expects = (expects,)
    else:
        try:
            expects = tuple(expects)
        except TypeError:
            expects = (expects,)

    # Normalize by stripping whitespace and lowercasing, so comparisons
    # are case-insensitive and ignore extra spaces.
    def normalize(value):
        return str(value).strip().casefold().lower()

    # Check whether any expected answer matches the actual answer.
    return any(normalize(answer) == normalize(expected) for expected in expects)
	"""


    """
	LLM as judge
	rapidfuzz
	"""