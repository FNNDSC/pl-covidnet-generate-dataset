
from unittest import TestCase
from unittest import mock
from covidnet_generate_dataset.covidnet_generate_dataset import Covidnet_generate_dataset


class Covidnet_generate_datasetTests(TestCase):
    """
    Test Covidnet_generate_dataset.
    """
    def setUp(self):
        self.app = Covidnet_generate_dataset()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')