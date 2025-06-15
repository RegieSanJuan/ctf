#!/usr/bin/env python3
import angr
import sys

# Create the project and load the binary
project = angr.Project("./angr-y_binary")

# Create a state based on the current loaded binary
state = project.factory.entry_state()

# Construct the simulation manager set with the current state
simmgr = project.factory.simulation_manager(state)

# Find the address to find and avoid
find = 0xFFFFAAAC
avoid = 0xFFFFAAAB

# Start exploring different inputs and hopefully find the find function that we want
simmgr.explore(find=find,avoid=avoid)

# if there is a solution,
if simmgr.found[0]:
    print("found a solution")
    # Print out the input that Angr had found
    print(simmgr.found[0].posix.dumps(sys.stdin.fileno()))
else:
    print("No found solutions")