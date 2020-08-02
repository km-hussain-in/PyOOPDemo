def work(n):
  for i in range(1000000 * n):
       pass

def job_coroutine():
   while True:
     n = yield
     print(f'Accepted job {n}')
     work(n)
     print(f'Finished job {n}')

handler = job_coroutine()
handler.send(None)
handler.send(70)
handler.send(90)
handler.close()

#await callable coroutine
async def greet(person):
  return 'Hello ' + person

#awaitable object
class Countdown:
  
  def __init__(self, limit):
    self.limit = limit
    
  def __await__(self):
    for n in range(self.limit, 0, -1):
      work(10 * n)
      yield n
  
async def start(): 
  #await calls are dispatched by event loop
  print(await greet("Countdown"))
  await Countdown(10)
  
entry = start()
#event loop
try:
  while True:
    print(entry.send(None))
except StopIteration: pass


