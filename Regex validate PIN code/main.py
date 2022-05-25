def validate_pin(pin):
    if len(pin) == 4 or len(pin) ==6:
        for char in pin:
            if char.isdigit():
                pass
            else:
                return False
        return True
    else:
        return False