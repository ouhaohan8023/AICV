from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

text = '从今年1月1号立了个flag，要发一个关于我做的这个小程序的介绍视频，硬是拖到今天哈。再不发就要开学了，赶紧补上。steamdb是国外查询游戏价格的网站，需要注意的是，他并不是steam官方的，是一个独立开发者开发的，属于一个外挂一样的存在。它的网站地址是 steamdb.info ，里面的价格内容非常全，低价区和史低的价格都有。唯一的缺点是不支持中文，还有访问慢。于是，出于对大神的膜拜，我手撸了一个steamdb低价区查询的小程序。在手机上就可以查看，上下班的路上可以刷一刷打发打发时间。小程序每天定时爬取steam所有游戏，30+区的价格，对于大部分的热门游戏，我都给汉化了。在这我给大家演示一下。比如输入只狼，可以搜到哈，然后进入后可以看到30+区的价格。我们最关注的其实还是阿根廷和浪漫的土耳其。可以看到阿根廷的价格是xxx，相当于国区价格的2折，点击价格也可以看到最近一次更新时间。这个价格一般是一天更新一次。拉到最后，可以看到同一个厂家出的游戏以及DLC，DLC大部分我都没汉化，我一个人实在是搞不过来。想着要不要找个小伙伴一起搞。。。目前这个项目的话算是为爱发电，1月1号开通流量主到现在收入100.。。服务器就得1000块一年好么。。。且用且珍惜吧，有想法的小伙伴也可以联系我～'
model_id = 'damo/speech_sambert-hifigan_tts_zh-cn_16k'
sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model=model_id)
output = sambert_hifigan_tts(input=text, voice='zhizhe_emo')
wav = output[OutputKeys.OUTPUT_WAV]
with open('output.wav', 'wb') as f:
    f.write(wav)