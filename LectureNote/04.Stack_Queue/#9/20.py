from My_Structure import Stack

_input = input()
paren_stack = Stack()
push_list = '([{<'
pop_list = {')':0,']':1,'}':2,'>':3}
answer = None
for i in _input:
    if i in push_list:
        paren_stack.push(i)
    else:
        if paren_stack.pop() == push_list[pop_list[i]]:
            answer =True
            continue
        else:
            answer = False
            break
print(answer)

