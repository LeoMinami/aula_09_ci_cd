import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14
    
def test_soma():
    #given a value of 2 and 3
    value1 = 2
    value2 = 3
    #when we calculate the sum
    output = methods.sum_of_values(value1, value2)
    #then the sum should be 5
    assert output == 5

def test_sub():
    #given a value of 8 and 2
    value1 = 8
    value2 = 2
    #when we calculate the sub
    output = methods.sub_of_values(value1, value2)
    #then the sub should be 5
    assert output == 6

def test_mult():
    #given a value of 8 and 2
    value1 = 8
    value2 = 2
    #when we calculate the mult
    output = methods.mult_of_values(value1, value2)
    #then the mult should be 16
    assert output == 16

def test_div():
    #given a value of 8 and 2
    value1 = 8
    value2 = 2
    #when we calculate the div
    output = methods.div_of_values(value1, value2)
    #then the sum should be 4
    assert output == 4