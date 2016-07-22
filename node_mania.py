# pass in the linked list
# to access the head of the linked list
# linked_list.head
def search_k_from_end(linked_list, k):
    node = linked_list.head
    length = 1
    while node.next:
        node = node.next
        length += 1
    if k > length:
        return None
    node = linked_list.head
    for i in range(length - k):
        node = node.next
    return node.data