import instaloader
import sys
if __name__ == '__main__':
    name = input("enter username here:")
    mod = instaloader.Instaloader()
    mod.download_profile(name, profile_pic_only=True)
    sys.exit()