import math as cronos
class Pics:
    def retNum(num, r, g, b):
        none = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        zero = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        one = [
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]]
        ]

        two = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        three = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]]
        ]

        four = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [r, g, b], [r, g, b],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        five = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [r, g, b], [r, g, b],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        six = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        seven = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [r, g, b], [r, g, b],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [0, 0, 0], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [r, g, b], [0, 0, 0],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        eight = [
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        nine = [
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[r, g, b], [0, 0, 0], [0, 0, 0],  [r, g, b]],
            [[0, 0, 0], [r, g, b], [r, g, b],  [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],  [0, 0, 0]]
        ]

        numbers = [zero, one, two, three, four, five, six, seven, eight, nine, none]

        first = cronos.floor(num/10)
        if first == 0:
            first = 10

        second = num%10

        return [numbers[first], numbers[second]]
