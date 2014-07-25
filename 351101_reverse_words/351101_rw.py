from argparse import ArgumentParser
import logging

logging.basicConfig(filename="351101.log", level=logging.DEBUG)
log = logging.getLogger(__name__)


def main():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    with open(args.input) as input_file:
        with open(args.output, "w") as output_file:
            number_of_cases = input_file.readline()
            log.info("number of cases to process: {0}".format(number_of_cases))
            case_number = 1
            for input_case in input_file:
                output_case = " ".join(word for word in reversed(input_case.split()))
                output_file.write("Case #{0}: {1}\n".format(case_number, output_case))
                case_number += 1
if __name__ == "__main__":
    main()
