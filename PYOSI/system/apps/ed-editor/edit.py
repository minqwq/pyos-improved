class SimpleEd:
    def __init__(self):
        self.buffer = []

    def load_file(self, filename):
        with open(filename, 'r') as f:
            self.buffer = f.readlines()
        print(f"{len(self.buffer)} lines loaded.")

    def print_buffer(self, start=0, end=None):
        if end is None:
            end = len(self.buffer)
        for i in range(start, end):
            print(f"{i + 1}: {self.buffer[i]}", end='')

    def insert_line(self, index, text):
        if index < 0 or index > len(self.buffer):
            print("Error: Invalid index")
        else:
            self.buffer.insert(index, text + "\n")
            print(f"Inserted line at {index + 1}")

    def delete_line(self, index):
        if index < 0 or index >= len(self.buffer):
            print("Error: Invalid index")
        else:
            removed = self.buffer.pop(index)
            print(f"Deleted line {index + 1}: {removed}", end='')

    def replace_line(self, index, text):
        if index < 0 or index >= len(self.buffer):
            print("Error: Invalid index")
        else:
            self.buffer[index] = text + "\n"
            print(f"Replaced line {index + 1}")

    def save_file(self, filename):
        with open(filename, 'w') as f:
            f.writelines(self.buffer)
        print(f"File saved to {filename}.")

    def command_loop(self):
        while True:
            cmd = input("")
            if cmd == 'q':
                break
            elif cmd.startswith('r '):
                filename = cmd.split(maxsplit=1)[1]
                self.load_file(filename)
            elif cmd == 'p':
                self.print_buffer()
            elif cmd.startswith('i '):
                _, index, text = cmd.split(maxsplit=2)
                self.insert_line(int(index) - 1, text)
            elif cmd.startswith('d '):
                index = int(cmd.split(maxsplit=1)[1]) - 1
                self.delete_line(index)
            elif cmd.startswith('s '):
                _, index, text = cmd.split(maxsplit=2)
                self.replace_line(int(index) - 1, text)
            elif cmd.startswith('w '):
                filename = cmd.split(maxsplit=1)[1]
                self.save_file(filename)
            else:
                print("Invalid command")

if __name__ == "__main__":
    editor = SimpleEd()
    editor.command_loop()
