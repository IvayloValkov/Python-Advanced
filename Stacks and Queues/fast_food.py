from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])
success = True

print(max(orders))

while orders:
    current_orders = orders.popleft()
    if food_quantity >= current_orders:
        food_quantity -= current_orders
    else:
        success = False
        orders.appendleft(current_orders)
        break

if success:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")