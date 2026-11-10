def hanoi_solver(n):
    rod_a = list(range(n, 0, -1))
    rod_b = []
    rod_c = []

    moves = []

    def record_move():
        moves.append(f"{rod_a} {rod_b} {rod_c}")

    def move_disks(num, source, auxiliary, target):
        if num == 1:
            target.append(source.pop())
            record_move()
            return

        move_disks(num - 1, source, target, auxiliary)

        target.append(source.pop())
        record_move()

        move_disks(num - 1, auxiliary, source, target)

    record_move()

    move_disks(n, rod_a, rod_b, rod_c)

    return "\n".join(moves)


# Test cases
print(hanoi_solver(2))
print()
print(hanoi_solver(3))
