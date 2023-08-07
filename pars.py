from icrawler.builtin import GoogleImageCrawler

def googl_img():
    filters = dict(
        type='photo',
        size='=1920x1080'

    )
    
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(
        keyword='wallpaper',
        max_num=5,
        filters=filters,
        overwrite=True
    )


def main():
    googl_img()

if __name__ == '__main__':
    main()