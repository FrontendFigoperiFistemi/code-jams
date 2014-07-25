import logging
logging.basicConfig(filename='975485.log', level=logging.DEBUG)

log = logging.getLogger(__name__)
hallway = range(1, 101)

class bot(object):
    def __init__(self, name, hallway):
        self.__name__ = name
        self.name = name
        if name == "orange":
            self.short_name = "O"
        elif name == "blue":
            self.short_name = "B"
        else:
            log.error("bot name can be orange or blue")
            raise
        self.hallway = hallway
        self.position = 1

    def press_button(self, buttons):
        next_button, index = self._get_first_button(buttons)
        if not next_button:
            log.info("{0}: finished".format(self.name))
            return False
        # print "{0} moving to {1}, position: {2}".format(self.name, next_button, self.position)
        if next_button < self.position:
            log.debug("{0}: moving backward".format(self.name))
            self.position -= 1
            return False
        elif next_button > self.position:
            log.debug("{0}: moving forward".format(self.name))
            self.position += 1
            return False
        elif next_button == self.position:
            if index == 1:
                log.debug("{0}: pressing button".format(self.name))
                return True  # button pressed
            else:
                log.debug("{0}: waiting".format(self.name))
                # waiting for the other robot move
                return False
        raise

    def _get_first_button(self, buttons):
        index = 1
        for button in buttons:
            if button[0] == self.short_name:
                return button[1], index
            index += 1
        return None, index

def parse_input(input_string):
    parts = input_string.split()
    number_of_buttons = parts[0]
    coordinates = []
    for index in range(1, len(parts), 2):
        bot_name = parts[index]
        coordinate = int(parts[index + 1])
        coordinates.append((bot_name, coordinate))
    return coordinates

def main():
    case_number = 1
    orange = bot
    with open("A-large-practice.in") as input_file:
        with open("output.txt", "w") as output_file:
            number_of_tt = int(input_file.readline())
            print number_of_tt
            for case in input_file:
                log.debug("processing input {0}".format(case))
                print "processing input", case
                coordinates = parse_input(case)
                button_to_push = coordinates
                orange = bot("orange", hallway)
                blue = bot("blue", hallway)
                seconds = 0
                while len(button_to_push):
                    print "_________________________________"
                    print button_to_push
                    print "bots: {0} {1}, {2} {3}".format(orange.name, orange.position, blue.name, blue.position)
                    orange_pressed = orange.press_button(button_to_push)
                    blue_pressed = blue.press_button(button_to_push)
                    if orange_pressed or blue_pressed:
                        # a button has been pressed
                        button_to_push = button_to_push[1:]
                    seconds += 1
                output_file.write("Case #{0}: {1}\n".format(case_number, seconds))
                case_number += 1


if __name__ == "__main__":
    main()
