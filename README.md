# Music163Matching
比较两个人的云音乐听过的歌曲排行，支持最近一周和所有时间，需要用户没有关闭听歌排行显示

## How to start
使用到的工具是[Selenium](https://selenium.dev/documentation/en/)一个web自动化测试工具，提供IDE以及插件多种方式。python下安装

    pip install selenium

[chromedriver.exe](https://chromedriver.chromium.org/) 下载对应Chrome版本的driver.exe，仓库带了一份Chrome version 78的driver.exe

    python main.py
```python
SONGS_WEEK = 0
SONGS_ALL = 1
if __name__ == '__main__':
    user1 = get_song_rank_list("https://music.163.com/#/user/songs/rank?id=322324034", SONGS_ALL)     
    user2 = get_song_rank_list("https://music.163.com/#/user/songs/rank?id=39661960", SONGS_ALL)       
    compare_song(user1, user2)
```

## Console
<div align=center><img src="https://github.com/EStormLynn/Music163Matching/blob/master/pic/Rank.png" width="938" height="521" alt="pic"/></div>

<div align=center><img src="https://github.com/EStormLynn/Music163Matching/blob/master/pic/IMG20191126_212518.png" width="536" height="863" alt="pic"/></div>