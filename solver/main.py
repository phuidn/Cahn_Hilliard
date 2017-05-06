"""
Basic functions for Cahn-Hilliard solver
"""

import argparse
import sys


def main(argv):
    """The Main function, calls everything else
    """

    parameters = read_input(argv)

    return 0


def read_input(argv):
    """Reads command line input provided by user.

    Args:

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


if __name__ == "__main__":
    main(sys.argv[1:])
