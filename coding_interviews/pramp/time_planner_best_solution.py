def meeting_planner(slotsA, slotsB, dur):
# edge cases: slot empty per either one of the two 
    if not slotsA or not slotsB:
        return []

    # all durs in one person's slot is less than the required dur
    
    i, j = 0,0
    while i < len(slotsA)and j < len(slotsB):
        
        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])
        
        if end-start >= dur:
          return [start, start + dur]
      
        if slotsA[i][1] < slotsB[j][1]:
            i += 1
        else:
            j += 1
    
    