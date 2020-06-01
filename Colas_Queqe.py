try:
	import Queue as queue
except ImportError:
	# Python 3
	import queue
fifo_queue = queue.Queue(3)
lifo_queue = queue.LifoQueue(3)
priority_queue = queue.PriorityQueue(3)
fifo_queue.put("Perro")
fifo_queue.put("Gato")
fifo_queue.put("Conejo")
lifo_queue.put("Perro")
lifo_queue.put("Gato")
lifo_queue.put("Conejo")
priority_queue.put((2, "Perro"))
priority_queue.put((3, "Gato"))
priority_queue.put((1, "Conejo"))
print("Cola FIFO")
print(fifo_queue.get())
print(fifo_queue.get())
print(fifo_queue.get())
print("\nCola LIFO")
print(lifo_queue.get())
print(lifo_queue.get())
print(lifo_queue.get())
print("\nCola de prioridad")
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
