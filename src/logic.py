import math

################ Find the closest matching element's index ################
def FindIndex(list, target, miss_ratio, logger):
    logger.DEBUG(f"FindIndex: target: \"{target}\" conformation: {miss_ratio}%")
    first = 0
    lenght = len(list)
    last = lenght - 1

    # Handle empty list - return empty response
    if (lenght == 0):
        return {"index": [], "exact_match": False, "target_value": target, "value": []}, False

    logger.DEBUG(f"Estimated complexity: log(n) + 1  = {math.ceil(math.log(lenght) + 1)} number_of_elements: {lenght}")


    miss_plus = 1 + miss_ratio / 100
    miss_minus = 1 - miss_ratio / 100

    #Checking for exact match
    while first <= last:
        midpoint = (first + last)//2
        current_value = int(list[midpoint])

        if current_value == target:
            logger.DEBUG(f"Found exact match. value: {target}, index: {midpoint}")
            return {"index": midpoint, "exact_match": True, "target_value": target, "value": current_value}, True
        
        elif current_value < target:
            first = midpoint+1
        else:
            last = midpoint-1
    
    #searching left side of the acceptable match
    logger.DEBUG(f"Looking for left side match for target value - {miss_ratio}%: {target} new target: {target*miss_minus}, index range: {0} - {midpoint}")
    left_idx = lenght
    
    fst, lst = FindClosesMatch(list, 0, midpoint, target*miss_minus)
    left_idx = lst + 1  #use the next element in the list to the closest match


    #searching right side of the acceptable match
    logger.DEBUG(f"Looking for righ side match for target value - {miss_ratio}%: {target} new target: {target*miss_plus}, index range: {midpoint} - {lenght - 1}")
    right_idx = -1

    fst, last = FindClosesMatch(list, midpoint, lenght - 1, target*miss_plus)
    right_idx = fst -1  #use the previous element from the closest match     
    
    
    logger.DEBUG(f"left_idx: {left_idx}\nright_idx: {right_idx}")
    
    indexes = [*range(left_idx, right_idx + 1, 1)]
    res = []
    for i in indexes:
        res.append(int(list[i]))
    
    logger.DEBUG(f"\"indexes\": {indexes}\n\"exact_match\": {False}\n\"target_value\": {target}\n\"value\": {res}")
    return {"index": indexes, "exact_match": False, "target_value": target, "value": res}, False


################ binary search function for sub range ################
def FindClosesMatch(list, first, last, target):
    while first <= last:
        mid = (first + last)//2
        current_value = int(list[mid])
    
        if current_value < target:
            first = mid + 1
        else:
            last = mid - 1
    return first, last


################  Beta Logic for adding linear search in case of the distance is less the log(n) ################
def FindIndex_beta(list, target, miss_ratio, logger):
    logger.DEBUG(f"FindIndex: target: \"{target}\" conformation: {miss_ratio}%")
    first = 0
    lenght = len(list)
    last = lenght - 1

    if (lenght == 0):
        return {"index": [], "exact_match": False, "target_value": target, "value": []}, False

    lg = math.ceil(math.log(lenght) + 1)

    logger.DEBUG(f"Estimated complexity: log(n) + 1  = {lg} number_of_elements: {lenght}")


    miss_plus = 1 + miss_ratio / 100
    miss_minus = 1 - miss_ratio / 100

    #Checking for exact match
    while first <= last:
        midpoint = (first + last)//2
        current_value = int(list[midpoint])

        if current_value == target:
            logger.DEBUG(f"Found exact match. value: {target}, index: {midpoint}")
            return {"index": midpoint, "exact_match": True, "target_value": target, "value": current_value}, True
        
        elif current_value < target:
            first = midpoint+1
        else:
            last = midpoint-1
    
    #searching left side of the acceptable match
    left_idx = lenght

    if (midpoint >= lg):            # binary search in case we are further away from the begining of the list then long(n) +1
        fst = 0
        lst = midpoint
        logger.DEBUG(f"Looking for left side match for target value - {miss_ratio}%: {target} new target: {target*miss_minus}, index range: {fst} - {lst}")
        
        while fst <= lst:
            mid = (fst + lst)//2
            current_value = int(list[mid])
        
            if current_value < target*miss_minus:
                fst = mid+1
            else:
                lst = mid-1
        #left_idx = mid + 1
        left_idx = lst + 1
    else:                           # linear search in case we are closer to the begining of the list then long(n) +1
        index = midpoint
        limit = target*miss_minus
        while index >= 0 and int(list[index]) >=limit:
            left_idx = index
            index -= 1

    #searching right side of the acceptable match
    right_idx = -1

    if (lenght-midpoint >= lg):     # binary search in case we are further away from the end of the list then long(n) +1
        fst = midpoint
        lst = lenght - 1
        logger.DEBUG(f"Looking for righ side match for target value - {miss_ratio}%: {target} new target: {target*miss_plus}, index range: {fst} - {lst}")
        while fst <= lst:
            mid = (fst + lst)//2
            current_value = int(list[mid])
        
            if current_value < target*miss_plus:
                fst = mid+1
            else:
                lst = mid-1
        right_idx = fst -1       
        #right_idx = mid -1
    else:                           # linear search in case we are closer to the end of the list then long(n) +1     
        index = midpoint
        limit = target*miss_plus
        while index < lenght and int(list[index]) <=limit:
            right_idx = index
            index += 1

    
    print(f"left_idx: {left_idx}\nright_idx: {right_idx}")
    indexes = [*range(left_idx, right_idx + 1, 1)]
    res = []
    for i in indexes:
        res.append(int(list[i]))
    
    return {"index": indexes, "exact_match": False, "target_value": target, "value": res}, False