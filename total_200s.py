import sys

total_200s = 0

with open(sys.argv[1]) as f:
  for line in f:

# 123.456.789.10 - - [06/Feb/2014:09:48:25 -0600] "GET /downloads/mmc-stable-win32.zip HTTP/1.1" 206 2783484 "http://multimc.org/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"

    if '" 200 ' in line:
      total_200s += 1

print '{"count": ' + str(total_200s) + ', "startups": "?"}'
