import os
from . import config

def check_output_size():
    """Check output folder size"""

    # In base 10
    MB_CONVERSION = 1000000
    total_sum = 0
    for root, _, files in os.walk("output"):
        for name in files:
            total_sum = total_sum + os.path.getsize(os.path.join(root, name))
    
    size_in_megabytes = total_sum/MB_CONVERSION

    # If it's bigger than 1 GiB in base 2, return error
    if size_in_megabytes > 1000:
        exit_code = config.SIZE_ERROR
    # Return warning if it surpassed 80% of 1GB
    elif size_in_megabytes > 800:
        exit_code = config.WARNING
    else:
        exit_code = config.SUCCESS
    
    return exit_code, size_in_megabytes