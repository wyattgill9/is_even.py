def write_is_even(filename):
    with open(filename, 'w') as file:
        file.write("def is_even(x):\n")
        
        for i in range(1, 10000):  
            if i % 2 == 1:
                file.write(f"    if x == {i}:\n")
                file.write(f"        return False\n")
            else:
                file.write(f"    if x == {i}:\n")
                file.write(f"        return True\n")
        file.write("    return False\n")
        file.write("print(is_even(10001))")

write_is_even('is_even.py')
