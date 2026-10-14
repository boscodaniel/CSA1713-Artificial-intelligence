from collections import deque

# State is represented as (M_left, C_left, M_right, C_right, boat_side)
# boat_side = 'left' or 'right'

def is_valid_state(m_left, c_left, m_right, c_right):
    # Check missionaries are not outnumbered on either side
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def get_successors(state):
    m_left, c_left, m_right, c_right, boat = state
    successors = []
    
    if boat == 'left':
        # Possible moves from left to right
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        for m, c in moves:
            new_state = (m_left - m, c_left - c,
                         m_right + m, c_right + c,
                         'right')
            if is_valid_state(*new_state[:-1]):
                successors.append(new_state)
    else:
        # Possible moves from right to left
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        for m, c in moves:
            new_state = (m_left + m, c_left + c,
                         m_right - m, c_right - c,
                         'left')
            if is_valid_state(*new_state[:-1]):
                successors.append(new_state)
    return successors

def bfs():
    start = (3,3,0,0,'left')
    goal = (0,0,3,3,'right')
    
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal:
            return path
        
        for successor in get_successors(state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor]))
    return None

# Run the BFS
solution = bfs()

if solution:
    print("Solution found!")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
