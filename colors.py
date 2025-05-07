from colorama import just_fix_windows_console, Fore, Style

# initialize colorama once 
just_fix_windows_console()

# Text colors
BLACK   = Fore.BLACK
RED     = Fore.RED
GREEN   = Fore.GREEN
YELLOW  = Fore.YELLOW
BLUE    = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN    = Fore.CYAN
WHITE   = Fore.WHITE

# Text styles
RESET     = Style.RESET_ALL
BOLD      = Style.BRIGHT     
UNDERLINE = "\033[4m"        
REVERSED  = "\033[7m"       

def colorize(text: str, *effects: str) -> str:
    effect_sequence = ''.join(effects) # join effects, for example: "\033[4m\033[7m" (UNDERLINE and REVERSED)
    
    return f"{effect_sequence}{text}{RESET}"