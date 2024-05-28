# Smart City Traffic

This project provides a function to find the busiest intersections in a smart city based on vehicle count data.

## Function

### find_busiest_intersections

This function takes a dictionary where keys are intersection names and values are the number of vehicles. It returns a list of intersections with the highest number of vehicles.

## Usage

```python
from find_busiest_intersections import find_busiest_intersections

data = {'A': 10, 'B': 20, 'C': 15}
print(find_busiest_intersections(data))  # Output: ['B']
