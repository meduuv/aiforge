def estimate_tokens(text: str) -> int: return (len(text)+3)//4
def truncate(text: str, max_chars: int) -> str:
    if max_chars<0: raise ValueError("max_chars must be non-negative")
    return text[:max_chars]
