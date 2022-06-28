


# =============================================================================
# Threading .....concurrent operation
# =============================================================================
#dir(threading)
['Barrier', 'BoundedSemaphore', 'BrokenBarrierError',
 'Condition', 'Event', 'ExceptHookArgs',
 'Lock', 'RLock', 'Semaphore', 'TIMEOUT_MAX',
 'Thread', 'ThreadError', 'Timer', 'WeakSet',
 '_CRLock', '_DummyThread', '_HAVE_THREAD_NATIVE_ID',
 '_MainThread', '_PyRLock', '_RLock', '_SHUTTING_DOWN',
 '__all__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__', '_active', '_active_limbo_lock', '_after_fork', '_allocate_lock',
 '_count', '_counter', '_dangling', '_deque',
 '_enumerate', '_islice', '_limbo', '_main_thread', '_maintain_shutdown_locks',
 '_make_invoke_excepthook', '_newname', '_os', '_profile_hook',
 '_register_atexit', '_set_sentinel',
 '_shutdown', '_shutdown_locks',
 '_shutdown_locks_lock', '_start_new_thread',
 '_sys', '_threading_atexits', '_time',
 '_trace_hook', 'activeCount',
 'active_count', 'currentThread', 'current_thread',
 'enumerate', 'excepthook',
 'functools', 'get_ident',
 'get_native_id', 'local',
 'main_thread', 'setprofile',
 'settrace', 'stack_size']

import threading

# global variable x
x = 0

def increment():
	"""
	function to increment global variable x
	"""
	global x
	x += 1

def thread_task():
	"""
	task for thread
	calls increment function 100000 times.
	"""
	for _ in range(100000):
		increment()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating threads
	t1 = threading.Thread(target=thread_task)
	t2 = threading.Thread(target=thread_task)

	# start threads
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))
