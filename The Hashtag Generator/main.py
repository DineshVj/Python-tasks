def generate_hashtag(s):
    final_string = "#"
    ready_string = ''
    li = list(s.split(" "))
    new_list = []
    for element in li:
        x = element.title()
        new_list.append(x)
    for n in new_list:
        ready_string += n
        final_string += n
    if len(ready_string) > 140 or len(ready_string) == 0:
        return False
    else:
        return final_string

