TOC_HW3
=======

This homework use real-price housing information in Taiwan and find the average of all sale prices matching the condition as the arguments. In order to run this program, the user must provide some arguments during compilation, these arguments are:

*URL = An URL that consists on a JSON file that will later be read to obtain all the data needed.
*City/Distric = Enclosed under the "鄉鎮市區" column in the JSON file.
*Road = A more specific address that have to be part of the "土地區段位置或建物區門牌" column.
*Year = Must be introduced as the Taiwanese year system, ex. 101, 102 ...

After receiving all these paremeters, only those data that match all of them will be counted and their housing's prices will be added to calculate the average of all of them later.
