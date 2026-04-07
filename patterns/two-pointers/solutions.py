"""
Two Pointers Pattern Solutions
==============================

Core two-pointer implementations and patterns
"""

# ============================================================================
# LC 3823: Reverse Letters Then Special Characters in a String
# ============================================================================

def reverseLettersAndSpecialCharacters(s: str) -> str:
    # Extract and reverse letters
    letters = [ch for ch in s if ch.isalpha()]
    letters.reverse()
    
    # Extract and reverse special characters
    specials = [ch for ch in s if not ch.isalpha()]
    specials.reverse()
    
    # Reconstruct
    result = []
    letter_idx = special_idx = 0
    
    for ch in s:
        if ch.isalpha():
            result.append(letters[letter_idx])
            letter_idx += 1
        else:
            result.append(specials[special_idx])
            special_idx += 1
    
    return ''.join(result)

# ============================================================================
# LC 3794: Reverse string prefix
# ============================================================================

def reversePrefix_twopointer(s: str, k: int) -> str:
    chars = list(s)
    left, right = 0, k - 1
    
    # Two pointers meet in middle
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)

# ============================================================================
# LC 283: Move Zeroes
# ============================================================================

def moveZeroes(nums: list[int]) -> None:
    """
    Move all zeroes to end while maintaining relative order of non-zero elements.
    Do not return anything, modify nums in-place instead.
    """
    # Pointer for next non-zero position
    next_non_zero = 0
    
    # Iterate through array
    for current in range(len(nums)):
        if nums[current] != 0:
            # Swap with next non-zero position
            nums[next_non_zero], nums[current] = nums[current], nums[next_non_zero]
            next_non_zero += 1