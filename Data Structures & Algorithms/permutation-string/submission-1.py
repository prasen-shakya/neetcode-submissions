class Solution:
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        # Frequency arrays for characters 'a' to 'z'
        s1_freq = [0] * 26
        window_freq = [0] * 26
        
        # Initialize the frequency arrays
        for i in range(len1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1
        
        # Compare the initial window with s1's frequency
        if s1_freq == window_freq:
            return True
        
        # Sliding window
        for i in range(len1, len2):
            window_freq[ord(s2[i]) - ord('a')] += 1
            window_freq[ord(s2[i - len1]) - ord('a')] -= 1
            
            if s1_freq == window_freq:
                return True
        
        return False
