import math
import queue

def shortest_path(M,start,goal):
    print("Shortest path finder called")
    
    
    paths = queue.PriorityQueue()
    paths.put(start, 0)
    
    scores = {start: 0}
    previous = {start: None}
    
    
    while not paths.empty():
    
        current = paths.get()

        for path in M.roads[current]:
            new_score = scores[current] + heuristic(M.intersections[current], M.intersections[path])

            if path not in scores or new_score < scores[path]:
                
                previous[path] = current

                scores[path] = new_score
                total_score = new_score + heuristic(M.intersections[current], M.intersections[path])
                paths.put(path, total_score)
            
        
        
    shortest_path = [goal]
        
    while shortest_path[0] != start:
        shortest_path.insert(0, previous[shortest_path[0]])
    
    
    return shortest_path



def heuristic(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))