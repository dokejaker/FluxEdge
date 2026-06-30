# test_fluxedge.py
"""
Tests for FluxEdge module.
"""

import unittest
from fluxedge import FluxEdge

class TestFluxEdge(unittest.TestCase):
    """Test cases for FluxEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FluxEdge()
        self.assertIsInstance(instance, FluxEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FluxEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
