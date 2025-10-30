import math
import heapq

def main():
    V = int(input("Enter number of destinations: "))
    S = 0  

    destinations = [(0, 0), (3, 4), (6, 8), (1, 1), (8, 6), (10, 10)]

    adj = []
    for i in range(V):
        adj.append([])

    for i in range(V):
        for j in range(V):
            if i != j:
                x1, y1 = destinations[i]
                x2, y2 = destinations[j]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                adj[i].append((j, distance))

    pq = []
    dis = [math.inf] * V
    dis[S] = 0
    heapq.heappush(pq, (0, S))

    while pq:
        distance, node = heapq.heappop(pq)
        for adjNode, edgeWeight in adj[node]:
            if distance + edgeWeight < dis[adjNode]:
                dis[adjNode] = distance + edgeWeight
                heapq.heappush(pq, (dis[adjNode], adjNode))


    dest_with_dist = []
    for i in range(V):
        pair = (dis[i], destinations[i])
        dest_with_dist.append(pair)


    dest_with_dist.sort()

    optimized_destinations = []
    for pair in dest_with_dist:
        dest = pair[1]
        optimized_destinations.append(dest)

    destinations_for_rover = []
    destinations_for_rover.append(optimized_destinations[0])  

    rest = optimized_destinations[1:]   
    rest.reverse()                       

    destinations_for_rover.extend(rest)  


    print("\nShortest distances from start:")
    for i in range(V):
        print(f"To {destinations[i]}: {dis[i]:.2f}")

    print("\nOptimized destination order (for rover.pop):")
    print(destinations_for_rover)

    path_taken = []
    while destinations_for_rover:
        next_dest = destinations_for_rover.pop()   
        path_taken.append(next_dest)
        print(f"Rover moving to: {next_dest}")

    print(f"\nFinal path taken: {path_taken}")


main()

