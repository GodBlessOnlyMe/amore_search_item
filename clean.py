"""
For experiment, stop all containers and then remove them
"""

import os

# Stop all containers
stop_all_containers = 'docker stop $(docker ps -a -q)'
os.system(stop_all_containers)

# Remove all containers
remove_all_containers = 'docker rm $(docker ps -a -q)'
os.system(remove_all_containers)
