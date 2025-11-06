def solution(input_string):
    seen = set()
    lonely = set()
    prev = None

    for ch in input_string:
        if ch != prev:
            if ch in seen:
                lonely.add(ch)
            seen.add(ch)
            prev = ch

    if not lonely:
        return "N"
    return "".join(sorted(lonely))