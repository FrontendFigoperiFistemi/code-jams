import logging
from argparse import ArgumentParser

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    args = parser.parse_args()
    with open(args.input_file) as input_file:
        with open(args.output_file, "w") as output_file:
            total_cases = int(input_file.readline().strip())
            for case_number in range(1, total_cases + 1):
                existent_dirs = set()
                non_existent_dirs = set()
                created_dir = 0
                existent, non_existent = map(int, input_file.readline().strip().split())
                for i in range(existent):
                    for d in get_dirs(input_file.readline().strip()):
                        existent_dirs.add(d)
                for i in range(non_existent):
                    for d in get_dirs(input_file.readline().strip()):
                        if d in existent_dirs:
                            pass
                        else:
                            log.debug("creating dir {dir}".format(dir=d))
                            existent_dirs.add(d)
                            created_dir += 1
                log.debug("created {0}".format(created_dir))
                log.debug("existent: {ex}, non existent: {non_ex}".format(ex=existent, non_ex=non_existent))
                log.debug(existent_dirs)
                log.debug(non_existent_dirs)
                output_file.write("Case #{case_number}: {created_dir}\n".format(created_dir=created_dir,
                                                                              case_number=case_number))


def get_dirs(path):
    while path:
        to_yield = path
        path = "/".join(path.split("/")[:-1])
        yield to_yield

if __name__ == "__main__":
    # for dir in create_dir('/home/gcj/finals'):
    #     print dir
    main()
