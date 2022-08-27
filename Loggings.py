"""Loggings :- Used to Log, Trace and make Custom loggers."""
import logging

logging.basicConfig(level=logging.DEBUG, filename="Logger", filemode="w",                  # The type of logging, the file it will log in and mode.
                    format="\n%(asctime)s - %(name)s - %(levelname)s - %(message)s",       # The format it'll print in
                    datefmt="%d:%m:%Y %H:%M:%S")                                           # Format of date. %D prints the date

logging.debug("Debug message")                                                      # Debug - Info - Warnings - Error - Critical
logging.info("Info message")                                                        # If printed any of the above, it'll print the ones after it.
logging.warning("Warning message")                                                  # By printing Debug, it'll print all the loggings.
logging.error("Error message")
logging.critical("Critical message")                                                # All of ths will be printed in a text file which was specified.

# Trace
import traceback
try:
    #var = 1 / 0
    #var2 = 1 + "2"
    var3 = [1, 2]
    var4 = var3[2]
except ZeroDivisionError as e:
    logging.error(F"Tried to do {e}", exc_info= True)                             # "exc_info = " could be anything
except TypeError as t:
    logging.exception("Hi")
except IndexError as i:
    logging.warning(f"{i} %s", traceback.format_exc())

# Custom Logger with handlers and formatters.
log = logging.getLogger(__name__)                                                 # ("") mentions the name of the file it will go into.
logging.info("Hi!")                                                               # If filename isn't mentioned, it'll go to the file mentioned in basicConfig.

handle = logging.FileHandler("Logger_2", mode="w")                                     # Gives custom filename. If file doesn't exist, it'll crreate one.
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")     # Custom format
handle.setLevel(logging.INFO)
handle.setFormatter(format)                                                            # Gives the format to the file mentioned
log.addHandler(handle)
log.info("New Logger.")

handle2 = logging.StreamHandler()                     # [1]                            # StreamHandler prints out in the terminal
handle2.setFormatter(format)
handle2.setLevel(logging.WARNING)
log.addHandler(handle2)
log.warning("Warning")
