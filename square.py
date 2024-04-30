def main():
    input_str = input("Enter the numbers separated by spaces: ")
    numbers = list(map(int, input_str.split()))


    def sum_of_squares_positive(nums):
        squared_positive_nums = map(lambda num: num ** 2, filter(lambda x: x > 0, nums))
        return sum(squared_positive_nums)

    print(sum_of_squares_positive(numbers))

if __name__ == "__main__":
    main()
