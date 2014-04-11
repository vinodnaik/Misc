#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import errno
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
 
  hasht={}
  match=re.search(r'\w+_([\w\.]+)',filename)
  if match:
    server=match.group(1)
  else:
    print "Could not extract server name from the file name"
    exit(1)
  
  text=open(filename).read()
  urls=re.findall(r'GET\s(\S+puzzle/)([\w-]+\.jpg)',text)
  for url in urls:
    final_url=server+url[0]+url[1]
    if url[1] not in hasht:
      hasht[url[1]]=final_url
  sorted_keys=sorted(hasht.keys(),key=sortfn)

  url_list=[]
  for url in sorted_keys:
    url_list.append(hasht[url])

  return url_list

def sortfn(val):
  tple=val.split('-')
  if len(tple)>=3:
    return tple[2]
  return tple[1]

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  
  try:
    os.mkdir(dest_dir)
  except Exception as e:
    print e
    if e.errno != errno.EEXIST:
      raise
  idx=0
  fp=open(dest_dir+"/index.html",'w+')
  fp.write("\n".join(["<verbatim>","<html>","<body>"]))
  path=os.path.abspath(dest_dir)
  buffer=""
  
  for url in img_urls:
    print "Downloading the image img"+str(idx)
    try:
      urllib.urlretrieve("http://"+url,dest_dir+'/img'+str(idx))
    except Exception as e:
      print e
      idx+=1
      continue
    buffer+="<img src="+path+'/img'+str(idx)+'>'
    idx+=1
    
  fp.write(buffer+"\n")
  fp.write("\n".join(["</body>","</html>"]))
  fp.close()

  
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
