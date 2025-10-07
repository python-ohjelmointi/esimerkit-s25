def sudoku_numerot_ok(numerot: list[int]) -> bool:
    """
    Palauttaa True, jos funktiolle annetut numerot ovat kelvollinen
    sudoku-lista. Muuten palauttaa False.

    >>> sudoku_numerot_ok([9, 0, 0, 0, 8, 0, 3, 0, 0])
    True

    >>> sudoku_numerot_ok([2, 0, 0, 2, 5, 0, 7, 0, 0])
    False

    >>> sudoku_numerot_ok([9, 10, 0, 0, 8, 0, 3, 0, 0])
    False
    """
    for numero in numerot:
        # nolla tarkoittaa, että lukua ei ole vielä asetettu:
        if numero == 0:
            continue

        # luku oikealla välillä:
        if  numero < 1 or numero > 9:
            return False

        # luku saa esiintyä listalla korkeintaan kerran:
        if numerot.count(numero) > 1:
            return False

    return True


if __name__ == '__main__':
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_numerot_ok(sudoku[0]))
    print(sudoku_numerot_ok(sudoku[1]))
