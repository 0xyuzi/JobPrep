'''
returns the earliest time slot that works for both of them and is of duration dur

1. each person's slots are disjotined (no overalp)
2. sorted by slot's start time

[62,70]
[60, 120]
'''

class solution:
    def meeting_planner(self,slotsA, slotsB, dur):
    # edge cases: slot empty per either one of the two 
        if not slotsA or not slotsB:
            return []
        
        # all durs in one person's slot is less than the required dur
        meet_slotsA = []
        for slot in slotsA:
            if slot[1] - slot[0] < dur:
                continue
            meet_slotsA.append(slot)
            
        meet_slotsB = []    
        for slot in slotsB:
            if slot[1] - slot[0] < dur:
                continue
            meet_slotsB.append(slot)
            
        # print(meet_slotsA, meet_slotsB)

        for slotA in meet_slotsA:
            for slotB in meet_slotsB:
            # check if overlap
                if slotA[0] < slotB[1] and slotB[0] < slotA[1]:
                    # print(slotA, slotB)
                    start_time = max(slotA[0], slotB[0])
                    end_time = min(slotA[1], slotB[1])
                    if end_time - start_time >=dur:
                        print(end_time - start_time, dur)
                        return [start_time, start_time+ dur]
            
        return []

if __name__ == "__main__":
    sol = solution()
     
    slotA = [[7,12]]
    slotB = [[2,11]]
    dur = 5

    print(sol.meeting_planner(slotA, slotB, dur))
    
    