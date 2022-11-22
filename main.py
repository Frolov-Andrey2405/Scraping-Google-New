# import module
from gnewsclient import gnewsclient

# declare a NewsClient object
client = gnewsclient.NewsClient(language='ukrainian',  # print("Location: \n", client.locations, '\n')
                                # print("Language \n", client.languages, '\n')
                                location='Ukraine',
                                # print("Topic \n", client.topics, '\n')
                                topic='World',
                                max_results=10)  # Your number of requests

news_list = client.get_news()

for item in list(news_list):
    print("\nTitle : ", item['title'])
    print("Link : ", item['link'], '\n')
