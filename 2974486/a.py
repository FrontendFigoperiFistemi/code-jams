from argparse import ArgumentParser
import logging
from itertools import islice
# logging.basicConfig(filename="a.log", level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    with open(args.input) as input_file:
        with open(args.output, "w") as output_file:
            number_of_cases = int(input_file.readline().rstrip())
            for case_number in xrange(1, number_of_cases + 1):
                case_input = list(islice(input_file, 10))
                first_input = int(case_input[0].rstrip())
                first_chosed_row = case_input[first_input].split()
                log.debug("{0}, {1}".format(first_input, first_chosed_row))
                second_input = int(case_input[5].rstrip())
                second_chosed_row = case_input[second_input + 5].split()
                log.debug("{0}, {1}".format(second_input, second_chosed_row))
                intersection = list(set(first_chosed_row) & set(second_chosed_row))
                log.debug(intersection)
                solution = "Case #{0}: {1}\n"
                if len(intersection) == 1:
                    output_file.write(solution.format(case_number, intersection[0]))
                elif len(intersection) == 0:
                    output_file.write(solution.format(case_number, "Volunteer cheated!"))
                else:
                    output_file.write(solution.format(case_number, "Bad magician!"))
            # for case in xrange(1, number_of_cases + 1):
            #     first_input = int(input_file.readline().rstrip())
            #     first_chosed_row = list(islice(input_file, 4))[first_input - 1]
            #     log.debug("{0}, {1}".format(first_input, first_chosed_row))

if __name__ == "__main__":
    main()
