class Solution:
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        # Frequency arrays for characters 'a' to 'z'
        s1_freq = [0] * 26
        window_freq = [0] * 26
        
        # Use one loop to initialize and slide the window
        for i in range(len2):
            if i < len1:
                s1_freq[ord(s1[i]) - ord('a')] += 1
                window_freq[ord(s2[i]) - ord('a')] += 1
            else:
                # Slide the window: add the new character and remove the old character
                window_freq[ord(s2[i]) - ord('a')] += 1
                window_freq[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Compare the frequency arrays once the initial window is set up
            if i >= len1 - 1 and s1_freq == window_freq:
                return True
        
        return False