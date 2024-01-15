import sys
##sys.path.append('../')
import colorama
from colorama import Fore, Back, Style
from enum import Enum

################ Loglevels ################
class Loglevels(Enum):
    ALL         = 0
    DEBUG       = 1
    INFO        = 2
    WARNING     = 3
    ERROR       = 4
    CRITICAL    = 5

################ Logger ################
class Logger:
    _logLevel = False

    @property
    def LOG_LEVEL(self):
        return self._logLevel
    
    @LOG_LEVEL.setter
    def LOG_LEVEL(self, value):
        self._logLevel = value


    def __init__(self, log_level=0) -> None:
        self._logLevel=int(log_level)

    def OK(self, message = ""):
        if self.LOG_LEVEL <= Loglevels.INFO.value:
            print(f"[ {Fore.GREEN}OK {Fore.RESET}] {message}")

    def DEBUG(self, message = ''):
        if self.LOG_LEVEL <= Loglevels.DEBUG.value:
            print(f"[{Fore.BLUE}DBG.{Fore.RESET}] {message}")

    def INFO(self, message = ''):
        if self.LOG_LEVEL <= Loglevels.INFO.value:
            print(f"[{Fore.WHITE}INFO{Fore.RESET}] {message}")
    
    def WARING(self, message = ''):
        if self.LOG_LEVEL <= Loglevels.WARNING.value:
            print(f"[{Fore.YELLOW}WARN{Fore.RESET}] {message}")

    def ERROR(self, message = ''):
        if self.LOG_LEVEL <= Loglevels.ERROR.value:
            print(f"[{Fore.RED}ERR.{Fore.RESET}] {Fore.RED}{message}{Fore.RESET}")

    def CRITICAL(self, message = ''):
        if self.LOG_LEVEL <= Loglevels.CRITICAL.value:
            print(f"[{Fore.MAGENTA}CRIT{Fore.RESET}] {Fore.MAGENTA}{message}{Fore.RESET}")
    
    