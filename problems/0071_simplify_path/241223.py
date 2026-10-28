class Solution:
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
