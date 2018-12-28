'''
Ryan Prashad
10/15/18
The lifeguard optimal angle problem
'''
import lifeguard

def get_optimal(case, values):
    '''
    this function returns the optimal angle of a lifeguard running
    '''
    chkangles = []
    lookmax = []
                 
    if values[2] > 2:
        mystp = (values[1] - values[0]) / float((values[2] - 1))
        
        for x in range(values[2]):
            chkangles.append((values[0] + (x * mystp)))
            
    if chkangles.count(values[0]) == 0: 
        chkangles.insert(0, values[0])
    if chkangles.count(values[1]) == 0:
        chkangles.append(values[1])
        
    for angle in chkangles:
        lookmax.append(lifeguard.get_response_time((case[0], case[1], case[2],\
                                  case[3], case[4], angle)))
    
    a = lookmax.index(min(lookmax))
    
    optimal_time = min(lookmax)
    optimal_theta_1 = chkangles[a]
    time_error = lifeguard.get_response_time(case) - \
                lifeguard.get_response_time((case[0], case[1], case[2], \
                                  case[3], case[4], chkangles[a]))
    return (optimal_time, optimal_theta_1, time_error)

def get_stats(cases, angles):
    '''
    this function gets stats from get_optimal
    '''
    times = []
    buffer = []
    rescued = 0  
    drowned_could_save = 0
    drowned_could_not_save = 0

    for case in cases:
        times.append(get_optimal(case, angles)[0])
        
    for x in range(0, len(cases)):
        if lifeguard.get_response_time(cases[x]) <= 120:
            rescued += 1
        buffer.append(lifeguard.get_response_time(cases[x]))
        
    for x in range(0,len(times)):
        if times[x] > 120 and buffer[x] > 120:
            drowned_could_not_save += 1

    drowned_could_save = len(cases) - (rescued + drowned_could_not_save)
                
    return (rescued, drowned_could_save, drowned_could_not_save)