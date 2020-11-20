"""
Eric Meehan
2020-11-20

Queue To Do
"""

def SequentialXOR(n):
    # Executing an XOR over sequential numbers starting with 1 returns a pattern of n, 1, n+1, 0
    # This function simulates this pattern
    switch = [n, 1, n + 1, 0]
    return switch[n % 4]

def Table(Start, Length):
    # Defines the end points for each row of the table
    return [Start + (Length * (i + 1) - (i + 1)) for i in range(Length)]
    
def XORRows(Start, End):
    # Finds the XOR for a row by performing the operation XOR(XOR(1 - StartOfRow), XOR(1 - EndOfRow))
    """
    Given that an XOR between any number and itself is 0, and an XOR between any number and 0 is itself, This function finds the cumulative XOR quickly by using the pattern defined in SequentialXOR to XOR the Start and End of each row - the results of which are a negation of the overlapping numbers (1 - Start).
     """
    if Start > 0:
        Start -= 1
    return SequentialXOR(Start) ^ SequentialXOR(End)
    
def main():
    # Generate the table
    table = Table(17, 4)
    print(table)
    # Create the cumulative XOR checksum
    CumulativeXOR = 0
    # Use the SequentialXOR function on each row, combining the result with the CumulativeXOR
    for i in range(4):
        CumulativeXOR ^= XORRows((17 + (4 * i)), table[i])
    # Print the result
    print(CumulativeXOR)

main()
