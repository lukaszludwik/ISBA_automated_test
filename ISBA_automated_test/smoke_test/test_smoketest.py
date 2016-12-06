import unittest
import psutil

from isbaoperations.operations import *


class IsbaSmoketests(unittest.TestCase):
    def setUp(self):
        run_isba()

    def test_run_isba(self):
        """
        INT50-54 [SMOKE TEST AUTOMATED] Run ISBA
        Verify whether can run ISBA application.
        """

        self.assertTrue("ISBA.exe" in [psutil.Process(i).name for i in psutil.get_pid_list()],
                        "ISBA process is running")
        self.assertTrue(is_isba_running(), "ISBA process is running")
        #   TODO make sure that the ISBA main window is visible

    def tearDown(self):
        # kill ISBA
        kill_isba()


if __name__ == '__main__':
    unittest.main()
