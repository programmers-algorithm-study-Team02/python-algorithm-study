dolls = []

def solution(board, moves):
    answer = 0
    
    for move in moves:
        doll = get_doll(board, move)
        if put_doll(doll):
            answer += 2
            
    return answer

def get_doll(board, move):
    for row in board:
        doll = row[move - 1]
        if doll != 0:
            row[move - 1] = 0
            return doll
    return 0
    
def put_doll(doll):
    if doll == 0:
        return False
    
    if len(dolls) > 0 and dolls[-1] == doll:
        dolls.pop()
        return True
    else:
        dolls.append(doll)
    
    return False
        
