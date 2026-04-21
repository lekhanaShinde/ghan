"""
Experiment 4: Bit Stuffing and Unstuffing
Demonstrates inserting and removing stuffed bits in binary data
"""


def bit_stuffing(data):
    """
    Insert a 0 after every sequence of five consecutive 1s.
    
    Args:
        data (str): Binary string to stuff
        
    Returns:
        str: Binary string with stuffed bits inserted
    """
    return data.replace("11111", "111110")


def bit_unstuffing(data):
    """
    Remove the stuffed 0 that appears after every sequence of five 1s.
    
    Args:
        data (str): Stuffed binary string
        
    Returns:
        str: Original binary string with stuffed bits removed
    """
    return data.replace("111110", "11111")


def main():
    """Main function to demonstrate bit stuffing and unstuffing."""
    
    # Get binary input from user
    binary_input = input("Enter binary data: ").strip()
    
    # Validate input
    if not all(c in '01' for c in binary_input):
        print("Error: Please enter only binary digits (0 and 1)")
        return
    
    # Apply bit stuffing
    stuffed_data = bit_stuffing(binary_input)
    
    # Apply bit unstuffing
    unstuffed_data = bit_unstuffing(stuffed_data)
    
    # Display results
    print("\n" + "="*50)
    print("BIT STUFFING RESULTS")
    print("="*50)
    print(f"Original Data:    {binary_input}")
    print(f"Stuffed Data:     {stuffed_data}")
    print(f"Unstuffed Data:   {unstuffed_data}")
    print(f"Verification:     {'✓ PASS' if unstuffed_data == binary_input else '✗ FAIL'}")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()



#Enter binary data: 111110110011