# VectorPy
A simple R3 vector (also known as a reimplimentation of the vector class from vpython which can be used without the nessesity to spin up wx or a webserver)

## Installation
vectorpy can be installed directly from the cloned source of this repository, or from pypi.
```bash
git clone https://github.com/tboudreaux/vectorpy.git
cd vectorpy
python setup.py install
```
or
```bash
pip install vectorpy
```

## Example
Here is a simple example
```python
    from vectorpy import vector

    vector_one = vector(2.3, 0, -5.6)
    vector_two = vector()   # intialize the vector <0, 0, 0>

    vector_three = vector_one + vector_two  # vector addition

    vector_four = vector_one * vector_two # Dot Product

    vector_five = vector_one.cross(vector_two) # v1 x v2 (cross product)

    vector_six = vector_one * 5 # Scaler multiplication

    vector_list = vector_one.aslist()   # cast vector to python list

    length_of_V1 = abs(vector_one)  # Magnitude of vector
    
    print('Vector three is: {}, vector four is: {}'.format(vector_three, vector_four))


```
There we go.
