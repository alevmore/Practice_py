from pathlib import Path

from colorama import Fore, Back, Style

directory = Path('./picture')
if directory.exists():
    if directory.is_dir():
        print (Fore.GREEN + 'the main folder is: ./picture')
        for path in directory.iterdir():
            if path.is_dir():
                print (Fore.GREEN + 'the subfolder inside the main folder is: ./logo')
                for fol in path.iterdir():
                    print (Fore.RED + f'{fol}')
            else:
                    print (Fore.BLUE + f'{path}')
else:
    print (Style.RESET_ALL + f'The folder {directory} is not found')


   








