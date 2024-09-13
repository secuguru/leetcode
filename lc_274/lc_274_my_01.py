def main(citations):
    c_size = len(citations)
    if c_size == 1 and citations[0] > 0:
        return 1
    
    c_arr = [0] * (c_size+1)
    for num in citations:
        for i in range(1, num+1):
            if i <= c_size:
                c_arr[i] += 1
            else:
                break
                
    h_idx = 0
    for i in range(1, len(c_arr)):
        if i <= c_arr[i] and i > h_idx:
            h_idx = i
    
    return h_idx

if (__name__ == "__main__"):
    tc = [
            [3,0,6,1,5],
            [1,3,1],
            [1,2,100],
            [1,7,9,2],
            [689,761,882,909,60,660,563,858,176,31,516,945,208,673,754,533,941,431,523,610,121,447,263,446,431,292,423,902,517,347,143,55,128,634,944,802,625,468,694,873,222,729,696,23,524,418,703,964,64,452,73,69,522,720,978,969,30,560,607,15,202,587,676,471,843,646,175,898,731,609,773,28,364,243,769,954,909,173,576,704,369,133,732,433,342,521,266,672,300,205,835,571,572,316,933,745,823,206,675,11,522,624,133,911,483,222,778,112,29,21,945,698,751,964,235,518,262,618,337,611,349,167,285,884,371,862,352,400,423,521,398,29,5,123,884,604,963,557,755,487,849,292,705,618,512,895,944,260,34,222,503,469,687,684,414,619,712,316,766,183,986,828,157,750,938,473,80,961,2,298,284,628,391,114,917,760,814,454,933,272,917,104,896,792,881,940,391,845,662,842,350,542,634,831,279,535,766,230,111,67,151,992,63,516,814,617,458,344,388,120,559,177,38,218,640,157,621,139,263,457,254,935,288,284,151,557,264,376,20,380,202,474,415,822,915,794,153,522,609,763,164,701,62,914,771,212,685,475,475,490,322,35,712,773,580,355,226,636,21,228,980,382,886,365,231,320,427,512,939,67,757,867,753,185,927,846,304,303,624,945,805,97,752,98,77,931,58,179,556,694,63,568,115,672,689,459,812,112,730,260,517,635,276,923,977,714,218,775,749,173,316,492,903,939,386,124,514,956,62,533,794,959,267,142,336,24,938,547,897,178,216,290,44,729,334,681,483,772,996,187,537,320,560,527,62,162,650,539,120,440,118,175,807,160,899,482,159,881,505,687,878,697,39,406,981,595,704,808,813,577,64,341,52,156,784,220,599,745,519,718,145,815,8,100,197,542,992,762,182,865,619,808,900,815,715,748,529,929,907,518,769,817,915,135,36,668,948,644,916,664,172,13,759,652,85,50,919,630,329,336,876,339,147,375,965,337,276,184,310,740,798,319,283,312,875,92,394,44,2,810,425,70,376,279,914,185,178,761,281,695,561,592,795,335,488,932,168,856,82,515,620,965,561,48,882,118,509,279,698,988,176,899,753,156,425,750,945,930,302,329,115,242,488,479,342,159,391,657,393,873,294,57,892,968,411,465,847,581,74,4,193,658,282,678,291,728,182,432,834,983,0,135,133,801,181,179,663,296,996,569,283,24,31,998,585,747,573,881,386,949,392,959,87,815,880,940,401,801,458,5,399,548,263,786,836,683,291,832,122,422,819,881,134,285,38,969,339,108,394,340,347,977,296,841,514,680,311,897,639,898,679,930,993,274,458,267,427,490,718,91,418,346,274,791,903,65,830,703,735,179,979,988,855,731,986,445,603,941,402,620,935,265,434,603,106,208,41,120,425,749,826,53,326,639,451,334,499,593,616,876,740,28,354,995,129,33,681,486,24,36,798,269,590,220,961,709,542,778,884,454,65,765,643,184,485,48,31,574,770,451,273,188,954,925,14,534,931,12,753,491,164,788,382,129,833,956,170,336,456,500,333,247,182,271,232,722,259,635,885,875,66,220,839,770,528,645,885,27,555,4,886,722,602,268,188,426,558,308,496,999,872,841,700,786,195,552,627,219,530,106,531,606,637,901,227,369,470,107,43,702,432,960,145,663,417,799,110,368,337,714,473,315,467,60,754,573,901,792,809,902,858,759,347,898,289,566,117,897,742,871,228,239,903,443,417,932,387,694,639,777,285,109,760,27,702,612,759,78,234,630,905,384,519,195,947,995,849,586,193,802,144,350,378,743,130,101,997,97,325,829,819,866,586,42,558,502,988,70,668,644,72,961,255,927,923,51,451,495,685,668,704,309,965,354,460,818,807,169,677,7,362,28,447,787,488,386,2,263,543,687,945,359,525,319,850,761,706,501,436,622,488,44,450,607,25,403,995,463,960,513,599,994,93,732,539,609,324,176,220,563,259,88,736,584,275,554,432,123,72,952,853,340,34,649,766,446,323,3,361,960,521,347,168,913,495,523,386,10,233,487,854,596,941,480,363,856,307,110,201,688,392,768,905,269,815,250,600,721,794,860,314,114,91,908,113,801,398,545,564,650,909,378,212,536,399,343,32,948,346,24,208,484,565,860,216,216,877,784,572,429,485,726,632,516,353,342,593,970,231,805,283,750,550,290,649,595,300,247,636,504,637,743,666,667,905,783,341,529,374,459,861,756,973,170,954,732,140,381,199,238,929,869,979,631,305,212,19,544,297,945,852,791,497,648,963,923,625,47,825,456,468,595,641,249,959,693,787,739,256,268,39,637,233,342,799,824,175,503,650,265,584,952,454,964,802,381,673,466,690,785,165,814,627,99,172,172,885,538,56,722,828,371,878,351,635,901,900,790,156,393,812,971,995,639,189,887,654,111,669,847,562,860,348,95,683,776,853,618,565,658,68,674,265,150,177,574,914,417,992,759,440,866,314,432,214,976,587,94,884,937,139,314,766,537,243,704,463,311,471,866,598,124,332,400,151,351,719,585,150,728,811,599,143,270,695,598,485,281,631,602,468,374,172,103,227,228,354,323,803,928,496,69,896,463,493,706,807,361,2,330,399,671,441,545,128,328,439,542,804,557,706,354,848,612,520,261,571,215,599,317,622,684,572,79,195,283,62,738,823,190,702,739,852,268,75,937,895,666,403,874,850,231,512,272,222,360,970,507,586,634,397,447,868,727,390,670,344,144,16,976,621,881,661,774,31,519,890,30,548,352,906,220,724,710,805,862,851,514,928,887,356,452,57,704,608,509,965,123,665,191,427,870,542,936,637,261,667,278,200,309,841,784,21,347,683,267,482,814,630,338,14,57,534,789,131,545,979,410,848,11,985,843,531,342,589,466,619,82,208,77,23,422,193,69,272,576,464,413,658,881,149,474,487,613,262,155,53,741,700,655,988,263,975,469,981,55,857,875,213,412,58,186,486,971,994,403,482,344,789,604,767,141,848,589,835,44,750,611,784,523,679,983,870,33,926,634,162,134,388,241,196,327,76,883,699,738,728,580,237,526,190,187,403,478,200,976,4,107,323,276,422,686,702,838,704,885,885,684,509,723,0,321,41,548,750,897,844,746,910,219,93,152,810,794,84,567,290,739,691,362,872,77,681,77,564,527,878,732,843,132,957,243,351,774,916,509,245,398,12,147,994,680,460,863,635,23,880,515,952,419,641,889,422,92,636,828,440,64,971,925,227,639,2,457,711,667,725,78,124,363,19,706,849,909,567,751,915,385,166,375,598,944,623,730,102,560,275,256,99,531,661,451,472,65,395,357,24,11,943,751,916,170,995,74,156,485,745,698,542,118,364,740,836,149,695,383,921,451,440,332,813,968,989,59,518,488,981,977,215,801,362,821,579,817,268,635,792,292,635,825,617,570,657,100,966,618,929,278,104,43,63,429,100,554,66,910,683,742,919,641,354,35,69,559,255,340,920,835,129,675,580,497,353,894,823,505,301,361,492,972,675,267,513,226,941,637,356,280,968,971,18,141,283,549,335,711,710,419,762,616,994,168,231,674,999,246,509,50,654,18,256,735,95,642,733,485,754,147,983,847,961,137,472,62,144,657,277,286,701,733,810,625,161,184,393,644,64,120,356,410,518,983,129,94,840,276,683,581,331,297,64,438,605,374,507,621,646,104,238,127,122,8,869,628,963,150,322,235,299,847,999,461,334,336,815,566,569,845,258,118,430,831,783,514,79,940,548,391,811,992,566,221,970,536,114,413,714,89,397,971,802,172,609,997,150,190,239,631,475,379,261,407,301,232,274,976,699,854,437,659,469,323,503,492,760,706,45,690,652,928,122,212,460,725,939,891,393,139,52,945,76,1,856,869,672,935,344,670,639,409,379,504,290,42,84,60,884,749,682,834,2,246,420,537,325,876,162,113,337,609,352,229,334,883,461,491,100,470,607,938,532,188,872,626,186,141,315,14,124,120,941,150,831,695,313,997,186,420,818,741,421,343,172,835,626,0,333,25,905,929,374,482,394,875,116,61,175,160,566,785,869,155,450,359,882,439,546,248,736,644,354,619,313,617,359,370,252,624,465,482,344,523,49,504,346,976,153,311,110,287,360,59,508,417,248,200,823,658,890,368,530,385,37,516,424,82,323,350,300,368,87,217,490,53,764,450,700,572,811,581,837,139,948,296,440,915,356,796,512,421,954,699,688,473,908,687,743,987,245,945,910,653,91,496,54,432,574,117,904,731,403,647,101,633,29,644,266,395,595,863,995,772,209,704,601,996,775,104,390,164,146,498,436,316,473,980,180,479,832,701,363,84,721,743,866,171,229,272,745,496,659,601,36,306,309,756,219,985,821,873,15,795,356,224,227,142,215,452,717,801,498,654,94,270,674,387,761,472,693,936,258,74,719,165,575,784,26,907,83,414,343,308,906,444,230,778,702,782,549,913,140,783,820,504,569,249,745,287,239,594,312,352,482,937,418,555,385,682,671,757,29,498,861,166,823,122,286,415,248,269,628,115,691,79,655,770,609,824,529,222,362,607,848,957,574,421,757,935,273,691,988,626,251,827,877,78,830,527,501,988,445,133,360,758,891,672,245,370,495,254,784,894,411,439,152,39,212,746,877,157,903,644,182,282,527,250,939,829,255,806,708,796,446,217,327,693,93,709,664,655,368,214,652,68,801,33,344,171,231,391,162,622,312,561,304,938,344,301,361,780,49,408,228,693,256,804,167,881,671,340,287,657,872,8,936,187,746,69,967,374,299,779,345,695,494,610,552,469,664,817,363,897,674,666,31,868,402,966,368,900,885,99,704,21,561,326,931,31,209,922,61,991,256,744,213,388,586,905,248,694,792,919,54,969,786,265,996,52,972,8,429,194,825,895,841,44,788,848,503,599,226,591,962,305,193,556,403,665,722,948,131,603,323,600,724,613,39,519,693,97,143,292,271,922,282,274,955,766,962,85,354,356,824,18,6,712,776,624,777,926,109,616,572,838,468,139,175,359,867,441,10,697,304,134,551,485,79,579,833,313,526,145,766,863,969,179,3,256,851,828,201,752,86,252,743,506,151,171,226,537,834,319,155,61,879,37,917,272,665,749,496,921,90,936,453,256,1,200,568,866,675,22,788,887,359,424,380,919,806,216,307,529,559,550,327,402,873,641,837,28,241,628,29,862,40,812,493,895,366,688,677,458,638,34,793,688,958,246,322,540,20,543,422,284,558,93,46,82,847,690,762,88,189,218,626,523,215,414,699,42,543,244,506,497,616,632,880,509,262,389,819,408,539,488,223,763,268,936,245,943,599,542,428,434,43,668,70,384,874,339,513,809,742,88,781,507,455,304,692,707,4,32,123,385,549,400,430,950,316,421,910,219,533,783,365,685,548,742,386,389,49,414,478,41,711,64,101,745,832,101,116,213,973,856,66,69,568,81,160,329,805,547,411,359,208,712,178,531,877,414,558,118,349,956,92,181,421,10,80,259,399,166,720,448,957,249,613,915,800,208,229,214,285,64,541,59,603,864,575,215,848,521,98,381,394,923,797,352,887,622,781,619,483,514,561,27,920,406,231,956,68,704,201,122,5,88,944,969,110,664,722,482,649,281,969,740,369,507,861,71,22,891,949,740,260,790,244,329,163,728,872,40,67,150,89,660,820,252,980,586,794,464,256,446,360,439,958,278,485,618,190,621,105,471,728,844,24,988,33,553,370,792,276,906,666,513,43,558,373,721,369,502,15,100,420,865,283,33,956,421,538,535,390,879,510,918,32,502,72,670,560,252,498,763,545,88,247,84,925,135,603,554,543,977,58,353,354,198,987,402,710,383,518,668,354,941,276,829,702,125,477,438,336,327,517,619,919,382,156,412,603,677,81,112,704,610,775,747,72,683,972,830,941,984,446,948,245,43,906,237,395,707,620,881,37,776,60,255,884,321,352,447,108,740,788,292,430,20,725,130,177,19,931,643,854,768,631,851,526,735,175,189,729,494,711,168,110,36,563,333,732,212,945,111,870,88,539,699,662,393,22,119,57,292,46,123,381,442,594,953,278,254,754,124,236,594,316,527,51,903,176,967,519,735,751,447,489,271,315,22,526,494,386,402,601,646,621,600,681,769,13,387,58,281,275,580,25,336,494,905,531,354,70,142,217,973,681,796,970,995,845,566,569,180,911,659,302,262,693,780,203,720,112,438,221,858,722,207,854,580,661,610,806,994,799,644,515,136,640,760,146,650,912,969,878,437,608,38,86,760,766,786,751,361,578,440,937,677,554,36,701,970,807,415,172,237,886,225,166,255,887,577,255,841,956,766,454,21,771,444,451,785,312,934,441,927,63,889,801,658,123,369,318,989,916,964,647,665,339,536,448,557,280,960,598,776,334,942,121,680,61,427,64,33,834,46,901,728,414,334,114,416,929,870,537,447,200,517,82,901,758,474,898,496,118,606,641,43,993,136,757,883,260,120,162,557,417,440,919,717,120,698,404,810,961,628,488,79,319,659,631,912,606,867,726,361,447,617,426,737,410,966,920,971,824,927,640,445,435,698,748,4,130,625,489,983,551,451,849,509,317,404,309,782,774,120,730,608,452,110,371,184,45,730,454,552,606,321,145,329,243,526,278,817,962,174,83,66,830,761,788,113,277,161,754,740,927,458,109,155,661,783,431,175,154,220,444,806,48,919,11,788,764,87,859,159,686,530,169,468,100,102,359,676,3,599,474,748,512,59,104,459,770,640,239,638,517,382,361,769,862,767,88,761,790,847,479,443,551,455,15,459,971,782,232,453,609,130,128,887,856,609,262,670,933,359,965,43,121,596,698,281,36,250,369,461,158,528,719,514,380,943,912,294,970,506,213,384,881,298,529,314,729,76,68,977,539,989,668,968,982,842,681,540,656,500,864,476,444,751,242,948,595,116,135,533,135,133,976,542,209,53,624,137,272,817,102,294,912,312,328,362,260,996,428,640,211,272,676,695,19,187,228,628,512,677,823,85,147,883,984,418,933,847,671,815,689,727,12,701,100,483,736,652,547,40,916,212,318,812,509,853,419,856,480,828,585,539,549,619,123,499,705,881,968,296,771,197,359,517,773,785,873,636,694,516,729,323,638,341,577,335,765,479,682,368,198,269,704,425,211,237,723,227,329,622,880,97,30,569,137,83,229,602,761,410,404,564,173,853,30,17,926,666,657,836,33,432,170,93,289,943,871,153,436,950,647,89,992,364,635,355,258,211,340,262,613,33,784,121,322,175,743,549,794,285,122,892,334,868,552,325,797,762,128,560,983,231,153,836,653,866,220,783,36,107,266,909,739,156,930,74,610,429,136,397,515,37,636,423,598,394,966,283,138,487,156,802,533,487,283,845,895,814,621,33,273,675,171,382,193,997,473,262,672,404,460,71,68,571,173,278,289,482,223,684,260,51,122,184,723,710,190,67,61,403,110,216,789,229,361,549,978,325,754,861,882,494,971,892,825,985,715,664,489,571,990,627,739,214,22,326,166,837,75,583,715,20,149,699,914,302,21,19,728,399,756,722,883,564,440,959,273,971,338,104,46,251,452,879,65,39,64,525,145,153,324,858,642,555,903,143,698,847,503,739,946,704,366,825,802,167,242,161,915,631,494,32,508,751,825,935,2,190,216,756,714,127,795,230,218,748,296,910,258,824,798,71,830,32,660,571,901,773,825,700,356,509,775,577,578,993,368,48,48,486,180,583,404,746,415,182,207,657,265,547,379,989,411,988,348,722,875,488,436,436,928,491,639,496,857,223,691,146,774,762,212,410,399,18,868,885,669,854,510,329,43,265,643,690,189,874,910,48,853,566,44,182,717,627,109,278,684,39,235,880,912,697,168,270,110,371,749,241,590,798,266,734,326,53,731,554,960,261,24,533,19,849,154,371,218,342,519,404,529,846,894,314,897,448,811,854,206,853,978,3,373,472,972,314,822,149,524,886,580,988,439,951,628,442,788,863,713,962,978,529,327,92,708,437,278,548,859,792,599,448,42,690,593,749,272,937,220,489,549,1,677,865,751,619,653,695,245,426,62,190,919,456,763,316,303,620,846,827,524,453,355,345,864,601,870,591,576,109,27,286,173,721,336,812,637,673,448,562,569,126,47,227,926,724,962,518,84,144,241,659,390,243,668,235,282,706,569,914,668,65,638,165,530,441,996,161,420,970,29,799,997,773,429,461,187,761,833,666,527,786,729,647,891,963,400,997,902,510,651,26,300,66,617,322,767,722,513,799,36,692,371,545,698,172,434,546,297,22,984,729,744,588,999,314,315,980,143,168,994,59,788,81,645,388,479,202,168,533,733,256,135,668,725,489,999,749,975,838,977,855,725,990,97,157,503,180,254,743,429,226,741,952,366,239,456,512,608,14,381,96,403,447,619,98,970,756,865,398,531,632,994,146,161,1,778,223,208,547,350,871,412,216,439,313,662,638,478,377,610,802,542,711,633,655,214,553,819,836,998,566,643,794,384,76,107,801,396,216,837,801,690,241,891,314,267,11,99,684,384,123,755,790,831,73,159,773,928,367,50,6,899,972,755,148,552,82,876,414,915,221,464,73,842,20,373,693,924,557,812,377,667,127,966,783,236,147,500,890,610,865,551,57,108,487,135,903,979,319,104,955,287,85,924,901,218,784,786,544,236,498,550,942,595,239,374,907,882,257,514,269,834,625,189,476,409,22,641,382,560,435,483,530,505,585,52,549,659,913,934,402,494,691,66,443,449,455,415,334,866,608,314,343,633,338,557,915,322,107,457,324,420,957,934,143,576,669,732,636,726,396,618,936,265,531,874,715,74,283,897,652,809,533,702,519,68,851,353,150,219,88,412,358,124,590,471,328,532,643,310,836,771,931,975,980,844,251,956,670,118,674,283,592,701,184,974,690,382,826,352,472,436,927,311,921,899,419,278,589,117,117,322,825,212,803,55,648,488,663,771,58,254,383,220,260,542,177,943,806,789,800,851,613,268,490,455,24,159,385,26,133,279,406,17,692,523,804,306,230,273,111,476,721,840,491,915,379,32,810,415,521,408,702,938,177,707,368,37,917,231,934,946,388,443,908,341,597,59,202,782,341,209,587,48,517,923,971,3,491,687,744,180,305,623,997,846,793,922,642,265,86,677,46,959,387,324,27,20,931,744,239,348,413,377,900,193,944,309,53,119,920,250,69,929,498,373,612,932,25,302,113,913,514,919,68,884,511,989,312,776,515,48,572,331,44,964,654,334,797,828,188,18,168,458,343,538,645,171,236,546,327,616,688,932,403,618,677,818,652,788,990,232,732,186,135,620,764,181,681,527,744,884,769,970,603,446,160,233,237,848,769,585,65,256,761,968,298,689,940,561,44,212,787,507,154,161,513,31,100,600,749,964,431,548,29,223,159,926,611,19,284,684,989,77,142,692,286,498,360,725,191,947,730,950,419,322,484,233,496,837,804,520,427,608,933,938,319,419,593,127,305,37,562,241,229,291,327,737,686,214,964,586,845,314,910,574,923,692,1,211,238,603,831,389,403,955,854,991,923,238,515,956,266,74,12,628,217,526,901,197,894,642,864,747,767,181,553,517,8,897,553,536,10,528,827,105,980,962,206,351,677,80,420,4,389,300,134,600,608,945,658,353,455,847,546,269,87,271,40,698,460,146,199,819,983,262,977,577,658,15,243,107,591,534,720,636,228,9,426,693,687,808,188,462,543,599,890,538,601,3,652,143,522,402,408,236,628,710,242,11,57,791,854,95,891,949,310,895,694,828,33,37,271,862,190,590,92,437,962,565,746,470,921,92,619,698,396,142,288,580,642,193,569,470,362,313,946,606,321,323,433,850,697,829,428,654,483,73,188,544,196,52,980,434,436,776,511,517,582,913,584,929,518,681,358,830,101,459,509,796,329,598,216,140,621,236,953,503,410,617,490,500,359,825,386,734,58,106,55,877,332,543,768,417,105,623,28,121,738,31,62,625,487,409,621,982,519,767,362,405,616,473,206,267,741,342,703,720,487,561,159,425,489,794,842,759,993,979,171,807,957,461,269,917,103,865,91,909,927,689,830,371,367,614,2,504,738,971,237,780,471,138,683,597,488,892,888,913,555,895,891,611,730,430,310,348,939,271,538,706,997,897,926,168,561,482,609,149,507,978,651,31,362,601,362,751,893,762,961,3,9,609,441,532,41,877,273,757,330,57,831,115,440,42,456,484,132,383,228,776,129,715,500,808,163,901,800,201,23,331,71,936,419,169,784,111,594,495,518,449,333,757,792,382,59,1,210,139,163,648,531,879,130,266,100,431,470,297,143,410,911,240,764,563,610,618,266,987,230,593,361,39,848,110,385,923,842,336,16,998,938,724,294,507,821,922,801,422,230,173,51,344,801,873,671,39,149,988,303,805,435,484,167,709,746,764,96,208,952,584,966,392,940,277,416,468,930,493,749,330,776,225,114,5,80,512,916,495,81,262,228,562,761,147,611,720,298,926,659,178,609,280,437,763,201,883,128,176,526,711,234,287,388,82,222,169,594,512,200,545,185,495,614,161,323,822,740,973,39,676,80,246,762,498,211,59,393,301,578,521,807,899,165,720,272,700,486,171,230,984,851,835,427,507,104,544,549,629,709,955,717,598,97,658,695,783,160,193,17,385,824,200,721,410,977,583,497,536,194,947,175,734,59,174,118,182,900,958,517,759,912,794,402,547,573,119,316,204,722,383,55,115,969,737,548,881,815,396,284,779,258,428,806,614,449,220,354,431,604,117,479,36,25,103,783,213,918,706,258,708,495,713,10,347,212,385,275,709,384,134,595,908,604,734,215,252,427,562,540,248,600,149,925,670,782,790,44,807,297,294,52,697,806,279,187,188,503,550,856,868,556,282,533,984,327,900,490,681,418,838,453,449,665,702,116,615,803,643,547,330,45,442,278,489,662,877,778,445,472,140,217,974,236,348,995,414,340,204,800,648,1,244,845,306,457,845,328,414,560,824,317,492,846,374,592,407,258,944,636,724,85,40,866,669,87,665,316,814,21,878,712,22,109,324,509,571,654,720,449,569,873,333,165,268,189,862,326,6,613,904,761,726,634,43,345,469,459,949,823,882,125,61,313,140,371,793,864,378,367,901,483,75,705,45,825,605,824,521,88,878,416,685,20,537,676,412,721,710,535,462,57,325,715,515,783,705,916,83,416,22,26,446,963,965,674,461,115,667,335,448,751,274,475,267,934,113,29,34,597,77,846,427,635,108,160,49,706,585,185,941,945,903,994,498,677,151,307,840,36,701,275,425,545,516,923,200,520,129,269,83,704,272,98,938,273]
         ]
    for t in tc:
        print(main(t))
