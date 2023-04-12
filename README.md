# TransLiter

<div align=right>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Felibooklover%2FTransLiter&count_bg=%235F3DC8&title_bg=%23555555&icon=python.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

TransLiter transliterates multilingual text into English. | by Hoyeol Kim

Currently, TransLiter supports Korean and Japanese. More languages will be added to TransLiter.

---

## Install

```
$ pip install TransLiter
```

## Load TransLiter in Python

```
$ Python

> import TransLiter as tl
```

## 1. Korean

### 1-1. Simpe functions.

```
> tl.ko("안녕하세요. 날씨가 좋네요!")
annyeohaseyo. narssiga johneyo!
```

If you want to use the transliteration function in a row:

```
> tl.transliter_ko()

> Please enter Korean text: 안녕하세요. 날씨가 좋네요!
annyeohaseyo. narssiga johneyo!

> Please enter Korean text: 우리나라 만세!
urinara manse!
```

To exit TransLiter, please press enter without any text.

### 1-2. File Export (txt -> txt)

The output is saved as `output_ko.txt` in your current directory.

```
> tl.txt_ko("test_ko.txt")
안녕하세요.
annyeohaseyo.
오늘 날씨 좋네요!
oneur narssi johneyo!
행복한 하루 되세요.
haeboghan haru doeseyo.
저는 독서가 취미입니다.
jeoneun dogseoga chwimiibnida.
하루하루 재미있게 살아요.
haruharu jaemiissge sarayo.
가족들과 저녁을 먹어요.gajogdeurgwa jeonyeogeur meogeoyo.
```

### 1-3. File Export (txt -> csv)

The output is saved as `output_ko.csv` in your current directory.

```
> tl.csv_ko("test_ko.txt")
    Original Text                 Transliterated Text
0          안녕하세요.                       annyeohaseyo.
1      오늘 날씨 좋네요!               oneur narssi johneyo!
2     행복한 하루 되세요.             haeboghan haru doeseyo.
3   저는 독서가 취미입니다.      jeoneun dogseoga chwimiibnida.
4  하루하루 재미있게 살아요.         haruharu jaemiissge sarayo.
5   가족들과 저녁을 먹어요.  gajogdeurgwa jeonyeogeur meogeoyo.
```

## 2. Japanese

### 2-1. Simple functions

```
> tl.jp("天気がいいですね。")
tenkigaiidesune。
```

If you want to use the transliteration function in a row:

```
> tl.transliter_jp()

> Please enter Japanese text: おねがいします。
onegaishimasu。

> Please enter Japanese text: 天気がいいですね。
tenkigaiidesune。

> Please enter Japanese text: 毎日運動をします。
mainichiundouwoshimasu。
```

To exit TransLiter, please press enter without any text.

### 2-2. File Export (txt -> txt)

The output is saved as `output_jp.txt` in your current directory.

```
> tl.txt_jp("test_jp.txt")
気を付けて。
kiwotsukete。
良いニュースです。
yoinyuーsudesu。
おやすみなさい。
oyasuminasai。
おねがいします。
onegaishimasu。
気をつけてください。
kiwotsuketekudasai。
それはいい考えですね。sorehaiikangaedesune。
```

### 2-3. File Export (txt -> csv)

The output is saved as `output_jp.csv` in your current directory.

```
>>> tl.csv_jp("test_jp.txt")
  Original Text    Transliterated Text
0        気を付けて。           kiwotsukete。
1     良いニュースです。         yoinyuーsudesu。
2      おやすみなさい。          oyasuminasai。
3      おねがいします。         onegaishimasu。
4    気をつけてください。    kiwotsuketekudasai。
5   それはいい考えですね。  sorehaiikangaedesune。
```

## 3. Spacing

Some langauges such as Japanese don't have spacing betweeon words. If there was spacing between characters or words for those language text, you would bump into errors. To avoid the errors, spacing needs to be removed.

```
> spacing("良 い ニ ュ ー ス で す。")
良いニュースです。
```

If you want to remove all spacing from a file, use `spacing_file("filename")`. The result is saved as `spacing_removed.txt`.

```
> spacing_file("test.txt")
```
