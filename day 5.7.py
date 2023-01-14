MAX = 26
# Function that return true if frequency
# of all the present characters is at least k
def atLeastK(freq, k):
    for i in range(MAX):

        # If the character is present and
        # its frequency is less than k
        if (freq[i] != 0 and freq[i] < k):
            return False;
    return True;
# Function to set every frequency to zero
def setZero(freq):
    for i in range(MAX):
        freq[i] = 0;
# Function to return the length of the longest
# sub-string such that it contains every
# character at least k times
def findlength(string, n, k):
    # To store the required maximum length
    maxLen = 0;
    freq = [0] * MAX;
    # Starting index of the sub-string
    for i in range(n):
        setZero(freq);
        # Ending index of the sub-string
        for j in range(i, n):
            freq[ord(string[j]) - ord('a')] += 1;
            # If the frequency of every character
            # of the current sub-string is at least k
            if (atLeastK(freq, k)):
                # Update the maximum possible length
                maxLen = max(maxLen, j - i + 1);
    return maxLen;
# Driver code
if __name__ == "__main__":
    string = "aaabb";
    n = len(string);
    k = 3;
    print(findlength(string, n, k));