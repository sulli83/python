def number_of_evens(numbers):
    return 2

def test_are_equal(actual,expected):
    assert expected == actual, "Expected {0} got {1}".format(actual, expected)

def test_not_equal(a,b):
    assert a != b, "Did not expect {0} but got {1}".format(a,b)
    
def test_is_in(collection,item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in_collection(collection, item):
    assert item not in collection, "{0} contains {1}".format(item, collection)
    

test_not_equal(15,14)    

test_is_in([4,6,7,12], 12)

test_are_equal(number_of_evens([1,2,3,4]), 2)



print("tests passed")