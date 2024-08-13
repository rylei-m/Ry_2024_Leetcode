from arraysAndStrings.isSubsequence.Solution import Solution, s_list, t


class Main:
    solution = Solution()
    for s in s_list:
        result = solution.isSubsequence(s, t)
        print(result)


if __name__ == '__main__':
    Main()
