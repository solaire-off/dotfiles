my_file = open(r"/sys/class/backlight/acpi_video0/brightness",'r')
s=my_file.readline()
s1=''
BOOK=['1','2','3','4','5','6','7','8','9','0']
for i in s :
    if i in BOOK :
      s1=s1+i
my_file.close()
if int(s1)>1 :
    s1=int(s1)-1
    my_file = open(r"/sys/class/backlight/acpi_video0/brightness",'w')
    my_file.write(str(s1))
    my_file.close()
