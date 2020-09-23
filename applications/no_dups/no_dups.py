def no_dups(s):
    # Your code here
    word_count = {}
    result = ''
    words = s.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word in word_count:
        if word_count[word] >= 0:
            result += f'{word} '
    result = result.rstrip()
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))