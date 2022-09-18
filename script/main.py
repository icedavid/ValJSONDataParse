import SkinImage
import SkinTheme
import Tools

_RES_PATH = '../res/'
_RES_LOCAL_DIR_NAME = {
    'skin', 
    'theme', 
    'maps', 
    'player_cards', 
    'player_titles', 
    'bundles'
}     # 需要初始化的路径都放在这里，直接添加名字就好

def main():
    for dir_name in _RES_LOCAL_DIR_NAME:
        Tools.initResDir(_RES_PATH + dir_name)

    # SkinImage.start()
    # SkinTheme.start()


if __name__ == '__main__':
    main()