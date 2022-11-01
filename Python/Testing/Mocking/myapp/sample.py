from Python.Testing.Mocking.myapp.dice import roll_dice


def guess_number(num):
    result = roll_dice()
    return "You won!" if result == num else "You lost!"
