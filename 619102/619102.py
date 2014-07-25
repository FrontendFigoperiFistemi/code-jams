from argparse import ArgumentParser
import logging

from itertools import combinations

# logging.basicConfig(filename="619102.log", level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    with open(args.input) as input_file:
        with open(args.output, "w") as output_file:
            T = int(input_file.readline().rstrip())
            log.debug("number of cases: {0}".format(T))
            for case_number in range(1, T + 1):
                N = int(input_file.readline().rstrip())
                wires = []
                intersections = 0
                for wire_number in range(1, N + 1):
                    wire = map(int, input_file.readline().rstrip().split())
                    log.debug("Case #{0}: wire_number: {1}, wire: {2}".format(case_number, wire_number, wire))
                    wires.append(wire)
                log.debug(wires)
                for couple in combinations(wires, 2):
                    if has_intersections(*couple):
                        intersections += 1
                output_file.write("Case #{0}: {1}\n".format(case_number, intersections))

def has_intersections(rope1, rope2):
    if rope1[0] < rope2[0] and rope1[1] > rope2[1]:
        return True
    if rope1[0] > rope2[0] and rope1[1] < rope2[1]:
        return True
    else:
        return False
if __name__ == "__main__":
    main()
