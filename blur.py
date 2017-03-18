import sys
import math

def main():
   try:
      the_file = open(sys.argv[1],"r")
      try:
         reach = int(sys.argv[2])
      except:
         reach = 4
   except IndexError:
      print("Usage: python3 fade.py [<image>]")
      sys.exit(1)
   except:
      print("Unable to open {:s}".format(sys.argv[1]))
      sys.exit(1)

   loss = []
   new_file = open("blur.ppm","w")

   for val in the_file:
      okay = val.split(" ")
      for value in okay:
         loss.append(value.rstrip())

   new_file.write("{:s}\n".format(loss[0]))
   new_file.write("{:s} {:s}\n".format(loss[1],loss[2]))
   new_file.write("{:s}\n".format(loss[3]))

   ll = groups_of_3(loss)
   loss_2 = turn_into_double_list(ll,loss[1])

   for okay in range(len(ll)):
      lol = find_reach_pixel(okay,loss_2,reach,int(loss[1]))
      new_pix = find_average(lol)
      new_file.write("{:d} {:d} {:d}\n".format(int(new_pix[0]),int(new_pix[1]),int(new_pix[2])))

def groups_of_3(values):
   inside_list = []
   new_list = []
   count = 0
   for val in range(4,len(values)):
      inside_list.append(values[val])
      count += 1
      if val == len(values) - 1:
         new_list.append(inside_list)
         return new_list
      elif count == 3:
         new_list.append(inside_list)
         inside_list = []
         count = 0

def turn_into_double_list(values,width):
   inside_list = []
   new_list = []
   count = 0
   w = width
   for val in range(len(values)):
      inside_list.append(values[val])
      count += 1
      w = int(width)
      if count == w:
         new_list.append(inside_list)
         inside_list = []
         count = 0
   return new_list

def find_reach_pixel(pixel,vals,reach,width):
   blur = []
   row = pixel//width
   column = pixel%width
   start_r = row - reach
   start_c = column - reach
   finish_r = row + reach +1
   finish_c = column + reach +1

   if start_r < 0:
      start_r = 0
   if finish_r > len(vals):
      finish_r = len(vals)
   if start_c < 0:
      start_c = 0
   if finish_c > width:
      finish_c = width

   for val in range(start_r,finish_r):
      for value in range(start_c,finish_c):
         blur.append(vals[val][value])
   return blur

def find_average(vals):
   div = len(vals)
   red = 0
   green = 0
   blue = 0
   for value in vals:
      red += int(value[0])
      green += int(value[1])
      blue += int(value[2])

   return [red/div,green/div,blue/div]

if __name__ == '__main__':
   main()
