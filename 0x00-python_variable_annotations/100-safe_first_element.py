from typing import Optional, Sequence

def safe_first_element(lst: Sequence[object]) -> Optional[object]:
    """Returns 1st elem of sequence if it exists, otherwise None.

    Args:
        lst: Input sequence.

    Returns:
        The 1st elem of sequence, or None if sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

