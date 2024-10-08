# This file is the main file that calls function to perform seismic design  # noqa: INP001, D100
# Users need to specify the system argument in this file.
# Users also need to specify the variables in "global_variables.py"

# The reason why I create this "redundant" file is to perform seismic
# design for a bunch of buildings (not a single one)

##########################################################################
#                       Relevant Publications                            #
##########################################################################

# Add relevant publications below

##########################################################################
#                       Load Necessary Packages                          #
##########################################################################

import time

from global_variables import baseDirectory
from seismic_design import seismic_design

# Count the starting time of the main program
start_time = time.time()

# ********************* Revised for Using System Argument ****************
# start_id = sys.argv[1]
# end_id = sys.argv[2]
# step_id = sys.argv[3]
# for id in range(int(start_id), int(end_id), int(step_id)):
#     building_id = 'Building_' + str(id)
#     print("Design for building ID = ", building_id)
#     seismic_design(building_id, base_directory)
# ********************* Revision Ends Here *******************************

# ********************* Single Building Case Ends Here *******************
IDs = [11]
for id in IDs:  # noqa: A001
    building_id = 'Test' + str(id)
    print('Design for Building ID = ', building_id)  # noqa: T201
    seismic_design(building_id, baseDirectory)

# ********************* Single Building Case Ends Here *******************

end_time = time.time()

print('Running time is: %s seconds' % round(end_time - start_time, 2))  # noqa: T201, UP031
