def return_key(value):
    country_code = {"Korea": 82, "US": 1, "Vietnam": 84, "UK": 44, "Japan": 81}
    key_list = list(country_code.keys())
    value_list = list(country_code.values())
    # print(key_list, value_list)
    idx_of_value = value_list.index(int(value))
    result = key_list[idx_of_value]
    return result


value = return_key(input("국가번호를 입력해주세요. :"))
print(value)
