def validate_number(text):
    try:
        float(text)
        return True
    except:
        return False
