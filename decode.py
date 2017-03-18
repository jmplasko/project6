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

   new_file = open("decode.ppm","w")
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


if __name__ == '__main__':
   main()
