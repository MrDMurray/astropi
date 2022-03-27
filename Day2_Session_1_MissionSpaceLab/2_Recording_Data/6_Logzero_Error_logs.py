from logzero import logger, logfile
from pathlib import Path
from time import sleep

base_folder = Path(__file__).parent.resolve()
logfile(base_folder/"events.log")

try:
    
    # show logging of successful iterations...
    for i in range(3):
        logger.info(f"Loop number {i+1} started")
        sleep(1)
    
    # Let's now divided by zero and break the world just for the craic...
    print(48152342/0)

except Exception as e:
    logger.error(f'{e.__class__.__name__}: {e})')