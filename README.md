# MED-Paper-Figure-6

A bunch of poorly-written ad-hoc python scripts to generate the alluvial diagram appears in my [ISME Publication](http://www.nature.com/ismej/journal/vaop/ncurrent/full/ismej2014195a.html):

<img src="http://www.nature.com/ismej/journal/vaop/ncurrent/images/ismej2014195f6.jpg" width="600" />

The scripts here explain only the generation of the alluvial diagram. To get a similar result for your dataset, first you need to analyze the same FASTA file with multiple different damarcation methods (such as assigning taxonomy to reads, OTU clustering, MED analysis, etc). Then you need to open each script and edit paths for input files (I wasn't kidding or being modest when I said "poorly-written"). When you run them in the correct order, you should get an output from the last one similar to this:

    taxa,otu,med,size
    Streptococcus,3349,000005591,557045
    Streptococcus,3349,000004955,554047
    Veillonella,3481,000003105,356556
    Streptococcus,962,000005530,239505
    Neisseria,1844,000003465,198265
    Fusobacterium,3540,000003684,166689
    Porphyromonas,3716,000005301,157760
    Prevotella,2433,000001012,145605
    Streptococcus,497,000005526,1035
    Streptococcus,962,000005526,126854
    Gemella,1975,000004822,111216
    Actinomyces,1003,000002612,104190
    Granulicatella,3226,000002347,100576
    Corynebacterium,2654,000005031,94972
    Pasteurella,612,000003262,81356
    Pasteurella,612,000003227,73804
    Fusobacterium,501,000003637,7728
    Fusobacterium,3540,000003637,60484
    Streptococcus,3223,000005538,1599
    Streptococcus,1846,000005538,6589
    Streptococcus,2604,000005538,1667
    Streptococcus,3349,000005538,57257
    Leptotrichia,487,000004781,58892
    Neisseria,4182,000003433,7029
    Neisseria,1844,000003433,50301
    Pasteurella,612,000005182,55451
    Actinobacillus,796,000003361,6565
    Actinobacillus,612,000003361,45592
    Fusobacterium,2889,000003638,4264
    Fusobacterium,3540,000003638,44902
    Actinomyces,1354,000002895,42699
    Prevotella,3964,000004447,42279
    Rothia,2389,000002864,40165
    Prevotella,2433,000004419,38738
    Capnocytophaga,2928,000002397,38377
    Campylobacter,998,000000313,38028
    Pasteurella,612,000005177,37281
    Actinobacillus,796,000003360,3727
    Actinobacillus,612,000003360,31324
    Pasteurella,612,000003263,34367
    Pasteurella,612,000003225,32745
    Collimonas,4148,000003532,32196
    Syntrophococcus,4229,000000346,30981
    Corynebacterium,2124,000002608,30579
    Prevotella,2433,000005422,28308
    Oribacterium,80,000004614,28272
    Selenomonas,3974,000005135,26897
    Bacteroides,2546,000004009,26729
    Veillonella,1215,000005139,4555
    Veillonella,3481,000005139,21818
    Actinobacillus,612,000003356,25568
    Porphyromonas,3716,000003840,25476
    Actinobacillus,796,000003366,2149
    Actinobacillus,612,000003366,23294
    Fusobacterium,2889,000003647,2904
    Fusobacterium,3540,000003647,22164
    Prevotella,2273,000004268,24634
    Leptotrichia,1750,000004735,24620
    Capnocytophaga,621,000004855,24385
    Rothia,2389,000002865,24216
    Prevotella,2427,000004476,21082
    Neisseria,4182,000003434,2293
    Neisseria,1844,000003434,17746
    Bacteroides,2546,000004010,18205
    Fusobacterium,2889,000003636,2033
    Fusobacterium,3540,000003636,15856
    Veillonella,1522,000005168,2545
    Veillonella,3481,000005168,14486
    Atopobium,3539,000002926,17575
    Johnsonella,2617,000003717,17151
    Fusobacterium,3540,000003665,16168
    Neisseria,1844,000003564,14615
    Neisseria,3085,000003564,1058
    Prevotella,2433,000001013,15706
    Bacteroides,2546,000003829,13187
    Bacteroides,2417,000003829,1824
    Actinobacillus,796,000003365,2461
    Actinobacillus,612,000003365,12265
    Porphyromonas,3716,000003842,14764
    Capnocytophaga,673,000001531,1823
    Capnocytophaga,621,000001531,12945
    Streptococcus,3349,000005557,2059
    Streptococcus,1846,000005557,1241
    Streptococcus,962,000005557,10194
    Bacteroides,2546,000003837,14283
    Parvimonas,3401,000000923,13871
    Actinomyces,4445,000005035,13661
    Parasegetibacter,441,000003963,13441
    Bacteroides,2546,000003984,11262
    Bacteroides,2417,000003984,1373
    Leptotrichia,487,000002031,13082
    Prevotella,2433,000004417,12803
    Moryella,3131,000001488,12573
    Actinobacillus,612,000005225,11598
    Selenomonas,3974,000003177,12135
    Prevotella,2469,000000443,12064
    Selenomonas,3974,000003178,11391
    Prevotella,3964,000005428,11158
    Johnsonella,2617,000003710,11113
    Actinomyces,4445,000005034,11056
    Prevotella,2433,000004416,10664
    Leptotrichia,4429,000005474,10657
    Porphyromonas,3716,000003841,10092
    Catonella,795,000005492,10357
    Bacteroides,2417,000003830,1100
    Bacteroides,2546,000003830,8977
    Neisseria,1844,000003470,10033
    Moryella,3131,000001486,9796
    Porphyromonas,3716,000005300,9687
    Prevotella,16,000001696,9518
    Fusobacterium,3540,000003651,8975
    Pasteurella,612,000003230,9280
    Rothia,2389,000002866,9251
    Streptococcus,962,000005556,8669
    Actinobacillus,612,000005215,7793
    Actinobacillus,612,000005221,6534
    Actinobacillus,796,000005221,2016
    Collimonas,4148,000003533,8422
    Campylobacter,4367,000000314,8223
    Leptotrichia,487,000004720,6619
    Leptotrichia,1689,000004720,1123
    Leptotrichia,3402,000004689,8170
    Prevotella,2655,000004362,8109
    Actinobaculum,4113,000002616,8046
    Tannerella,1159,000003976,7910

Then you can go to http://raw.densitydesign.org, paste this output into the input box on the web site, select 'alluvial diagram', set you width and height (to something like 900 x 2000), and finally set "sorty by" option to "automatic".

Which should give you something like this:

<img src="http://i.imgur.com/vOjMEaK.png" />

I apologize for the sloppy code. Regenerating figures in a publication should be much more straightforward. This was a last minute figure, and my eager to get it done empowered my desire to do the right thing. I am hoping to come back to this at some point to give the code a facelift. Meanwhile please don't hesitate to send me your questions: meren at mbl edu.
