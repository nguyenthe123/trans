import trans as trs
import sys

def main():
    """ This is main program """
    script, sentence = sys.argv
    #print(sentence)
    if sentence[len(sentence)-1] == '.':
        sentence = sentence[0:len(sentence)-1]
    print(sentence)
    #k = 1
    #for i in range (0, len(sentence)):
    #    if sentence[i] == ' ':
    #        k = k + 1
    #print(k)
    words = sentence.split()
    for word in words:
        print(word)
        word = trs.convert_to_lower_case(word)
        trs.creat_htmlfile()
        stt = 1
        stt = trs.counting_words(stt)
        print("Tim kiem tu so " + str(stt))
        trs.download_image_from_google(word) 
        inf_image_file = trs.change_name_of_image_file(word)
        path = trs.convert_png_to_jpg(word, inf_image_file)
        print("\n Tai file image cua tu ve " + path)
        trs.creating_html_file(word,stt,path)
        print("Tao file html")

if __name__ == "__main__":
    main()

