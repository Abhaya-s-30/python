def reverse(input_str):
    words=input_str.split('.')
    reversed_words=words[::-1]
    reversed_str='.'.join(reversed_words)
    return reversed_str
input_str="i.like.this.program.very.much"
result=reverse(input_str)
print(result)