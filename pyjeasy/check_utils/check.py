# import os, sys
import printj


def check_value(value, check_from, raise_exception_on_fail: bool = True, verbose: bool = True) -> bool:
    if value in check_from:
        return True
    else:
        if verbose:
            message = f'{value} is not valid.\n\
                Valid options are {check_from}.'
            printj.red(message)
        if raise_exception_on_fail:
            raise Exception
        return False
