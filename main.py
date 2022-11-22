# import module
from gnewsclient import gnewsclient

# declare a NewsClient object
client = gnewsclient.NewsClient(language='ukrainian', # print("Language \n", client.languages, '\n')
                                location='Ukraine', # print("Location: \n", client.locations, '\n')
                                topic='World', # print("Topic \n", client.topics, '\n')
                                max_results=10)  # Your number of requests

news_list = client.get_news()

for item in list(news_list):
    print("\nTitle : ", item['title'])
    print("Link : ", item['link'], '\n')
