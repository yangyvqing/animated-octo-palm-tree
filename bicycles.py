bicycles=['trek','cannondale','redline','specialized']
message = f"My frist bisycle was a {bicycles[0].title()}"
print(message)
name=['liyit','sunjw','yangxiy','langl']
hello=f"i want your {name[0].title()}"
print(hello)

name.append('munan')
print(name)
name.insert(0,'sunsun')
print(name)
del name[0]
name=['liyit','sunjw','yangxiy','langl']
print(name)
popped_name=name.pop()
print(name)
print(popped_name)
name=['liyit','sunjw','yangxiy','langl']
name.insert(1,'munan')
print(name)
too_far='munan'
name .remove(too_far)
print(name)
print(f"\n{too_far.title()} is too far to me.")