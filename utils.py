def clean_str(s):
    buf = ''
    for c in s:
        if c.isprintable():
            buf += c
    return buf.strip()

def html_str(s):
    buf = ''
    s = s.lower()
    for c in s:
        if c.isalnum():
            buf += c
    return buf
