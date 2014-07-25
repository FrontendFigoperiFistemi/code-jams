from argparse import ArgumentParser

import logging
from itertools import product

logging.basicConfig(filename="90101.log", level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    with open(args.input) as input_file:
        with open(args.output, "w") as output_file:
            l_count, d_count, n_count = map(int, input_file.readline().split())
            words = []
            for ind in xrange(d_count):
                words.append(input_file.readline().rstrip())
            cases = []
            for ind in xrange(n_count):
                cases.append(input_file.readline().rstrip())
            log.debug("words: " + ",".join(words))
            # log.debug("cases: " + ",".join(cases))
            case_number = 1
            for case in cases:
                word_count = 0
                combinations = []
                pattern = False
                tmp_pattern = ""
                for char in case:
                    if char == "(":
                        pattern = True
                        continue
                    elif char == ")":
                        pattern = False
                        combinations.append(tmp_pattern)
                        tmp_pattern = ""
                        continue
                    else:
                        if pattern:
                            tmp_pattern += char
                        else:
                            combinations.append(char)
                log.debug(case)
                for combination in product(*combinations):
                    word = "".join(combination)
                    if word in words:
                        log.debug(word)
                        word_count += 1
                output_file.write("Case #{0}: {1}\n".format(case_number, word_count))
                case_number += 1

if __name__ == "__main__":
    main()

