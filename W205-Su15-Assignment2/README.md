# W205-Su15-Assignment2
Michael Kennedy's Assignment 2 Submission
Due 06/26/2015


OVERVIEW
Data collection will resume exactly where it left off if it crashes or cannot recover a connection
Some output files do not contain exactly 1000 tweets since I was still writing the resuming code during data collection
Stream will attempt to auto-restart when disconnected
Groups of 1000 json responses are dumped to sequential files in the output directory
Data analysis extracts 'real' words from each tweet, plots the 30 most common words straight to a file, and writes a full list of word frequencies to csv
By default, it creates 3 sets of files by searching for tweets containing #nbafinals2015, #warriors, and tweets that contain both


USAGE
collect_data.py pad_n output_dir hashtag1 [hashtag2 [hashtag3...]]
	collects live tweets from the twitter Streaming API
	pad_n (int)
		determines number of padding digits for the output files
		adjust according to expected maximum number of tweets
	output_dir (str)
		path to the output directory
		program will create a gigantic file of tokenized text for debugging purposes
		all json will go inside the 'json' folder in the format 'json0000001'
		each json file contains a maximum of 1000 tweets
	hashtags (str)
		hashtags to filter by during data collection
		separate by spaces and do not include the hashtag symbol

analyze_data.py
	run from the output directory of collect_data.py
	will automatically create histograms of the top 30 used words for the tweets in the json directory and a csv listing of the frequency of all of the words
	only counts words that are valid according to the nltk corpus
	output filenames are the concatenated hashtags provided as a list of tuples set by the groups variable
		ex. groups = (nbafinals,swag) will count words for tweets containing both #nbafinals and #swag, and output results as nbafinals+swag.csv/png

FILES
./README.MD
./analyze_data.py
./collect_data.py
./nbafinals2015.csv
./nbafinals2015.png
./warriors.csv
./warriors.png
./warriors+nbafinals2015.csv
./warriors+nbafinals2015.png
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/text
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000001
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000002
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000003
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000004
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000005
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000006
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000007
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000008
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000009
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000010
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000011
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000012
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000013
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000014
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000015
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000016
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000017
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000018
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000019
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000020
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000021
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000022
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000023
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000024
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000025
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000026
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000027
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000028
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000029
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000030
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000031
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000032
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000033
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000034
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000035
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000036
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000037
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000038
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000039
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000040
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000041
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000042
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000043
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000044
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000045
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000046
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000047
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000048
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000049
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000050
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000051
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000052
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000053
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000054
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000055
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000056
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000057
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000058
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000059
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000060
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000061
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000062
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000063
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000064
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000065
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000066
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000067
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000068
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000069
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000070
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000071
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000072
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000073
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000074
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000075
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000076
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000077
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000078
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000079
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000080
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000081
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000082
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000083
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000084
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000085
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000086
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000087
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000088
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000089
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000090
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000091
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000092
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000093
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000094
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000095
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000096
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000097
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000098
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000099
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000100
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000101
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000102
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000103
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000104
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000105
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000106
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000107
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000108
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000109
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000110
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000111
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000112
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000113
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000114
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000115
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000116
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000117
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000118
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000119
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000120
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000121
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000122
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000123
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000124
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000125
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000126
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000127
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000128
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000129
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000130
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000131
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000132
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000133
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000134
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000135
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000136
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000137
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000138
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000139
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000140
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000141
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000142
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000143
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000144
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000145
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000146
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000147
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000148
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000149
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000150
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000151
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000152
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000153
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000154
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000155
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000156
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000157
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000158
http://w205-mak-assignment2-output.s3-us-west-1.amazonaws.com/json/json0000159