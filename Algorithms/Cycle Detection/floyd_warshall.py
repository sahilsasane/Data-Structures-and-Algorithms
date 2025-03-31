class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list_with_cycle(nums, pos):
    nodes = [ListNode(num) for num in nums]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0] if nodes else None


def detect_cycle(ll):
    f = l = ll
    while l and l.next:
        f = f.next
        l = l.next.next
        if f == l:
            return True, f

    return False, None


nums = [1, 2, 3, 4, 5]
pos = 1

head = create_linked_list_with_cycle(nums, pos)

cycle_exists, meeting_point = detect_cycle(head)

if cycle_exists:
    print(f"Cycle detected at node with value: {meeting_point.val}")
else:
    print("No cycle detected")
