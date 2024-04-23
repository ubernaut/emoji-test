## Can emoji speed up a python script?

A friend of mine made an outrageous claim that emoji at the END of a python script seems to speed it up.  

I didn't believe this so I set up a simple test.


	`
  import random
  import time
  # List of emoji characters
  emojis = ['😀', '😂', '😍', '😎', '😇', '😜', '😉', '🥳', '😊', '🤣', '😋', '😘', '🤩', '🤔', '🤪', '😬', '😌', '😏', '🤓', '😝', '😴', '🤗', '😆', '😁', '🤭', '😄', '🤫', '😑', '😶', '😛', '🥴', '🤤', '😋', '😔', '🥺', '😟', '😒', '🙁', '☹️', '😣', '😢', '😭', '😤', '😠', '😡', '🤬', '😖', '😓', '😩', '😰', '😨', '😱', '😵', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '😇', '🥴', '🥵', '🥶', '🥳', '🥺', '🥸', '🤥', '🤭', '🤫']

  def print_rand_emojis():
      random_emojis = ''.join(random.choices(emojis, k=69))
      print(random_emojis)

  def Fibonacci(n):
      if n<0:
          print("sub zero input")
      elif n == 0:
          return 0
      elif n == 1 or n == 2:
          return 1
      else:
          return Fibonacci(n-1) + Fibonacci(n-2)

  emoji_times=[]
  def race_fib():
      start = time.time()
      print(Fibonacci(35))
      print_rand_emojis()
      end = time.time()
      this_run=end-start
      emoji_times.append(this_run)

  def run_all(times=100):
      print("")
      print("NEW RUN")
      for i in range(0,times):
          race_fib()
      print("########################")
      print("RESULTS")
      print("########################")
      print("emoji: ")
      print(sum(emoji_times))
      print("########################")

  run_all()

  `
