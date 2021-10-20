'''
This program tests the compound interest calculator
'''

from calc import monthly_compounding

def test_tautology():
    assert 3 == 3

# Test that investing no money generates no returns
def test_zeroes():
    # Initialize some user inputs
    initial = 0
    monthly = 0
    years = 0
    annual_rate = 0
    # calculate a final sum
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)
    # do an actual test
    assert final_sum == 0
    
def test_cash():
    initial = 1000
    monthly = 100
    years = 10
    annual_rate = 0
    # calculate a final sum
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)
    # do an actual test
    assert final_sum == 13000
    
def test_cash():
    initial = 1000
    monthly = 100
    years = 10
    annual_rate = 0
    # calculate a final sum
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)
    # do an actual test
    assert final_sum == 13000
    
def test_interest():
    initial = 1000
    monthly = 100
    years = 2/12
    annual_rate = 12
    # calculate a final sum
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)
    # do an actual test
    assert final_sum == 1221.1