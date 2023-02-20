# LinkedIn Learning Course: Advanced Python by Joe Marini
# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string!"
    print(s)

   # print(s+b) # should result in a TypeError because you bytes are not converted to a str -- should "decode" the bytes into a string, can use the decode method to do so

    s2 = b.decode('utf-8')
    print(s+s2)

main()
