from django import template

register = template.Library()

@register.filter(name="number_to_character")
def number_to_character(value:int):
    numbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "for",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "ten",
    }
    return numbers[value+1]