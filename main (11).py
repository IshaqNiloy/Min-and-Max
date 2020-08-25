import numpy

def numpy_min(my_arr):
    #The tool min returns the minimum value along a given axis.
    #'0' means vertically down
    #'1' means horizontally across
    return numpy.min(my_arr,axis = 1)

def numpy_max(my_arr):
    #The tool max returns the maximum value along a given axis.
    #By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.
    print(numpy.max(my_arr, axis = None))

if __name__ == '__main__':
    row, column = map(int, input().split())
    my_arr = numpy.array([input().strip().split() for _ in range(row)], int)
    numpy_max(numpy_min(my_arr))
