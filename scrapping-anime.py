from bs4 import BeautifulSoup
import requests
import os

# author Muhammad Rifqi <muhammadrifqi.tb@gmail.com>
def writeLink(animeName , link):
    path = os.path.dirname(os.path.abspath(__file__))
    # Filename to append
    filename = path + "\list-anime.txt"
    # The 'a' flag tells Python to keep the file contents
    # and append (add line) at the end of the file.
    myfile = open(filename, 'a')
    # Add the line
    myfile.write( 'Nama : ' + animeName + '\nLink : ' + link + '\n')
    # Close the file
    myfile.close()


website = requests.get('https://www.samehadaku.tv/')

if website.status_code == 200:
    html = BeautifulSoup(website.content , 'html.parser')
    getContents = html.find_all(class_="post-title")
    getContents = getContents[1:2]
    no = 0

    print('Lagi Progress , sabar yahh ......')
    for x in getContents:
        no += 1
        link = x.find('a').get('href')
        animeName = x.find('a').getText()

        openLink = requests.get(link)

        if openLink:
            # open one
            content = BeautifulSoup(openLink.content , 'html.parser')
            contentList = content.find('div' , class_="download-eps")

            if len(contentList.find_all('li')) > 1:
                linkList = contentList.find_all('li')[1].find_all('a')
            else :
                linkList = contentList.find_all('li')[0].find_all('a')

            # open two
            linkDownload = linkList[3].get('href')
            openLink2 = requests.get(linkDownload)
            content2 = BeautifulSoup(openLink2.content , 'html.parser')
            contentList2 = content2.find('div' , class_="download-link")
            # open three
            linkDownload2 = contentList2.find('a').get('href')
            openLink3 = requests.get(linkDownload2)
            content3 = BeautifulSoup(openLink3.content , 'html.parser')
            contentList3 = content3.find('div' , class_="download-link")
            # content download zippyshare
            zippyshare = contentList3.find('a').get('href')
            openZippy = requests.get(zippyshare)
            contentZippy = BeautifulSoup(openZippy.content , 'html.parser')

            if (contentZippy.find('div' , class_="video-share") is None):
                linkDownloadAnime = 'Gagal Grab :<'
                progress = "Gagal :<"
            else :
                linkDownloadAnime = contentZippy.find('div' , class_="video-share").find('input').get('value')
                progress = "Berhasil " + str(no)

            writeLink(animeName , linkDownloadAnime)
            print(progress)

    print('\n PROGRAM SELESAI <author : Muhammad Rifqi>')
else :
    print('something wrong here')
