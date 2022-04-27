import math
import signal
import time

class GracefulKiller:
  kill_now = False
  signals = {
    signal.SIGINT: 'SIGINT',
    signal.SIGTERM: 'SIGTERM'
  }

  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, signum, frame):
    print("\nReceived {} signal".format(self.signals[signum]))
    print("Cleaning up resources. End of the program")
    self.kill_now = True


def count_primes():
  number=1
  count = 0

  while(count<100000):
    isprime=1
    number+=1
    for j in range(2,int(math.sqrt(number))+1):
      if(number%j==0):
        isprime=0   
        break
    if(isprime==1):
      count+=1    

killer = GracefulKiller()
while(not killer.kill_now):
  start = time.monotonic()
  count_primes()
  print("counted primes in: ", time.monotonic() - start)
