import sys
import math

def main():
   try:
      r = int(sys.argv[4])
      x = int(sys.argv[3])
      y = int(sys.argv[2])
      the_file = open(sys.argv[1],"r")
   except IndexError:
      print("Usage: python3 fade.py <image> <row> <column> <radius>")
      sys.exit(1)
   except:
      print("Unable to open {:s}".format(sys.argv[1]))
      sys.exit(1)

   loss = []
   new_file = open("fade.ppm","w")

   for val in the_file:
      okay = val.split(" ")
      for value in okay:
         loss.append(value.rstrip())

   new_file.write("{:s}\n".format(loss[0]))
   new_file.write("{:s} {:s}\n".format(loss[1],loss[2]))
   new_file.write("{:s}\n".format(loss[3]))

   loss_2 = groups_of_3(loss)

   for okay in range(len(loss_2)):
      row = okay//int(loss[1])
      column = okay%int(loss[1])
      scale = (r - (math.sqrt(abs(y-row)**2 + abs(x-column)**2))) / r
      if scale < .2:
         scale = .2
      print(scale)
      red = int(loss_2[okay][0]) * scale
      green = int(loss_2[okay][1]) * scale
      blue = int(loss_2[okay][2]) * scale
      new_file.write("{:d} {:d} {:d}\n".format(int(red),int(green),int(blue)))

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

if __name__ == '__main__':
   main()
