# Wordcounter with tagging & json output
To count words frequency in multiple text files, tag them and save them into a json file.

# Requirs
- python 2.x
- TreeTagger (Save TreeTagger installation path in .env, see example)
- TreeTagger language parameter files 

# Commands
The word_counter takes two commands: 
`python word_counter.py language filename`

In order to get the word tags classified in the language of your choice, just add the language code of the language, e.g.:
`python word_counter.py de filename`

Please note: In order to support the language of your desire, you need to install the parameter file of your desired language with TreeTagger.

language default: en
The parameter filename will add some more information to your json file depending on your filename, see below.


# Structure of your source file names with arg "filename"
prefix_lastName_firstName_year_month_day.txt, e.g. de_Schneider_Anton_2018_07_21.txt

Given that, the json file will be structured the following way:
```
[{
  "firstName": "Anton",
  "lastName": "Schneider",
  "month": "07",
  "year": 2018,
  "day": "21"
  "party": "de",
  "words":[{
    "count": 30,
    "tag": "KON",
    "word": "and"
  }, 
  {..}]
},
{..}]
```

# Structure of your source file names without arg
If you just want to output an array of objects for your different files, you do not need to provide an argument.
The resulting json data will look like:

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


# How to use
1. Put your text file(s) into the path `wordcounter/files`, for example, a file named "de_Schneider_Anton_2018_07_21.txt"
2. Execute the following commands
```
cd wordcounter
python word_counter.py language filename
```

or for a simple output: 
`python word_counter.py`

3. The result will be written in the file named `data.json`
