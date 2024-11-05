import sys
from pathlib import Path
import colorama
colorama.init(autoreset=True)

path=sys.argv[1]
def path_to_directory(path): 
   
    directory = Path(path)

    if directory.exists():
        if directory.is_dir():
            print (colorama.Fore.GREEN + 'the main folder is: {directory.name}')
            for folder in directory.iterdir():
                if folder.is_dir():
                    print (colorama.Fore.GREEN + 'the subfolder inside the main folder is: {folder.name}')
                    for fol in folder.iterdir():
                        print (colorama.Fore.RED + f'{fol.name}')
                else:
                    print (colorama.Fore.BLUE + f'{folder.name}')
    else:
        print (colorama.Style.RESET_ALL + f'The folder {directory.name} is not found')

        return path
path_to_directory(path=path)  


   








