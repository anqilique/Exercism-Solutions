def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    if hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob == '' or hey_bob.isspace():
       return "Fine. Be that way!"
    
    return "Whatever."
