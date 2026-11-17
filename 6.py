def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1

    count = 0

    count += tower_of_hanoi(
        n-1, source, destination, auxiliary
    )

    print(f"Move disk {n} from {source} to {destination}")

    count += 1

    count += tower_of_hanoi(
        n-1, auxiliary, source, destination
    )

    return count

n = int(input("Enter number of disks: "))

moves = tower_of_hanoi(n, 'A', 'B', 'C')

print("Total moves:", moves)