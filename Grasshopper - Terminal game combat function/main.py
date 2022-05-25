def combat(health, damage):
    final = health - damage
    if final >0:
        return final
    else:
        return 0