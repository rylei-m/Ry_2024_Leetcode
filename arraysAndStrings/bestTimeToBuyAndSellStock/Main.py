from arraysAndStrings.bestTimeToBuyAndSellStock.Solution import Solution, prices


class Main:
    solution = Solution()
    result = solution.max_profit(prices)
    print(result)


if __name__ == "__main__":
    Main()
