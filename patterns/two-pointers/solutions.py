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

# ============================================================================
# LC 26: Remove Duplicates from Sorted Array
# ============================================================================

def removeDuplicates(nums: list[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    Return the number of unique elements.
    """
    if not nums:
        return 0
    
    # Slow pointer for unique elements
    slow = 0
    
    # Fast pointer to iterate
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    # Return number of unique elements
    return slow + 1

# ============================================================================
# LC 27: Remove Element
# ============================================================================

def removeElement(nums: list[int], val: int) -> int:
    """
    Remove all occurrences of val in nums in-place.
    Return the number of elements not equal to val.
    """
    # Pointer for next position to place non-val element
    next_pos = 0
    
    # Iterate through array
    for current in range(len(nums)):
        if nums[current] != val:
            # Place non-val element at next position
            nums[next_pos] = nums[current]
            next_pos += 1
    
    # Return count of non-val elements
    return next_pos