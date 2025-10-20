from collections import deque

def solution(cards1, cards2, goal):
    carddecks = [
        deque([card for card in cards1]),
        deque([card for card in cards2])
    ]
        
    for g in goal:
        result = False
        for carddeck in carddecks:
            if len(carddeck) > 0 and carddeck[0] == g:
                carddeck.popleft()
                result = True
        if result == False:
            return "No"
        
    return "Yes"
