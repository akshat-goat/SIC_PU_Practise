def solve_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    solve_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    solve_hanoi(n - 1, auxiliary, source, destination)

    
print("--- Tower of Hanoi Solver ---")
num_disks = int(input("Enter the number of disks: "))
if num_disks <= 0:
    print("Number of disks must be positive.")
else:
    solve_hanoi(num_disks, 'A', 'B', 'C')