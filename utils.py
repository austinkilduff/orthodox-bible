def clean_str(s):
    buf = ''
    for c in s:
        if c.isprintable():
            buf += c
    return buf.strip()
