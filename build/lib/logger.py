import datetime
from os import stat
from pathlib import Path
from rich.console import Console
from inspect import getframeinfo, stack

class Log:
    def __init__(self):

        self.COLORS = {
            "DEBUG":"green bold",
            "INFO":"bright_magenta bold",
            "SUCCESS":"bright_green bold",
            "WARNING":"bright_yellow bold",
            "ERROR":"bright_red bold",
            "CRITICAL":"black bold on bright_red",
            "TRACEBACK":"black bold on bright_red",
            "filename":"purple4 italic"
        }

        self.console = Console(markup=True, log_time=False, record=True)


    def log(self, level, text):
        caller = getframeinfo(stack()[2][0])
        filename = Path(caller.filename).name
        
        log_format = f'[{datetime.datetime.now()}] | [{self.COLORS.get(level)}]{level:^10}[/] | {text} [{self.COLORS.get("filename")}]\[{filename}:{caller.lineno}][/]'
        
        self.console.print(log_format)

        text_ = self.console.export_text()

        with open(f'src/data/logs/console_{datetime.datetime.now().strftime("%Y-%m-%d")}.log', 'a') as file:
            if stat(file.name).st_size >= 1_000_00_000:
                file.truncate(0)
            else:
                file.write(text_)


    def debug(self, text):
        self.log('DEBUG', text)


    def info(self, text):
        self.log('INFO', text)


    def success(self, text):
        self.log('SUCCESS', text)


    def warning(self, text):
        self.log('WARNING', text)


    def error(self, text):
        self.log('ERROR', text)


    def critical(self, text):
        self.log('CRITICAL', text)


