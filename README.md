# TransLiter

<div align=right>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Felibooklover%2FTransLiter&count_bg=%235F3DC8&title_bg=%23555555&icon=python.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

TransLiter transliterates multilingual text to English. | by Hoyeol Kim

Currently, TransLiter supports Korean and Japanese. More languages will be added to TransLiter.

---

### Setup

```
$ git clone https://github.com/elibooklover/TransLiter.git

$ pip install -r requirements.txt
```

### 1. Korean

```
> from transliter_ko import *

> ko("안녕하세요. 날씨가 좋네요!")
annyeohaseyo. narssiga johneyo!
```

If you want to use the transliteration in a row:

```
> from transliter_ko import *
> transliter_ko()

> Please enter Korean text: 안녕하세요. 날씨가 좋네요!
annyeohaseyo. narssiga johneyo!

> Please enter Korean text: 우리나라 만세!
urinara manse!
```

To exit TransLiter, please press ctrl+c.

### 2. Japanese

```
> from transliter_jp import *

> jp("天気がいいですね。")
tenkigaiidesune。
```

If you want to use the transliteration in a row:

```
> from transliter_jp import *
> transliter_jp()

> Please enter Japanese text: おねがいします。
onegaishimasu。

> Please enter Japanese text: 天気がいいですね。
tenkigaiidesune。

> Please enter Japanese text: 毎日運動をします。
mainichiundouwoshimasu。
```

To exit TransLiter, please press ctrl+c.

---
