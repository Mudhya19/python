def number_of_hooks(length,max_hook_dist):
    n = 1
    while length/n > max_hook_dist:
        n = n*2
    return n + 1