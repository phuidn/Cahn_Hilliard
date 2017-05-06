import unittest
from solver import main

class CahnHilliardTests(unittest.TestCase):

    def test_main(self):
        """ Test the main function
        """
        
        main.main([])
    
    def test_read_input(self):
        """ Test the read input function
        """

        args = ["--timesteps", "500", "--n_elements", "50", "--periodic", "--diffusion_coeff", "1.5", "--boundary_coeff", "1.5"]
        input_dict = main.read_input(args)

        self.assertEqual(input_dict["timesteps"], 500)
        self.assertEqual(input_dict["n_elements"], 50)
        self.assertEqual(input_dict["periodic"], True)
        self.assertEqual(input_dict["diffusion_coeff"], 1.5)
        self.assertEqual(input_dict["boundary_coeff"], 1.5)


