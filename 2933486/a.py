from argparse import ArgumentParser
from collections import defaultdict
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    with open(args.input) as input_file:
        with open(args.output, "w") as output_file:
            for case_number in range(1, int(input_file.readline().rstrip()) + 1):
                couples = []
                warriors = set()
                enemies = defaultdict(set)
                response = "Yes"
                for couple_number in range(int(input_file.readline().rstrip())):
                    couples.append(input_file.readline().rstrip().split())

                log.debug("Case #{0}: ".format(case_number))
                for warr1, warr2 in couples:
                    enemies[warr1].add(warr2)
                    enemies[warr2].add(warr1)
                    warriors.add(warr1)
                    warriors.add(warr2)

                for warrior in warriors:
                    friends = set()
                    for enemy in enemies[warrior]:
                        # enemies of my enemy are my friends
                        for friend in enemies[enemy]:
                            friends.add(friend)
                            if enemies[warrior].intersection(friends):
                                response = "No"
                                break
                output_file.write("Case #{0}: {1}\n".format(case_number, response))

if __name__ == "__main__":
    main()
