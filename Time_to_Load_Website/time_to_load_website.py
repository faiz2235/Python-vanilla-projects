'''
    This script takes a url from the user and returns the time taken to load that
    website.
    ## How to use this ?
    1. Just type the following on the command prompt:
    python time_to_load_website.py
    2. It will reuest you to provide a url. Provide the url and hit enter to see the
    script in action.
'''

from urllib.request import urlopen
import time

def get_load_time(url):
    """
    This function takes a user defined url as input
    and returns the time taken to load that url in seconds.
    Args:
        url (string): The user defined url.
    Returns:
        time_to_load (float): The time taken to load the website in seconds.
    """
    if ("https" or "http") in url: # checking for presence of protocols
        open_this_url = urlopen(url) # open the url as entered by the user
    else:
        open_this_url = urlopen("https://" + url) # adding the http to the url
    
    start_time = time.time() # time stamp before the reading of url starts
    open_this_url.read() # reading the user defined url
    end_time = time.time() # time stamp after the reading url
    open_this_url.close() # closing the instace of the urlopen object
    time_to_load =  end_time - start_time

    return time_to_load


if __name__ == "__main__":
    url = input("Enter the url: ")
    print(f"\nThe time taken to load {url} is {get_load_time(url)} seconds.")
