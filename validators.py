def is_non_negative_number(value):
    text = value.strip()
    if not text:
        return False
    if text.count(".") > 1:
        return False
    if text.startswith("-"):
        return False
    number_part = text.replace(".", "", 1)
    return number_part.isdigit()
