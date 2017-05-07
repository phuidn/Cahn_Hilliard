"""
Basic functions for Cahn-Hilliard solver
"""

import argparse
import sys
import numpy as np

def main(argv):
    """The Main function, calls everything else
    """

    parameter_dict = read_input(argv)

    system_array = generate_initial_config(parameter_dict)

    return 0


def read_input(argv):
    """Reads command line input provided by user.

    Args:
        argv - the command line argument to the program, with the program name
        removed

    Returns:
        A dict mapping given args to their values
    """

    parser = argparse.ArgumentParser(description="Integrate the 2d Cahn-Hilliard equation")

    parser.add_argument("--timesteps", type=int, default=1000,
                        help="set the number of timesteps to run the simulation for")
    parser.add_argument("--n_elements", type=int, default=250,
                        help="set the number of elements N in the NxN domain")
    parser.add_argument("--periodic", help="Use periodic boundaries",
                        action="store_true")
    parser.add_argument("--diffusion_coeff", type=float, default=1.0,
                        help="set the diffusion coefficient")
    parser.add_argument("--boundary_coeff", type=float, default=1.0,
                        help="set the boundary coefficient")

    arguments = parser.parse_args(argv)

    return vars(arguments)

def generate_initial_config(parameter_dict):
    """Generates the initial configuration for the system, a numpy array of
    random numbers with values between -1.0 and 1.0

    Args:
        parameter_dict - the dictionary of parameters defined by the user
        as command line options (or taking their default values)

    Returns:
        a numpy array
    """

    dimension = parameter_dict["n_elements"]

    return np.random.ranf((dimension, dimension)) * 2.0 - 1.0


if __name__ == "__main__":
    main(sys.argv[1:])
