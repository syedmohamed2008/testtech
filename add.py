
# add two numbers
s = 'abcabcbb'
'''lst = []
distchar = ''
maxlength = 0
strlen = len(s)
''''''for i in s:
    if i not in distchar:
        distchar = distchar + i''''''

distchar = s
#print(distchar)
for j in range(strlen,0,-1):
    #print (j)
    for k in range(j):
        if s[k:j] not in lst:
            if(len(set(s[k:j])) == len(s[k:j])):
                lst.append(s[k:j])
print(lst)
print(set(s))
distlen = len(distchar)
print(distchar)
for i in range(distlen+1):
    #print(i)
    if distchar in lst:
        print(distchar)
        maxlength = len(distchar)
        #print(maxlength)
    else:
        distchar= distchar[i:]
        #print(distchar)

print(maxlength)'''


char_set = set()
left = 0
max_len = 0

for right in range(len(s)):
    # Shrink the window from the left if there's a duplicate
    while s[right] in char_set:
        #print(s[right])
        #print(s[left])
        char_set.remove(s[left])
        print(char_set)
        left += 1
        print(f'left:' + str(left))
    char_set.add(s[right])
    print(char_set)
    max_len = max(max_len, right - left + 1)
    print('maxlen' + str(max_len))

print(max_len)

