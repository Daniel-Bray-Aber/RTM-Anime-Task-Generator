#!/usr/bin/python

from dateutil.parser import parse
from dateutil.parser import ParserError
from datetime import timedelta
import sys
import getopt

anime_name = None
start_date = None
start_episode = None
end_episode = None
days_interval = None
priority = None
tags = []
date = None
help_menu = False

try :
    opts, args = getopt.getopt(sys.argv[1:], "n:d:s:e:i:p:t:h")
except getopt.GetoptError:
    print ("-n <anime name> -d <start date>") 

for opt, arg in opts :
    if opt == "-n" :
        anime_name = arg    
    elif opt == "-d" :
        start_date = arg
    elif opt == "-s" :
        start_episode = arg
    elif opt == "-e" :
        end_episode = arg
    elif opt == "-i" :
        days_interval = arg
    elif opt == "-p" :
        priority = arg
    elif opt == "-t" :
        tags.append(arg)
    elif opt == "-h" :
        help_menu = True

if help_menu :
    print("Usage: animeTastGenerator.py -n <Anime Name> -d <Start Date> -s <Start Episode> -e <End Episode> -i <Days Between Episodes> -p <Priority Level> -t <Tag> -t <Tag> -t <Tag> ...")
    exit()

if anime_name == None :
    print("Please make sure you specify the -n <Anime Name> Argument");
    exit()

try :
    date = parse(start_date, dayfirst=True, yearfirst=False)
except ParserError :
    print("Please make sure the -d <Start Date> argument is an acceptable format eg: DD/MM/YYYY");
    exit()
except TypeError :
    print("Please make sure you specify the -d <Start Date> Argument (Format: DD/MM/YYYY)")
    exit()
    
try :
    start_episode = int(start_episode)
except ValueError:
    print("Please make sure -s <Start Episode> argument is an integer")
    exit()
except TypeError:
    print("Please make sure you specify the -s <Start Episode> argument")
    exit()
        
try :
    days_interval = int(days_interval)
except ValueError:
    print("Please make sure -i <Days Interval> argument is an integer")
    exit()
except TypeError:
    print("Please make sure you specify the -i <Days Interval> argument")
    exit()


try :
    priority = int(priority)
    if priority < 1 or priority > 3 :
        print("Please make sure -p <Priority> is 1, 2, or 3")
        exit()
except ValueError:
    print("Please make sure -p <Priority> argument is an integer")
    exit()
except TypeError:
    print("Please make sure you specify the -p <Priority> argument")
    exit()

try :
    end_episode = int(end_episode)
except ValueError:
    print("Please make sure -e <End Episode> argument is an integer")
    exit()
except TypeError:
    print("Please make sure you specify the -e <End Episode> argument")
    exit()

if end_episode < start_episode :
    print("Please make sure -s <Start Episode> is less or equal to -e <End Episode>")
    exit()

for x in range(start_episode, end_episode + 1) :
    task = "Watched " + anime_name + " (" + str(x) + ")" 
    task += " ^" + date.strftime("%d %b %y")
    for tag in tags :
        task += " #" + tag
    task += " !" + str(priority)
    task += " =25 minutes"
    print(task)
    date += timedelta(days=days_interval)

#b = b + timedelta(days=daysBetweenViewing)




