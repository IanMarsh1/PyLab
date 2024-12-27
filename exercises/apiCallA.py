# apiCallA
#* Look at an example api documentation in swagger https://swagger-ui.meteomatics.com/
#* In the search bar, put in the url https://api.weather.gov/openapi.yaml
#* https://www.geeksforgeeks.org/how-to-make-api-calls-using-python/#
#* https://www.w3schools.com/python/python_ref_dictionary.asp

import requests

def get_posts(uri):
    # https://www.w3schools.com/python/python_try_except.asp
    try:
        # go out and ask the server for the info at this uri
        response = requests.get(uri)

        # look at HTTP status codes https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    # find a station id using the /stations in swagger API
    stationID = "0084W"
    
    # each URI is for each api call
    tempURI = f'https://api.weather.gov/stations/{stationID}/observations/latest'
    locURI = f'https://api.weather.gov/stations/{stationID}'
    
    # make the api call
    temp = get_posts(tempURI)
    loc = get_posts(locURI)
    
    # convert data type to sting so it can be printed and get the values from the dictionary I want
    # note: this is not the best way to do this
    temp = str(temp['properties']['temperature']['value'])
    loc = str(loc['properties']['name'])
    
    print("The temperature at " + loc + " is " + temp + "C")
        
if __name__ == '__main__':
    main()