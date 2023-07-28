# Transliter

<div align=right>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Felibooklover%2FTransLiter&count_bg=%235F3DC8&title_bg=%23555555&icon=python.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

#### Transliter transliterates multilingual text into Latin script | by Hoyeol Kim

Currently, Transliter supports Korean, Japanese, Russian, Ukrainian, Bulgarian, Macedonian, Mongolian, Montenegrin, Serbian, and Tajiki. More languages will be added to Transliter in the future.

There are several functions in Transliter, such as `tl.ko`, `tl.transliter_ko`, `tl.txt_ko`, and `tl.csv_ko`, in addition to spacing functions (`tl.spacing` and `tl.spacing_file`). To transliaterate from a language other than Korean, simply replace the language code `ko` with your desired language code.

Language codes are as follows: `ko` (Korean), `jp` (Japanese), `ru` (Russian), `ua` (Ukrainian), `bg` (Bulgarian), `mk` (Macedonian), `mn` (Mongolian), `me` (Montenegrin),  `sr` (Serbian), and `tj` (Tajiki).

---

## Install

```
$ pip install transliter
```

## Load Transliter in Python

```
$ Python

> import transliter as tl
```

## 1. Korean

### 1-1. Simple functions.

```
> tl.ko("안녕하세요. 날씨가 좋네요!")
'annyeonghaseyo. nalssiga jotneyo!'
```

If you want to use the transliteration function several times in a row:

```
> tl.transliter_ko()

> Please enter Korean text: 안녕하세요. 날씨가 좋네요!
annyeonghaseyo. nalssiga jotneyo!

> Please enter Korean text: 우리나라 만세!
urinara manse!
```

To exit Transliter, please press enter without any text.

### 1-2. File Export (txt -> txt)

The output is saved as `filename_output.txt` in your current directory.

```
> tl.txt_ko("test_ko.txt")
안녕하세요.
annyeonghaseyo.
오늘 날씨 좋네요!
oneul nalssi jotneyo!
행복한 하루 되세요.
haengbokhan haru doeseyo.
저는 독서가 취미입니다.
jeoneun dokseoga chwimiibnida.
하루하루 재미있게 살아요.
haruharu jaemiitge salayo.
가족들과 저녁을 먹어요.gajokdeulgwa jeonyeokeul meokeoyo.
```

### 1-3. File Export (txt -> csv)

The output is saved as `filename_output.csv` in your current directory.

```
> tl.csv_ko("test_ko.txt")
    Original Text                 Transliterated Text
0          안녕하세요.                     annyeonghaseyo.
1      오늘 날씨 좋네요!               oneul nalssi jotneyo!
2     행복한 하루 되세요.           haengbokhan haru doeseyo.
3   저는 독서가 취미입니다.      jeoneun dokseoga chwimiibnida.
4  하루하루 재미있게 살아요.          haruharu jaemiitge salayo.
5   가족들과 저녁을 먹어요.  gajokdeulgwa jeonyeokeul meokeoyo.
```

## 2. Japanese

### 2-1. Simple functions

```
> tl.jp("天気がいいですね。")
tenkigaiidesune。
```

If you want to use the transliteration function several times in a row:

```
> tl.transliter_jp()

> Please enter Japanese text: おねがいします。
onegaishimasu。

> Please enter Japanese text: 天気がいいですね。
tenkigaiidesune。

> Please enter Japanese text: 毎日運動をします。
mainichiundouwoshimasu。
```

To exit Transliter, please press enter without any text.

### 2-2. File Export (txt -> txt)

The output is saved as `filename_output.txt` in your current directory.

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

The output is saved as `filename_output.csv` in your current directory.

```
> tl.csv_jp("test_jp.txt")
  Original Text    Transliterated Text
0        気を付けて。           kiwotsukete。
1     良いニュースです。         yoinyuーsudesu。
2      おやすみなさい。          oyasuminasai。
3      おねがいします。         onegaishimasu。
4    気をつけてください。    kiwotsuketekudasai。
5   それはいい考えですね。  sorehaiikangaedesune。
```

## 3. Spacing

Some languages such as Japanese don't have spacing between words. If there is spacing between the characters or words for text in those languages, you might bump into errors. To avoid the errors, the spacing needs to be removed.

```
> tl.spacing("良 い ニ ュ ー ス で す。")
良いニュースです。
```

If you want to remove all spacing from a file, use `spacing_file("filename")`. The result is saved as `filename_rmspace.txt`.

```
> tl.spacing_file("test.txt")
```

## 4. Cyrillic

Transliter currently supports Russian and Serbian between languages written in Cyrillic. More languages will be added soon.

### 4-1. Simple functions

```
# Russian
> tl.ru("Привет")
'Privet'

# Serbian
> tl.sr("Здраво")
'Zdravo'
```

If you want to use the transliteration function several times in a row:

```
# Russian
> tl.transliter_ru()

> Please enter Russian text: Привет.
Privet.

> Please enter Russian text: Как дела?
Kak dela?

# Serbian
> tl.transliter_sr()

> Please enter Serbian text: Жао ми је
Žao mi je

> Please enter Serbian text: Добро јутро
Dobro jutro
```

To exit Transliter, please press enter without any text.

### 4-2. File Export (txt -> txt)

The output is saved as `filename_output.txt` in your current directory.

```
# Russian
> tl.txt_ru("test_ru.txt")
Доброе утро.
Dobroe utro.
Меня зовут Мандли.
Menya zovut Mandli.
Рад познакомиться с тобой.
Rad poznakomit'sya s toboj.
Как дела?Kak dela?

# Serbian
> tl.txt_sr("test_sr.txt")
Добро јутро
Dobro jutro
Драго ми је
Drago mi je
Пријатан дан желим
Prijatan dan želim
Не разумем
Ne razumem
Извините!Izvinite!
```

### 4-3. File Export (txt -> csv)

The output is saved as `filename_output.csv` in your current directory.

```
# Russian
> tl.csv_ru("test_ru.txt")
                Original Text          Transliterated Text
0                Доброе утро.                 Dobroe utro.
1          Меня зовут Мандли.          Menya zovut Mandli.
2  Рад познакомиться с тобой.  Rad poznakomit'sya s toboj.
3                   Как дела?                    Kak dela?

# Serbian
> tl.csv_sr("test_sr.txt")
        Original Text Transliterated Text
0         Добро јутро         Dobro jutro
1         Драго ми је         Drago mi je
2  Пријатан дан желим  Prijatan dan želim
3          Не разумем          Ne razumem
4           Извините!           Izvinite!
```
