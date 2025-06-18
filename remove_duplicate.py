def remove_duplicate(s: str) -> str:
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)

print(remove_duplicate('Huzaifa'))
