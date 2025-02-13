def __init__(self):
    print("weeeeee thanks ma'am")
    
def add(*add_args: float)-> float:
    """adds all the numbers passed"""
    
    print(sum(add_args))
    
def mult(*mult_args: float) -> float:
    """Multiply all the numbers passed"""
    
    result = 1
    for n in mult_args:
        result *= n
    print(result)

    
def subt(*subt_args: float) -> float:
    result = subt_args[0]
    for n in subt_args[1:]:
        result -= n
    print(result)

def div(*div_args: float) -> float:
    result = div_args[0]
    for n in div_args[1:]:
        result /= n
    print(result)