def reverseBits(input_array):
    reversed_bits = []
    
    for i in range(len(input_array)-1, -1, -1):
        reversed_bits.append(input_array[i])
    
    if( len(input_array) == len(reversed_bits)):
        print('Hurrah! The lengths match!')
    else:
        print('Oops. The lengths do not match! Check your ranges.' )

    if(len(input_array) != 8):
        print('This is not a 32-bit integer...')

    return reversed_bits

reversed_bits = reverseBits(input_array)

print('I:', input_array)
print('O:',reversed_bits)