# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
'''
U
    Input -> text file
    Output -> print decoded text

    Rules
        Punctuation and spaces are immutable
        All input and output should be UPPERCASE

    Task
        Find the key to decode the cipher
        Decode it
        Show the plain text

        Utilize frequency analysis to decode

P
    Bring over list of chars in order of most frequent use
    Create dict 
        key: alphabet chars (uppercase)
        value: percentage of use
    Match dict vs list letter percentages
    Decode into new string
    Print string

'''