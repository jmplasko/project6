import timeit
import random
import sys
import threading
import array_list
import linked_list

# the increase in stack size has only an effect on the next thread 
# being run (see below)
threading.stack_size(64*1024*1024) # E.g. 64 MB stack
sys.setrecursionlimit(2 ** 20)     # something real big

 
# print out the timing results
def print_timing(desc, iterations, seconds):
   print('{}\t{:>5} iterations in {:7.3f} seconds'.format(desc, iterations, seconds))
 
 
# build a list for this test ... the type of list is passed as module
# We use the most efficient way for array_list and linked_list, respectively
def build_list(n, module, max=10000):
   list = module.empty_list()
   for pos in range(n):
      if module.__name__ == 'array_list':
         # append to the end for array list
         list = module.add(list, pos, random.randrange(max))
      else:
         # append to the front for linked list
         list = module.add(list, 0, random.randrange(max))      
 
   return list
 
 
# the function passed to foreach must take an argument, but we
# don't really want to do anything with it for this experiment
def noop(value):
   pass
 
 
# timeit expects that the function passed will take no arguments, so
# this function gathers the arguments and returns a new function that
# uses them, but that itself does not take any arguments
def build_operation(list, module, n):

   # Add your own function here and return them below as appropriate
   
   def run_build_list():
      list = module.empty_list()
      for pos in range(n):
         list = module.add(list, 0, random.randrange(10000))

   def run_get():
      for i in range(module.length(list)):
         noop(module.get(list,i))

   def run_foreach():
      module.foreach(list, noop)
   
   # Return here the name of the function you want to run
   return run_get
 
 
def run_one_experiment(num_elements, num_iterations, module):
   list = build_list(num_elements, module)
   to_run = build_operation(list, module, num_elements)
   seconds = timeit.timeit(to_run, number=num_iterations)
 
   # Change the text here to reflect the name of the function 
   # you selected for running in build_operation()
   print_timing('{:>12}.get(): {:>7} elements'.format(
      module.__name__, num_elements), num_iterations, seconds)
 
def main():
   # select the numbers for the problem size n you want to test
   for n in [10, 100, 1000, 10000, 50000]:
      # run one experiment with n and n_iter = number of iterations 
      n_iter = 100   # i.e. how often to run the function
      # and the type of list: array_list or linked_list
      run_one_experiment(n, n_iter, array_list)

'''
 Remember: n is "the problem size", here the number of elements in a list, 
 and the 100 above is just the number of iterations i.e. how often the 
 actual test is being run. If you run a test 1000 times instead of 100 times, 
 it just takes 10 times longer. The point here is, that some of these tests, 
 especially when using small n's, are really fast within microseconds, 
 so you run it more often to get a better measurement. 
 Don't change the number of iterations in single one experiment, otherwise 
 you have to correct for it. In fact the problem size n and number 
 of iterations should give a running time between fractions of seconds and 
 maybe several seconds (minutes?). While the number of iterations apparently 
 always scales linear with the running time, the problem size n does not. 
 And that is what you have to figure out.
'''
      
# ------- Don't change anything here ----------      
# only new threads get the redefined stack size
thread = threading.Thread(target=main)
thread.start()
