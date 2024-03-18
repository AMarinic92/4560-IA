import subprocess
import shlex
import sys
from imageCaptioning import imageCap

def main() ->int:
    args = sys.argv[1:]
    print(args)
    #args = ["https://static.wikia.nocookie.net/warhammer40k/images/5/55/AnkhoftheTriarch9thEdition.jpg/revision/latest/scale-to-width-down/1000?cb=20200925173557",
    #                    "https://static.wikia.nocookie.net/warhammer40k/images/3/33/Necron_Warriors_vs_UM.png/revision/latest/scale-to-width-down/1000?cb=20160811061758"]
    json = ""
    captions = imageCap(args).get_caption()
    id_count = 0
    for caption in captions:
        json += '{"id":'+str(id_count)+',"imageUrl":"'+args[id_count]+'","type":"Bad alt text","message":"","suggestion":"'+caption[0].get("generated_text")+'"},'
        id_count += 1
    print(json[:-1])
    return 0

if __name__ == '__main__':
    sys.exit(main())