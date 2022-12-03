import timeit
global begin
global end

def start():
    global begin
    global end
    # Begin TimeIt to calculate runtime
    begin = timeit.default_timer()
    return

def end():
    global begin
    global end
    stop = timeit.default_timer()
    runtime = stop - begin
    runtime = round(runtime,2)
    print('Runtime: ',runtime,' seconds')
    return