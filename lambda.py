operations={'add':lambda x,y:x+y,
            'subtract':lambda x,y:x-y,
            'multiply':lambda x,y:x*y,
            'divide':lambda x,y:x/y,
            'modulus':lambda x,y:x%y,
            'exponentiation':lambda x,y:x**y,
            'floor division':lambda x,y:x//y}
x,y=10,5
for op_name,op in operations.items():
    print(f"{op_name.capitalize()}of {x} and {y}:{op(x,y)}")
    