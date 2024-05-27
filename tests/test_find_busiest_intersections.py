import unittest
import sys
import os

# เพิ่มเส้นทางของโฟลเดอร์โปรเจคไปยัง sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from find_busiest_intersections import find_busiest_intersections

class TestFindBusiestIntersections(unittest.TestCase):
    
    def test_single_busiest_intersection(self):
        data = {'A': 10, 'B': 20, 'C': 15}
        result = find_busiest_intersections(data)
        print("Result for test_single_busiest_intersection:", result)
        self.assertEqual(result, ['B'])
    
    def test_multiple_busiest_intersections(self):
        data = {'A': 10, 'B': 20, 'C': 20}
        result = find_busiest_intersections(data)
        print("Result for test_multiple_busiest_intersections:", result)
        self.assertEqual(result, ['B', 'C'])
    
    def test_no_intersections(self):
        data = {}
        result = find_busiest_intersections(data)
        print("Result for test_no_intersections:", result)
        self.assertEqual(result, [])
    
    def test_all_intersections_same_traffic(self):
        data = {'A': 10, 'B': 10, 'C': 10}
        result = find_busiest_intersections(data)
        print("Result for test_all_intersections_same_traffic:", result)
        self.assertEqual(result, ['A', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()

