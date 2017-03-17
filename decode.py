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

   loss = []
   new_file = open("decode.ppm","w")

   for val in the_file:
      okay = val.split(" ")
      for value in okay:
         loss.append(value.rstrip())

   loss = groups_of_3(loss)

   new_file.write("{:s}\n".format(loss[0][0]))
   new_file.write("{:s} {:s}\n".format(loss[0][1],loss[0][2]))


   for pix in loss[1:len(loss)]:
      red = int(pix[0])*10
      if red > 255:
         red = 255
      blue = red
      green = red
      new_file.write("{:d} {:d} {:d}\n".format(red,green,blue))




def groups_of_3(values):
   inside_list = []
   new_list = []
   count = 0
   for val in range(len(values)):
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
