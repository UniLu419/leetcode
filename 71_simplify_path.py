from typing import List
from timing_dec import timing


class Solution:
    @timing
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        ans = []
        for folder in path_list:
            match folder:
                case "":
                    continue
                case "..":
                    if ans:
                        ans.pop()
                case ".":
                    continue
                case _:
                    ans.append(folder)
        return "/" + "/".join(ans)


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    path = "/home/"
                case 2:
                    # sample 2
                    path = "/home//foo/"
                case 3:
                    # sample 3
                    path = "/home/user/Documents/../Pictures"
                case 4:
                    # sample 4
                    path = "/../"
                case 5:
                    # sample 5
                    path = "/.../a/../b/c/../d/./"
                case _:
                    break
            print(f"ans = {solution.simplifyPath(path)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
