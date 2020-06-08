# Crawling-cloud-music-review

     爬取网易云音乐评论的工程代码,由于网易云歌曲量太多，所以要找齐所有的歌曲就很有难度，
     我们发现所有的歌曲都有一个编号id ；例如：4646545454564，而对应的网址 也 包含有id,
     例如：https://music.163.com/#/song?id=17413778， 以其实我们只要能够将每首歌对应 的id找到就行，
     而每首歌对应着歌手，所以我们只要找全了歌手，就能找全所有歌曲，也能找全所有歌曲的评论，
     在这里我们只需要爬取热门评论就行，作为学习实践使用，如果喜欢的话记得标个星星star哦

需要的环境与包：
ubutun系统
Python
requests
BeautifulSoup
等等，如果运行时报错某个模块没有的话，使用pip install 就OK啦

本项目分为三阶段：

（1）爬取网易云所有歌手保存到csv文档中        Python  爬取网易云所有歌手.py

（2）根据已有的歌曲名单爬取对应的歌曲id,保存到TXT文件中     python 取歌曲ID和名字.py

（3）根据文件id爬取评论保存TXT文档中                   python 爬取热门评论.py

结果展示：
我太胆小

乱世如麻不敢称军阀

太平盛世不敢说爱你

年少别遇见太惊艳的人

误终生

人生很长 缘分很短 错过的不可逆转

欲望很近 梦想很远 有取舍方能实现

越长大 越怀念 回不去 的从前

遗憾着自己 被现实 一点一点改变

谁家的姑娘长得这么漂亮，唉呀妈呀，唉呀妈呀，千万别卸妆！

谁家的姑娘长得这么漂亮，满汉家的满汉家的真漂亮

谁家的姑娘长得这么漂亮，公屏上的公屏上的最漂亮

这首歌请和《还不是因为你长的不好看》一起食用[大笑]

被茶茶圈粉，来听这首歌的

听茶师唱完觉得好听特地来搜搜[呲牙]

[大哭]果然评论君们来路分明：一路满汉家妹子，一路b站全职视频过来的

有从茶师那里来的吗[大哭]

_(:з」∠)_满汉全席唱哪首歌火哪首厉害了 反正不是你家的姑娘

被茶茶圈粉～茶家的姑娘最漂亮

坑军出征，寸草不生

我一直以为这首歌是我爸爸编的[撇嘴]

 喜欢是放肆，爱是克制。
 
相遇是矜持，相处是忍耐。

在感情中，

我可以走一万步去见你，

也愿意退一万零一步离开你。

其实

没有什么永远

反正跟谁过得开心 ，就跟谁在一起

不用太认真，所有人都是过客

谁都不是谁的一切 ，除了父母[爱心]




后续的学习中我会加入将爬取的数据插入mysql保存的部分和对网易云热评进行情感分析，希望能够一直走在前行的路上
