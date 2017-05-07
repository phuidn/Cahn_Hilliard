"""
Basic functions for Cahn-Hilliard solver
"""

import argparse
import sys
import numpy as np
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

def main(argv):
    """The Main function, calls everything else
    """

    # read command line inputs
    parameter_dict = read_input(argv)

    # generate initial system configuration
    system_array = generate_initial_config(parameter_dict)

    n_timesteps = parameter_dict["timesteps"]

    # main simulation loop over timesteps
    for i in xrange(n_timesteps):
        print "timestep {0: d}".format(i)

        dt = parameter_dict["timestep_value"]

        # calculate system for the current timestep
        du_dt = calculate_du_dt(system_array, parameter_dict)

        system_array += dt * du_dt

    plt.imshow(system_array)
    plt.show()
        
        # output data

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

    parser.add_argument("--timesteps", type=int, default=5000,
                        help="set the number of timesteps to run the simulation for")
    parser.add_argument("--timestep_value", type=float, default=0.005,
                        help="set the duration of each timestep")
    parser.add_argument("--n_elements", type=int, default=150,
                        help="set the number of elements N in the NxN domain")
    parser.add_argument("--periodic", help="Use periodic boundaries",
                        dest="boundary", action="store_const", 
                        const="wrap", default="reflect")
    parser.add_argument("--diffusion_coeff", type=float, default=2.0,
                        help="set the diffusion coefficient")
    parser.add_argument("--boundary_coeff", type=float, default=1.5,
                        help="set the boundary coefficient")
    parser.add_argument("--output", type=str, default="default", 
                        choices=["plot", "print", "none"],
                        help="set the output format")

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

def calculate_du_dt(system, parameter_dict):
    """ Calculate the time derivative of the system in its current state

    Args:
        system - the current system, a 2d numpy array
        parameter_dict - the dictionary of parameters defined by the user

    Returns
        a numpy array of the same dimension as the system
    """

    D_coeff = parameter_dict["diffusion_coeff"]
    b_coeff = parameter_dict["boundary_coeff"]
    
    potential_component = system**3 - system
    boundary_component = b_coeff * filters.laplace(system, mode = parameter_dict["boundary"])

    return D_coeff * filters.laplace(potential_component - boundary_component, mode = parameter_dict["boundary"])


if __name__ == "__main__":
    main(sys.argv[1:])
