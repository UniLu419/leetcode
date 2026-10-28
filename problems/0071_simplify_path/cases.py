METHOD = "simplifyPath"

CASES = [
    dict(args=("/home/",), expected="/home"),
    dict(args=("/home//foo/",), expected="/home/foo"),
    dict(args=("/home/user/Documents/../Pictures",), expected="/home/user/Pictures"),
    dict(args=("/../",), expected="/"),
    dict(args=("/.../a/../b/c/../d/./",), expected="/.../b/d"),
    dict(args=("/",), expected="/"),
    dict(args=("/a/./b/../../c/",), expected="/c"),
    dict(args=("/..hidden/.",), expected="/..hidden"),
]
