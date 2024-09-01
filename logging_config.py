import logging
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

EMOJIS = {
    'INFO': 'ℹ️',
    'DEBUG': '🐞',
    'WARNING': '⚠️',
    'ERROR': '❌',
    'CRITICAL': '🔥'
}

class CustomFormatter(logging.Formatter):
    FORMAT = "[{emoji} {color}{levelname:<8}{reset}] {asctime} => {message}"
    
    COLORS = {
        'DEBUG': Fore.CYAN + Style.BRIGHT,
        'INFO': Fore.LIGHTBLUE_EX + Style.BRIGHT,
        'WARNING': Fore.YELLOW + Style.BRIGHT,
        'ERROR': Fore.RED + Style.BRIGHT,
        'CRITICAL': Fore.MAGENTA + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE + Style.BRIGHT)
        log_emoji = EMOJIS.get(record.levelname, '')
        
        self.datefmt = "%Y-%m-%d %H:%M:%S"
        
        log_msg = self.FORMAT.format(
            emoji=log_emoji,
            color=log_color,
            levelname=record.levelname,
            asctime=self.formatTime(record, self.datefmt),
            message=record.getMessage(),
            reset=Style.RESET_ALL
        )

        return log_msg

class FilterLogs(logging.Filter):
    def filter(self, record):
        # Modify the condition to fit the logs you want to filter out
        if 'discord.gateway' in record.name:
            return False
        return True

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()]
    )
    
    logger = logging.getLogger()
    for handler in logger.handlers:
        handler.setFormatter(CustomFormatter())
        handler.addFilter(FilterLogs())
