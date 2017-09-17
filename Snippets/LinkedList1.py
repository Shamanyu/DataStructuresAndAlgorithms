class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data) 
        current = self.head
        previous = None
        while current:
            previous = current
            current = current.get_next()
        if previous == None:
            self.head = new_node
        else:
            previous.set_next(new_node)

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            return ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_list(self):
        node = self.head
        while node:
            print(node.get_data())
            node = node.get_next()
    
    def remove_duplicates(self):
        node_dictionary = dict()
        current = self.head
        while current:
            if current.get_data() in node_dictionary:
                self.delete(current.get_data())
            else:
                node_dictionary[current.get_data()] = True        
            current = current.get_next()

    def find_element_from_last(self, n):
        slow = self.head
        fast = self.head
        counter = n
        while fast and counter > 0:
            fast = fast.get_next()
            counter -= 1
        if counter > 0:
            print("The list has fewer than ", n, "elements")
            return -1
        else:
            while fast:
                fast = fast.get_next()
                slow = slow.get_next()
            return slow.get_data()

L = LinkedList()
number_of_elements = int(input("Enter the number of entries:\n"))
for x in range(0, number_of_elements):
    L.insert(int((input("Enter number: "))))

#to_delete = int(input("Which number is to be deleted?\n"))
#while True:
#    try:
#        L.delete(to_delete)
#    except ValueError:
#        break

#L.remove_duplicates()

#print(L.find_element_from_last(7))



L.print_list()
