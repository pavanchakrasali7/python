class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue operation
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty. Nothing to dequeue.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Peek operation to see the front item
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. Nothing to peek.")

    # Get the size of the queue
    def size(self):
        return len(self.queue)

    # Display the queue
    def display(self):
        if not self.is_empty():
            print("Queue:", self.queue)
        else:
            print("Queue is empty.")

# Example usage
queue = Queue()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Display queue
queue.display()

# Peek the front element
print(f"Peek: {queue.peek()}")

# Dequeue elements
queue.dequeue()
queue.dequeue()

# Display queue after dequeue
queue.display()

# Check size of the queue
print(f"Queue size: {queue.size()}")

# Dequeue remaining elements
queue.dequeue()

# Try to dequeue from empty queue
queue.dequeue()
