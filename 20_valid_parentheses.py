class Solution:
    def isValid(self, s: str) -> bool:
        bucket = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                bucket.append(s[i])
                continue
            if not len(bucket) > 0:
                return False
            if s[i] == ")":
                if bucket[-1] != "(":
                    return False
            if s[i] == "]":
                if bucket[-1] != "[":
                    return False
            if s[i] == "}":
                if bucket[-1] != "{":
                    return False
            bucket = bucket[:-1]
        if len(bucket) == 0:
            return True
        return False


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a brackets string: ")
            print(f"ans = {solution.isValid(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
