import string

def word_count(s):
    # Your code here

    # if the string contains NO ignored characters return an empty dictionary
    # split string into words on whitespace
    # all words should be lowercase
    # IGNORE THESE CHARACTERS ->   " : ; , . - + = / \ | [ ] { } ( ) * ^ &

    result = {}
    ignored = '":;,.-+=/\|[]}{()*^&'

    lower_s = s.lower()

    for char in ignored:
        if char in lower_s:
            lower_s = lower_s.replace(char, '')
    
    if len(lower_s) > 0:
        words = lower_s.split()

        for item in words:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1
    
    return result
        

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))