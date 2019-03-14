# wecraw


1 功能

爬取微信朋友圈。

严格来说，不应该叫“爬取”，因为ie它不是一般意义上的爬虫。

它只是利用python脚本，通过ADB操作手机，从而对微信模拟执行某些操作。

对屏幕元素的识别，采用的是从手机拉取截屏，将截屏与事先获取的另一些截屏进行对比，从而确定屏幕元素的位置。

由于我不懂计算机图形学，所以图像对比采用了笨笨的遍历数组的方法，手动羞赧～～～，相信一定有更好的办法实现它。

由于图像对比笨笨嗒，所以需要大量的事前工作，获取截屏，给予正确的命名，以帮助程序确定屏幕元素。

在/refer文件夹可以看到那些需要事先准备的截屏。


2 使用方法：

准备两个空的屏幕，左边那个设为主屏，放微信，右边那个放WPS。

按照/refer的内容获取截屏，并进行命名，用它们替换调/refer下的内容。

用ADB连接手机，启动wecraw.py，然后该干嘛干嘛去，它工作非常慢，也许需要好几天。

但是中间要经常看看它，也许它会出什么错，比如进入死循环。


3 限制

只能爬取自己的朋友圈，不能爬取微信好友的朋友圈。对代码稍作改动可以实现，但我不知道那有什么意义，所以没做。

只能爬取文字，不能爬取照片，而且照片可能会引起一些错误。

没办法，谁叫我的朋友圈全是文字呢，你要是有爬取照片的需求，那就自己动手改代码吧。


4 为什么做

我在微信朋友圈写了很多文字，有上百万字，我想把它们收集起来，但是微信没有提供相应的接口，于是只好自己动手了。

这段代码工作效率真的很低，足足用了4天才把我的微信朋友圈爬完，也许有什么办法能让它快一些。


