import unittest
from solver import main
import numpy as np 

class CahnHilliardTests(unittest.TestCase):

    def test_main(self):
        """ Test the main function
        """
        
        # run a short simulation
        main.main(["--timesteps", "10", 
                   "--n_elements", "50", 
                   "--output", "none"])
    
    def test_read_input(self):
        """ Test the read_input function
        """

        args = ["--timesteps", "500", 
                "--timestep_value", "0.001",
                "--n_elements", "50", 
                "--periodic", 
                "--diffusion_coeff", "1.5", 
                "--boundary_coeff", "1.5", 
                "--output", "plot"]

        input_dict = main.read_input(args)

        self.assertEqual(input_dict["timesteps"], 500)
        self.assertEqual(input_dict["n_elements"], 50)
        self.assertEqual(input_dict["boundary"], "wrap")
        self.assertEqual(input_dict["diffusion_coeff"], 1.5)
        self.assertEqual(input_dict["boundary_coeff"], 1.5)
        self.assertEqual(input_dict["output"], "plot")
        self.assertEqual(input_dict["timestep_value"], 0.001)

    def test_generate_initial_config(self):
        """ Test the generate_initial_config function
        """

        input_dict = {"n_elements": 250}
        system_array = main.generate_initial_config(input_dict)
        
        # array is the correct size
        self.assertEqual(system_array.shape[0], input_dict["n_elements"])
        self.assertEqual(system_array.shape[1], input_dict["n_elements"])

        # all array values are valid
        self.assertTrue(np.max(system_array) < 1.0)
        self.assertTrue(np.min(system_array) > -1.0)
    
    def test_calculate_du_dt(self):
        """ Test the calculation of the time derivative of the concentration
        """
        
        input_dict = main.read_input([])
        initial_array = main.generate_initial_config(input_dict)

        new_array = main.calculate_du_dt(initial_array, input_dict)

        end_array = initial_array + input_dict["timestep_value"] * new_array

        #self.assertTrue(np.max(end_array) < 1.0)
        #self.assertTrue(np.min(end_array) > -1.0)

