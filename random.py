def show_excitement():
    # Your code goes here!
    input_string = "I am super excited for this course!"
    to_be_returned = ""
    start = 1
    while start <= 5:
        start = start + 1
        to_be_returned = to_be_returned+input_string+" "
    return to_be_returned


print(show_excitement())

