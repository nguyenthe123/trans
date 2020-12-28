import sys
import os
from icrawler.builtin import GoogleImageCrawler
from PIL import Image

def convert_to_lower_case(word):
    """ This function convert WORD to word"""
    return word.lower()

def creat_htmlfile():
    """ This function will creat word.html (if it is not exist) """
    htmlfile = "word.html"
    hfile = open(htmlfile, 'a')
    hfile.close

def counting_words(stt):
    htmlfile = "word.html"
    hfile = open(htmlfile,'r')
    lines = hfile.readlines()
    for line in lines:
        if line[0:5] == '<b>Từ':
            stt = stt + 1
            #print(str(stt))
    hfile.close
    return stt

def creating_html_file(word,stt,inf_image_file):
    """ This function will creating html file from wordfile !!!!"""
    path = os.getcwd()
    if path[-9:] == '/download':
        path = os.getcwd()[:-8]
    #print(path)
    os.chdir(path)
#Open wordfile
    wordfile = "anhviet109K.txt"
    #print(wordfile)
    print(f"Searching word data from file '{wordfile}'... ")
    datafile = open(wordfile,'r')
    lines = datafile.readlines()
    number_of_line = 0
    key_line = 0
    leng_of_word = len(word)
    print(leng_of_word)
    for line in lines:
        #print(line)
        #print(line[0])
        if line[0] == '@':
            str_numofline = str(number_of_line)
            #print(line[0::])
        if line[0:leng_of_word + 3] == ('@' + word + ' /'):
            key_line = number_of_line
            #print(lines[key_line+1][0])
            #write into new file with word and example
            fout = open('word.html','a')
            fout.write('\n' + '<b>Từ số ' + str(stt) + ' '+ line[1:-1:] +' </b>' + '\n')
            fout.write(f"\n <img src={inf_image_file}> \n ")
            fout.close
            for k in range(1,50):
                if lines[key_line + k][0] != '@':
                    fout = open('word.html','a')
                    fout.write('<pre>' + lines[key_line + k][0::] + '</pre>')
                    #print(lines[key_line + k][0::])
                    fout.close
                else:
                    break
            #fout.close
        number_of_line += 1
    if key_line == 0:
        fout = open('word.html','a')
        fout.write('\n' + '<b>Từ số ' + str(stt) +' ' + word + ' '+ 'không tìm ra' + ' </b>' + '\n')
        fout.write(f"\n <img src={inf_image_file}> \n ")
        fout.close
    #print(key_line)
    #print(lines[key_line])
    data = lines[key_line]
    datafile.close
    return data

def download_image_from_google(word):
    """ This function will down load word's image from goolge"""
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'download'})
    google_crawler.crawl(keyword=word, max_num=1)

def convert_png_to_jpg(word, inf_image_file):
    """ This function will convert png file to jpeg file"""
    path = inf_image_file
    if path[-3:] == "png":
        pathimg = path[0:-3] + "jpg"
        namejpg = word + '.jpg'
        img = Image.open(path).convert('RGB')
        img.save(pathimg, 'jpeg')
    else:
        pathimg = path
    return pathimg
def change_name_of_image_file(word):
    """ This function change namefile and get path of it"""
    #path = "/home/kepthe/Desktop/Gitne/trans/download"
    #print ("The path is: ",os.getcwd())
    path = os.getcwd()
    if path[-9:] != '/download':
        path = os.getcwd() + '/download'
    #print(path)
    os.chdir(path)
    #print(os.getcwd())
    namefile_old = os.listdir(path)
    FJoint = os.path.join
    files = [FJoint(path,f) for f in os.listdir(path)]
    namefile_new = word + namefile_old[0][-4:]
    #print(namefile_new)
    str_namefile_old = str(namefile_old[0])
    os.rename(str_namefile_old,namefile_new)
    #print(os.listdir(path))
    #cmd = f'cd {path}'
    #print(cmd)
    #cmd = f"mv {namefile_old} {namefile_new}"
    #failure = os.system(cmd)
    #if failure:
    #    print(f'Change {namefile_old} to {namefile_new} failure!!!')
    #else:
    #    print(f'Change {namefile_old} to {namefile_new} successfully!!!')
    inf_image_file = path + '/' + namefile_new
    #print(inf_image_file)
    return inf_image_file

def main():
    """ This is main program """
    script, word = sys.argv
    word = convert_to_lower_case(word)
    stt = 1
    creat_htmlfile()
    stt = counting_words(stt)
    print("Tim kiem tu so " + str(stt))
    download_image_from_google(word)
    inf_image_file = change_name_of_image_file(word)
    path = convert_png_to_jpg(word, inf_image_file)
    print(path)
    print("\n Tai file image cua tu ve " + path)
    creating_html_file(word,stt,path)
    print("Tao file html")

if __name__ == "__main__":
    main()
