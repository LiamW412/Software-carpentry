import numpy as np
import numpy.testing as npt
from inflammation.models import daily_max


data = np.loadtxt(fname = 'data/inflammation-01.csv', delimiter=',')

daily_max([[1,2], [3,4], [5,6]])

# test_input_pass = np.array([[1,2], [3,4], [5,6]])
# test_input_fail = np.array([[2,0], [3,4], [5,6]])
# test_result = np.array([3,4])

# npt.assert_array_equal(daily_mean(test_input_fail), test_result)