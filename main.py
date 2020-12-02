# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
def set_require():
    print("How many numbers lottery needs?")
    num_need = int(input("Answer: "))

    print("How many numbers you want to chose?")
    num_want = int(input("Answer: "))

    if num_need > num_want:
        print("you should give more than the lottery needs")
        return set_require()
    return num_need, num_want

def number_get(num_want):
    nums = []
    for i in range(num_want):
        num = int(input("the %d number you want: " % (i + 1)))
        nums.append(num)
        print(nums[i], " added")
    print("\nall your numbers are added...")

    nums.sort()
    return nums

def print_combinations(num_need, nums):
    from itertools import combinations
    comb = list(combinations(nums, num_need))
    print("\nthe combinations of the numbers are listed below:")
    for item in comb:
        print(item)
    pass

if __name__ == '__main__':

    input("This is a program for winning lottery")
    execute = 1
    while execute:
        num_need, num_want = set_require()
        nums = number_get(num_want)
        print_combinations(num_need, nums)

        ex = input("do it again(Y/N)")
        if ex != "Y":
            print("祝您中獎")
            execute = 0






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
