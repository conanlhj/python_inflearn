# -*- coding: utf-8 -*-


def is_positive_number(integer_str_value):
    # '''
    # Input:
    #   - integer_str_value : 숫자형태의 문자열 값
    # Output:
    #   - integer_str_value가 양수일 경우에는 True,
    #     integer로 변환이 안되거나, 0, 음수일 경우에는 false
    # Examples:
    #   >>> import factorial_calculator as fc
    #   >>> fc.is_positive_number("100")
    #   True
    #   >>> fc.is_positive_number("0")
    #   False
    #   >>> fc.is_positive_number("-10")
    #   False
    #   >>> fc.is_positive_number("abc")
    #   False
    # '''
    try:
        # ===Modify codes below=============
        # 시작전 반드시 'pass'를 지울 것
        return True if int(integer_str_value) > 0 else False
        # ==================================
    except ValueError:
        return False


def get_factorial_value(integer_value):
    # '''
    # Input:
    #   -  integer_value : 자연수 값
    # Output:
    #   -  integer_value의 Factorial 값
    # Examples:
    #    >>> import factorial_calculator as fc
    #    >>> fc.get_factorial_value(5)
    #    120
    #    >>> fc.get_factorial_value(7)
    #    5040
    # '''
    # ===Modify codes below=============
    temp = 1
    for i in range(1, int(integer_value)+1):
        temp = temp*i
    result = temp

    # ==================================
    return result


def main():
    user_input = 0
    # ===Modify codes below=============
    while 1:
        user_input = input('Input a positive number : ')
        if is_positive_number(user_input) is True:
            print(get_factorial_value(user_input))
        elif user_input == '0':
            break
        else:
            print('Input again, Please')
    print('Thank you for using this program')
    # ==================================


if __name__ == "__main__":
    main()