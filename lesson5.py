import re

my_text = "Vasya , 1995, vasya@gmail.com,"\
          "Aman , 1995, aman@gmail.com,"\
          "Eldar , 1995, eldar@gmail.com,"\
          "Magira , 1995, magira@gmail.com,"\
          "Volodya , 1995, volodya@gmail.com,"\
          "Nina , 1995, nina@gmail.com,"\
          "Masha, 1998,masha@gmail.com"

searching = r"Nina"
results = re.match(searching, my_text)

print(results)

searching = r'@\w+.\w+'
results = re.findall(searching, my_text)

print(results)