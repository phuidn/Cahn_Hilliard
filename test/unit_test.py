import unittest
from solver import main
import numpy as np 

class CahnHilliardTests(unittest.TestCase):

    def test_main(self):
        """ Test the main function
        """
        
        main.main([])
    
    def test_read_input(self):
        """ Test the read_input function
        """

        args = ["--timesteps", "500", "--n_elements", "50", "--periodic", "--diffusion_coeff", "1.5", "--boundary_coeff", "1.5"]
        input_dict = main.read_input(args)

        self.assertEqual(input_dict["timesteps"], 500)
        self.assertEqual(input_dict["n_elements"], 50)
        self.assertEqual(input_dict["periodic"], True)
        self.assertEqual(input_dict["diffusion_coeff"], 1.5)
        self.assertEqual(input_dict["boundary_coeff"], 1.5)

    def test_generate_initial_config(self):
        """ Test the generate_initial_config function
        """

        input_dict = main.read_input([])
        system_array = main.generate_initial_config(input_dict)
        
        # array is the correct size
        self.assertEqual(system_array.shape[0], input_dict["n_elements"])
        self.assertEqual(system_array.shape[1], input_dict["n_elements"])

        # all array values are valid
        self.assertTrue(np.max(system_array) < 1.0)
        self.assertTrue(np.min(system_array) > -1.0)
