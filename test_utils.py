import utils as u

def test_add():
    assert u.add(2,3)==5

def test_sub():
    assert u.sub(3,2)==1

def test_mul():
    assert u.mul(2,3)==6

def test_div():
    assert u.div(6,2)==3

def test_mod():
    assert u.mod(7,3)==1

def test_power():
    assert u.power(2,3)==8

def test_floor_div():
    assert u.floor_div(7,3)==2

def test_sqrt():
    assert u.sqrt(9)==3

def test_factorial():
    assert u.factorial(5)==120

def test_absolute():
    assert u.absolute(-5)==5

def test_maximum():
    assert u.maximum(3,5)==5

def test_minimum():
    assert u.minimum(3,5)==3