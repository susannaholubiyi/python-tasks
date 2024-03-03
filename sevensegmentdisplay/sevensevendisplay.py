class SevenSevenDisplay:
    def __init__(self):
        self.different_segments = []

    @staticmethod
    def validate_input(input_message):
        for character in input_message:
            if character != "0" and character != "1":
                raise ValueError("Invalid input")

    def print_out_segment(self, input_message: str):
        if self.check_if_on(input_message):
            self.validate_input(input_message)
            self.different_segments += input_message
            self.display_each_output_with()

    @staticmethod
    def check_if_on(input_message):
        return input_message[-1] == "1"

    def display_each_output_with(self):
        if self.different_segments[0] == "1":
            print("# # # #")
        if self.different_segments[5] == "1" and self.different_segments[1] == "1":
            for number in range(4):
                print("#     #")
        elif self.different_segments[5] == "1" and self.different_segments[1] == "0":
            for number in range(4):
                print("#      ")
        elif self.different_segments[5] == "0" and self.different_segments[1] == "1":
            for number in range(4):
                print("      #")
        if self.different_segments[6] == "1":
            print("# # # #")
        if self.different_segments[4] == "1" and self.different_segments[2] == "1":
            for number in range(4):
                print("#     #")
        elif self.different_segments[4] == "1" and self.different_segments[2] == "0":
            for number in range(4):
                print("#      ")
        elif self.different_segments[4] == "0" and self.different_segments[2] == "1":
            for number in range(4):
                print("      #")
        if self.different_segments[3] == "1":
            print("# # # #")


seven_segment = SevenSevenDisplay()
seven_segment.print_out_segment("01100111")
