from argparse import ArgumentParser
from itertools import islice
from itertools import combinations
import logging
logging.basicConfig(filename="351101.log", level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, default=None)
    args = parser.parse_args()
    with open(args.input) as input_file:
        with open("output.txt", "w") as output_file:
            tt_number = input_file.readline()
            case = 1
            while True:
                params = list(map(str.rstrip, islice(input_file, 3)))
                if not params:
                    break
                credit, items_number, items = params
                credit = int(credit)
                items = map(int, items.split())
                items_number = int(items_number)
                log.debug("credit: {0}, items: {1}".format(credit, items))
                for first, second in combinations(items, 2):
                    items_sum = first + second
                    log.debug("{0} + {1} = {2} (credit = {3})".format(first, second, items_sum, credit))
                    if items_sum == credit:
                        log.info("found: {0} + {1} = {2} (credit = {3})".format(first, second, items_sum, credit))
                        first_index = items.index(first)
                        second_index = items[first_index + 1:].index(second) + first_index + 1
                        output_file.write("Case #{0}: {1} {2}\n".format(case, first_index + 1, second_index + 1))
                        break
                case += 1
            # first_index = 0
            # second_index = 1
            # for first in items:
            #     for second in items[first_index + 1:]:
            #         items_sum = first + second
            #         log.debug("{0} + {1} = {2} (credit = {3})".format(first, second, items_sum, credit))
            #         if items_sum == credit:
            #             log.debug("found {0} {1}".format(first, second))
            #             break
            #         second_index += 1
            #     first_index += 1



if __name__ == "__main__":
    main()
