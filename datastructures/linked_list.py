class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return new_node

    def insert(self, data, pos=None):
        pass

    def delete(self, data):
        current_node = self.head

        if current_node.data == data:
            self.head = current_node.next
            return

        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
            current_node = current_node.next

    def get_all_data(self):
        data = []

        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.next
        return data

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


if __name__ == "__main__":
    ll = LinkedList()
    ll.append("A")
    ll.append("B")
    ll.append("C")
    ll.print_list()
    print(ll.get_all_data())
    ll.delete('A')
    ll.print_list()
