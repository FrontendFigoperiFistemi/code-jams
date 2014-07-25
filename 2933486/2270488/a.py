from argparse import ArgumentParser
import logging
import numpy as np
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def check_winner(positions):
    winner = ""
    Ts = positions.count("T")
    Os = positions.count("O")
    Xs = positions.count("X")
    if Ts + Os == 4:
        winner = "O won"
    if Ts + Xs == 4:
        winner = "X won"
    return winner

def main():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()
    with open(args.input) as file_input:
        with open(args.output, "w") as file_output:
            ncases = int(file_input.readline().rstrip())
            for case_number in range(1, ncases + 1):
                board = []
                winner = ""
                for i in range(4):
                    board.append([c for c in file_input.readline().rstrip()])
                    # log.debug(file_input.readline())
                file_input.readline()
                for row in board:
                    row_winner = check_winner(row)
                    if row_winner:
                        winner = row_winner
                for col_num in range(4):
                    column = []
                    for row in board:
                        column.append(row[col_num])
                    col_winner = check_winner(column)
                    if col_winner:
                        winner = col_winner
                diag_winner = check_winner([board[0][0], board[1][1], board[2][2], board[3][3]])
                if diag_winner:
                        winner = diag_winner
                diag_winner = check_winner([board[3][0], board[2][1], board[3][2], board[0][3]])
                if diag_winner:
                        winner = diag_winner
                if not winner:
                    for row in board
                file_output.write("Case #{0}: {1}\n".format(case_number, winner))
                log.debug("Case #{0}: {1}\n".format(case_number, winner))



if __name__ == "__main__":
    main()
