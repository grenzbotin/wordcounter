# Wordcounter with word type tagging & json output
To tag & count words frequency in multiple text files and save the output into a json file.

## Requierements
- python 2.x
- TreeTagger
- TreeTagger language parameter files 

## Installation
- Make sure you have python 2.x on your machine
- Install TreeTagger (http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) & TreeTaggerWrapper for python (http://treetaggerwrapper.readthedocs.io/en/latest/)
- Install necessary language parameter files for TreeTagger
- Create .env file in the poject root & set the path for your TreeTagger installation
- Put your textfiles into  the path `wordcounter/wordcounter/files`

## Run it
### To run the script with english text files & plain output as array of object for every file, run:

```
cd wordcounter
python word_counter.py
```

#### Output (language default: 'en'):
```
[
  [
    {
      "count": 30,
      "tag": "KON",
      "word": "and"
    }, 
    {..}
  ],
  [..]
]
```

### To run the script with another language support, run it with:
Please Note: Make sure you have the language parameter file installed!

```
cd wordcounter
python word_counter.py de
```

#### Output (language default: 'en'):
```
{
  list: [
    {
      text: [
        {
          "count": 30,
          "tag": "KON",
          "word": "und"
        }, 
      {..},
      ]
      {..},
    }
  ],
]
```

### To run the script and add the filenames information into your output tree, run it with:

```
cd wordcounter
python word_counter.py en filename
```

#### Output (language: en, filename data enrichment)

In order to make this work, the filename needs to have the naming convention: prefix_lastName_firstName_year_month_day.txt
So, imagine our file is named Germany_Schneider_Anton_2018_07_21.txt

Given that, the json file will be structured the following way:

```
{
  list: [
    {
      "firstName": "Anton",
      "lastName": "Schneider",
      "month": "07",
      "year": 2018,
      "day": "21"
      "party": "Germany",
      "words":[{
        "count": 30,
        "tag": "KON",
        "word": "and"
      }, 
      {..}]
    }
  ]
}
```


## Result
The result will be written in a file named `wordcounter/wordcounter/data.json`
