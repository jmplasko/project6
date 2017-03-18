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

   new_file = open("fade.ppm","w")
   counter = 0
   counter_2 = 0
   pixel = []

   for line in the_file:
      if counter < 3:
         new_file.write("{:s}".format(line))
         if counter == 1:
            k = line.split(" ")
            amount = int(k[0])*int(k[1])
            width = k[0]
      else:
         val = line.split(" ")
         for num in val:
            pixel.append(num)
            if len(pixel) == 3:
               row = counter_2//int(width)
               column = counter_2%int(width)
               scale = (r - (math.sqrt(abs(y-row)**2 + abs(x-column)**2))) / r
               if scale < .2:
                  scale = .2
               red = int(pixel[0]) * scale
               green = int(pixel[1]) * scale
               blue = int(pixel[2]) * scale
               new_file.write("{:d} {:d} {:d}\n".format(int(red),int(green),int(blue)))
               pixel = []
               counter_2 += 1
      counter += 1


if __name__ == '__main__':
   main()
