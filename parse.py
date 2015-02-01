import sys

def percentage(part, whole):
  return 100 * float(part) / float(whole)

line_counts = 0;
uniques = set()

unique_windows = 0
unique_osx = 0
unique_linux = 0

total_200s = 0

with open(sys.argv[1]) as f:
  for line in f:
    line_counts += 1

# 123.456.789.10 - - [06/Feb/2014:09:48:25 -0600] "GET /downloads/mmc-stable-win32.zip HTTP/1.1" 206 2783484 "http://multimc.org/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"

    sections = line.split()
    ip = sections[0]
    if ip not in uniques:
      if "GET /downloads/mmc-stable-win32.zip" in line:
        unique_windows += 1
      elif "GET /downloads/mmc-stable-lin" in line:
        unique_linux += 1
      elif "GET /downloads/mmc-stable-osx64.tar.gz" in line:
        unique_osx += 1

    uniques.add(sections[0])

    if '" 200' in line:
      total_200s += 1

uniques_count = len(uniques)
print 'Line count: {0}'.format(line_counts)
print 'Unique IPs: {0}'.format(uniques_count)
print 'Unique Windows, OS X, Linux: {0} {1} {2}'.format(unique_windows, unique_osx, unique_linux)
print 'Unique %: {0} {1} {2}'.format(percentage(unique_windows, uniques_count), percentage(unique_osx, uniques_count), percentage(unique_linux, uniques_count))
print 'Total 200 lines (excludes partial downloads): {0}'.format(total_200s)
