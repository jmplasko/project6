import sys

def main():
   try:
      the_file = open(sys.argv[1],"r")
   except IndexError:
      print("Usage: python3 decode.py <image>")
      sys.exit(1)
   except:
      print("Unable to open {:s}".format(sys.argv[1]))
      sys.exit(1) 

#   loss = []
   new_file = open("decode.ppm","w")

#   for val in the_file:
#      okay = val.split(" ")
#      for value in okay:
#         loss.append(value.rstrip())

#   new_file.write("{:s}\n".format(loss[0]))
#   new_file.write("{:s} {:s}\n".format(loss[1],loss[2]))
#   new_file.write("{:s}\n".format(loss[3]))

#   loss = groups_of_3(loss)

   counter = 0
   pixel = []

   for line in the_file:
      if counter < 3:
         new_file.write("{:s}".format(line))
      else:
         val = line.split(" ")
         for num in val:
            pixel.append(num)
            if len(pixel) == 3:
               red = int(pixel[0])*10
               if red > 255:
                  red = 255
               blue = red
               green = red
               new_file.write("{:d} {:d} {:d}\n".format(red,green,blue))
               pixel = []
      counter += 1

#   for pix in loss:
#      if counter != 0:
#         red = int(pix[0])*10
#         if red > 255:
#            red = 255
#         blue = red
#         green = red
#         new_file.write("{:d} {:d} {:d}\n".format(red,green,blue))
#      counter += 1

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
