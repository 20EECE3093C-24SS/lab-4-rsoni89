# TODO-1: add convert_to_letter_grade(score) function
def convert_to_letter_grade(score):

    if not isinstance(score,(int,float)):
        raise TypeError("Score must be a numberic value")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80 or score<=89:
        return "B"
    elif score >= 70 or score <= 79:
        return "C"
    elif score >= 60 or score <=69:
        return "D"
    else:
        return "F"
