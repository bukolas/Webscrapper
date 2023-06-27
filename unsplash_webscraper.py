import requests
import os
#url = "https://unsplash.com/napi/search/photos?query=dog&per_page=20&xp=4"

# init a constructor: a constructor is a method that will 
# be automatically called whenever we instantiate an object of a class
class Unsplash: 
    def __init__(self, search_term, per_page =20, quality ="thumb"):
        self.search_term = search_term
        self.per_page = per_page
        self.page = 0
        self.quality = quality
#to avoid been blocked, we have to create a headers in form of dictionary by copying header from the url page
        self.headers = {"Accept-Language": "en-US",
                        "Referer": "unsplash.com",
                        "Accept-Encoding": "gzip",
                        "Sec-Ch-Ua-Mobile": "?0",
                        "Sec-Ch-Ua-Platform": "Windows",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"




        }

#create method that will set the url
    def set_url(self):
        return f"https://unsplash.com/napi/search/photos?query={self.search_term}&per_page={self.per_page}&xp={self.page}"
    
    #create another method that will make a request
    def make_request(self):
        url = self.set_url()
        return requests.request("GET",url, headers = self.headers)
    
    # we need to get the data and add the .json to get the data at the end
    def get_data(self):
        self.data = self.make_request().json()

    #another method that will save the data
    def save_path(self,name):
        download_dir = "unsplash"
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()), download_dir,name)}.jpg"

#it will derefernce all the symbolic links on the operating systems that support them 
# the os path above is giving the absolute path to the working directory. 
# we also join the unsplash and name as argument to this path with another os path


    #create a method that will download the images
    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath,"wb") as f:
            f.write(requests.request("GET",url,headers =self.headers).content)

    # create another method to scrape the images 
    def Scrapper(self, pages):
        for page in range(0, pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['results']:
                name = item['id']
                url = item['urls'][self.quality]
                self.download(url,name)
            self.page += 1

if __name__ == "__main__":
    scrapper = Unsplash("dogs")
    scrapper.Scrapper(1)