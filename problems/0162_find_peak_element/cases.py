METHOD = "findPeakElement"


def check(output, expected, args):
    """Any peak index is accepted: strictly greater than both neighbours, with nums[-1] = nums[n] = -inf."""
    nums = args[0]
    if isinstance(output, bool) or not isinstance(output, int) or not 0 <= output < len(nums):
        return False
    left = nums[output - 1] if output > 0 else float("-inf")
    right = nums[output + 1] if output + 1 < len(nums) else float("-inf")
    return nums[output] > left and nums[output] > right


CASES = [
    dict(args=([1, 2, 3, 1],), expected=2),
    dict(args=([1, 2, 1, 3, 5, 6, 4],), expected=5),
    dict(args=([-2147483648],), expected=0),
    dict(args=([1, 2, 3, 4, 5],), expected=4),
    dict(args=([5, 4, 3, 2, 1],), expected=0),
    dict(args=([1, 3, 2, 4, 1],), expected=1),
]
