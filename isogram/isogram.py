def is_isogram(string):
    new_string = string.lower().replace(' ', '').replace('-', '')
    if len(new_string) == len(set(new_string)):
        return True
    else:
        return False

# 要求返回True或false时，return判断语句即可
# return len(new_string) == len(set(new_string))