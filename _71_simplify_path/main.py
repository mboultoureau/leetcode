class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []

        for p in path.split("/"):
            if folders and p == "..":
                folders.pop()
            elif p not in [".", "..", ""]:
                folders.append(p)

        return "/" + "/".join(folders)


        # Other solution
        # folders = deque([])
        # i = 0
        # current = ""

        # while i < len(path):
        #     if path[i] == "/":
        #         if current == ".." and folders:
        #             folders.pop()
        #         elif current != "" and current != ".." and current != ".":
        #             folders.append(current)

        #         current = ""
        #     else:
        #         current += path[i]

        #     i += 1

        # if current == ".." and folders:
        #     folders.pop()
        # elif current != "" and current != ".." and current != ".":
        #     folders.append(current)

        # result = ""
        # while folders:
        #     result += "/" + folders.popleft()

        # if result == "":
        #     return "/"

        # return result