def solution(tickets):
    tickets.sort()
    
    def fly(src):
        dsts = [ticket[1] for ticket in tickets if ticket[0] == src]
        
        if not dsts:
            if not tickets:
                return True
            return False
        
        for dst in dsts:
            ticket = [src, dst]
            tickets.remove(ticket)
            path.append(dst)
            if fly(dst):
                return True
            tickets.append(ticket)
            path.pop()
            
        return False
    
    path = ["ICN"]
    fly("ICN")
    
    
    return path
    
