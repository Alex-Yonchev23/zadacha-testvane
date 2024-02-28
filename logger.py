# logger.py

class Logger:
    @staticmethod
    def log_operation(operation, x, y, result):
        with open("log.txt", "a") as log_file:
            log_file.write(f"{x} {operation} {y} = {result}\n")
